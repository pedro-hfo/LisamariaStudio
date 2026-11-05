# Publicação no GitHub Pages

## O que é publicado

[Abrir o website](https://pedro-hfo.github.io/LisamariaStudio/).
O repositório público é [pedro-hfo/LisamariaStudio](https://github.com/pedro-hfo/LisamariaStudio).

O Pages serve a apresentação estática React e os guias Sphinx em `docs/pt/` e `docs/en/`. Python não corre no Pages. A apresentação publicada liga ao guia de arranque local em vez de montar o formulário de marcações ou pedir `/api`. Executa a [aplicação local](getting-started.md) para experimentar marcações.

## Acompanhar uma publicação

1. Implementa uma etapa numa branch identificada e faz commits descritivos.
2. Antes do merge, atualiza o README e os guias PT/EN afetados.
3. Faz merge para `main` com `--no-ff` e depois push.
4. Abre a execução em **Actions → Validate and deploy GitHub Pages**. Ao job `build` concluído com sucesso segue-se `deploy`, que apresenta o endereço do site.

Os pull requests executam as mesmas verificações e build sem publicar. Existe também execução manual através de **Run workflow**. Em **Settings → Pages → Source**, seleciona **GitHub Actions**. Para um repositório privado, o GitHub exige um plano que suporte Pages; este repositório é público com autorização do proprietário.

## Compreender o build

`.github/workflows/pages.yml` instala Node 24 e uv, repõe as dependências dos dois lockfiles e executa `npm run check`. Depois executa:

```bash
npm run build:pages
```

`scripts/build_pages.py` constrói o Vite no modo `pages` e gera novamente a documentação Sphinx. Junta o frontend e a documentação em `build/pages`, excluindo a cache de compilação Sphinx. O workflow envia apenas essa pasta e publica-a com credenciais temporárias do GitHub; não guarda um token pessoal no repositório.

`PAGES_BASE_PATH` usa `/LisamariaStudio/` por omissão; o CI obtém o valor a partir do nome do repositório. O `BASE_URL` do Vite mantém recursos e ligações dentro desse caminho. Os comandos normais `npm run dev` e `npm run build` mantêm a interface local de marcações. Se adicionares um domínio próprio, altera também o caminho base do workflow para `/`, além de configurares o domínio no Pages.

## Verificação

`frontend/tests/pages.test.tsx` verifica que o modo publicado apresenta guias PT/EN no caminho do repositório e não faz pedidos ao backend. Os testes de aceitação existentes continuam a cobrir as marcações locais. O Sphinx estrito verifica referências e o teste de paridade exige caminhos correspondentes nos guias PT/EN.

Hint: **build** produz ficheiros; **deploy** publica esses ficheiros. Um build aprovado, por si só, não confirma a publicação. O GitHub documenta o [workflow personalizado](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
