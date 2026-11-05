# Começar

## Instalar uma vez

Requisitos: Node 22.12+ (24 recomendado para este repositório), npm, uv e Python 3 para executar o instalador. Em macOS: `brew install node@24 uv`. O uv descarrega o Python 3.13 do projeto e cria `.venv/`.

Na raiz:

```bash
npm run setup
npm run dev -- --port 3000
```

| Endereço | Serviço |
|---|---|
| `http://127.0.0.1:3000` | Aplicação React |
| `http://127.0.0.1:3001` | Documentação Sphinx PT/EN |
| `http://127.0.0.1:3000/api/docs` | Contrato HTTP interativo do FastAPI |

`--port x` coloca a documentação em `x+1`. O backend usa uma porta interna livre, exposta ao navegador através de `/api`. Os dois endereços de utilização continuam a ser `x` e `x+1`. O comando mostra os endereços depois de verificar que os quatro pontos de entrada respondem.

**Ctrl+C termina todos os processos**, incluindo os processos de recarregamento. Se uma porta estiver ocupada, o comando falha com uma mensagem; não muda silenciosamente de porta. Os logs ficam em `.cache/dev/<processo>/`.

## Experimentar

Cria uma marcação futura. Repete a mesma hora para observar a rejeição de um conflito. Uma sessão de exemplo dura 60 minutos e deixa 15 minutos para preparação. Estes valores aguardam decisão de negócio. A hora introduzida usa o fuso do dispositivo, indicado junto ao campo; a API exige um instante com fuso.

O exemplo guarda dados em memória. Reiniciar ou alterar o backend limpa a agenda. Não introduzas dados de clientes: o exemplo nem sequer os solicita.

## Verificar

```bash
npm run check
.venv/bin/pytest acceptance/backend -v
npm test
npm run docs:build
npm run dev -- --port 4100 --check
```

O último comando inicia, verifica e termina os serviços. `npm run check` verifica estilo Python, tipos, regras de arquitetura, BDD, componentes React, build e documentação estrita. Usa `uv.lock` e `package-lock.json` para reproduzir as dependências.

## Recarregamento

Vite atualiza o front-end; Uvicorn reinicia o backend; Sphinx reconstrói a documentação ao mudar guias, código ou cenários. As alterações a `docs/conf.py` ou aos próprios scripts de arranque pedem um reinício do comando.
