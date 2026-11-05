import argparse
import importlib.util
import socket
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location("dev", Path(__file__).parents[1] / "dev.py")
dev = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dev)


@pytest.mark.parametrize("port", ["0", "1023", "65535", "70000"])
def test_invalid_port_is_rejected(port):
    with pytest.raises(argparse.ArgumentTypeError):
        dev.application_port(port)


def test_busy_port_is_not_silently_replaced():
    with socket.socket() as occupied:
        occupied.bind(("127.0.0.1", 0))
        with pytest.raises(RuntimeError, match="unavailable"):
            dev.reserve_port(occupied.getsockname()[1])
