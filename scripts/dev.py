"""PT: Inicia e supervisiona aplicação + documentação.

EN: Start and supervise the application + documentation.
"""

import argparse
import os
import signal
import socket
import subprocess
import sys
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
BIN = ROOT / ".venv/bin"


def application_port(value):
    port = int(value)
    if not 1024 <= port <= 65534:
        raise argparse.ArgumentTypeError("Port / Porta: 1024–65534 (x+1 is reserved for docs).")
    return port


def reserve_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.bind(("127.0.0.1", port))
    except OSError:
        sock.close()
        raise RuntimeError(f"Port {port} is unavailable / A porta {port} está ocupada.") from None
    return sock


def stop_processes(processes):
    # Each service owns a process group, including Vite/Uvicorn reload workers.
    for process in reversed(processes):
        try:
            os.killpg(process.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
    for process in reversed(processes):
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            process.wait(timeout=5)


def ready(url):
    try:
        with urlopen(url, timeout=1) as response:
            return response.status == 200
    except (URLError, OSError):
        return False


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=application_port, default=3000)
    parser.add_argument(
        "--check", action="store_true", help="Start, verify, then stop all services."
    )
    args = parser.parse_args(argv)
    if not (BIN / "uvicorn").exists() or not (ROOT / "node_modules/.bin/vite").exists():
        parser.exit(1, "Run / Executa: npm run setup\n")
    processes, reservations = [], []
    log_files = []
    logs = ROOT / ".cache/dev" / str(os.getpid())
    logs.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, PYTHONUNBUFFERED="1", LISAMARIA_APP_PORT=str(args.port))
    signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))
    try:
        # Fail before starting any service if either public port is occupied.
        app_socket = reserve_port(args.port)
        reservations.append(app_socket)
        docs_socket = reserve_port(args.port + 1)
        reservations.append(docs_socket)
        backend_socket = reserve_port(0)
        reservations.append(backend_socket)
        backend_port = backend_socket.getsockname()[1]
        env["LISAMARIA_API_URL"] = f"http://127.0.0.1:{backend_port}"

        def launch(name, command, **kwargs):
            log = (logs / f"{name}.log").open("w")
            log_files.append(log)
            process = subprocess.Popen(
                command,
                cwd=ROOT,
                env=env,
                stdout=log,
                stderr=subprocess.STDOUT,
                start_new_session=True,
                **kwargs,
            )
            processes.append(process)
            return process

        # A fresh strict build prevents an old HTML directory masking a broken build.
        docs_build = launch(
            "docs-build",
            [
                str(BIN / "sphinx-build"),
                "-W",
                "--keep-going",
                "-b",
                "html",
                "docs",
                "build/docs-live",
            ],
        )
        try:
            build_status = docs_build.wait(timeout=90)
        except subprocess.TimeoutExpired:
            raise RuntimeError(
                "Documentation build timed out / A documentação excedeu o tempo."
            ) from None
        if build_status != 0:
            raise RuntimeError("Documentation build failed / Falhou o build da documentação.")
        processes.remove(docs_build)

        launch(
            "backend",
            [
                str(BIN / "uvicorn"),
                "lisamaria.bootstrap:create_app",
                "--factory",
                "--fd",
                str(backend_socket.fileno()),
                "--reload",
                "--reload-dir",
                "backend/src",
            ],
            pass_fds=(backend_socket.fileno(),),
        )
        backend_socket.close()
        app_socket.close()
        launch(
            "frontend",
            ["npm", "run", "dev", "--workspace", "frontend", "--", "--port", str(args.port)],
        )
        docs_socket.close()
        launch(
            "docs",
            [
                str(BIN / "sphinx-autobuild"),
                "docs",
                "build/docs-live",
                "--no-initial",
                "-W",
                "--host",
                "127.0.0.1",
                "--port",
                str(args.port + 1),
                "--watch",
                "backend/src",
                "--watch",
                "frontend/src",
                "--watch",
                "acceptance",
                "--watch",
                "scripts/docs_generate.py",
                "--ignore",
                "*/reference/generated/*",
                "--ignore",
                "*/__pycache__/*",
            ],
        )
        urls = [
            f"http://127.0.0.1:{args.port}/api/health",
            f"http://127.0.0.1:{args.port}/",
            f"http://127.0.0.1:{args.port + 1}/pt/index.html",
            f"http://127.0.0.1:{args.port + 1}/en/index.html",
        ]
        pending = set(urls)
        deadline = time.monotonic() + 90
        print("Starting / A iniciar…", flush=True)
        while pending:
            if any(process.poll() is not None for process in processes):
                raise RuntimeError(
                    "A service stopped during startup / Um serviço parou no arranque."
                )
            pending = {url for url in pending if not ready(url)}
            if time.monotonic() > deadline:
                raise RuntimeError(
                    "Startup timeout / Tempo de arranque excedido: " + ", ".join(pending)
                )
            if pending:
                time.sleep(0.2)
        print(
            f"App:  http://127.0.0.1:{args.port}\n"
            f"Docs: http://127.0.0.1:{args.port + 1}\n"
            f"API:  http://127.0.0.1:{args.port}/api/docs\n"
            f"Logs: {logs}\nCtrl+C stops everything / termina todos os serviços.",
            flush=True,
        )
        if args.check:
            return 0
        while True:
            if any(process.poll() is not None for process in processes):
                raise RuntimeError("A service stopped / Um serviço parou.")
            time.sleep(0.5)
    except KeyboardInterrupt:
        return 0
    except (RuntimeError, OSError) as error:
        print(str(error), file=sys.stderr)
        for path in logs.glob("*.log"):
            print(f"\n{path.name}:\n{path.read_text()[-5000:]}", file=sys.stderr)
        return 1
    finally:
        stop_processes(processes)
        for sock in reservations:
            sock.close()
        for log in log_files:
            log.close()


if __name__ == "__main__":
    sys.exit(main())
