# Como documentar sem sobrecarregar

Cada módulo deve explicar **o que faz, porque existe e como o testar**. Acrescenta detalhe quando ele ajuda a decidir ou compreender; não comentes operações óbvias linha a linha.

## Três níveis

1. **Essencial:** responsabilidade, vocabulário, um exemplo e comando de teste.
2. **Quando precisares:** invariantes, dependências, erros e decisões relevantes.
3. **Referência:** assinaturas e docstrings geradas do código.

Começa pelo primeiro nível. Usa hints para termos novos. Ajustaremos a profundidade à medida que fores ganhando experiência.

## Duas línguas, mesma estrutura

Os guias existem em `docs/pt/` e `docs/en/`, com os mesmos caminhos. O seletor de idioma mantém a página equivalente. Atualiza os dois ficheiros no mesmo trabalho. O glossário preserva os termos ingleses úteis na literatura.

As docstrings Python têm blocos `PT:` e `EN:`; Sphinx seleciona a tradução correspondente. Os comentários TypeScript também têm PT/EN; TypeDoc extrai a referência, integrada no Sphinx. Os nomes e assinaturas de código mantêm-se iguais.

```python
def execute(...):
    """PT: Descreve a intenção em português.

    EN: Describe the intention in English.
    """
```

O servidor recompila referências quando o código muda. Os ficheiros `reference/generated/` são derivados e não se editam manualmente. Os cenários publicados são gerados a partir dos `.feature`, para evitar cópias desatualizadas.

## Adicionar um módulo

Cria o módulo no código e a pasta com o mesmo nome em `acceptance/`. Acrescenta um guia equivalente em PT/EN, atualiza os índices e o glossário. Documenta primeiro um comportamento; só depois cria as abstrações que esse comportamento exigir.

`npm run docs:build` trata avisos de documentação como erros. O teste de paridade verifica que os guias têm equivalentes nos dois idiomas e que os cenários mantêm os mesmos IDs e estrutura.
