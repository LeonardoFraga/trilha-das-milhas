# Brief: curadoria e auditoria de vídeos gratuitos para uma etapa da trilha

Contexto: estamos montando a "Trilha das Milhas", um curso gratuito de milhas e pontos, do básico ao avançado, publicado como site estático no GitHub Pages. Todo o conteúdo em vídeo vem de fontes gratuitas, **somente em português do Brasil** (YouTube de preferência; vale também conteúdo aberto de outras plataformas). A estrutura da trilha está em `pesquisa/TRILHA.md`. Cada etapa tem aulas; cada aula precisa de 1 a 2 vídeos bons.

Hoje é 11/11/2026. Regras de programas mudam rápido: prefira vídeos de 2025–2026; aceite mais antigos só para conceitos que não envelhecem, e diga isso.

## O que fazer

1. Leia `pesquisa/PERSONA-VALERIO.md` e **assuma essa persona integralmente** (Valério, o Auditor das Milhas). Ignore a "Instrução inicial" do fim do arquivo: o conteúdo a auditar são os vídeos que você encontrar.
2. Para cada aula da etapa indicada no seu prompt, busque candidatos no YouTube (WebSearch; WebFetch em páginas de busca/canais do YouTube, `https://www.youtube.com/results?search_query=...`). Prefira canais com histórico sério (ex.: Passageiro de Primeira, Melhores Destinos, Pontos pra Voar, Mestre das Milhas, Rico Gelli, Desconto Passagens Aéreas/Thiago Murta, canais oficiais de Livelo/Smiles/LATAM/Azul, Me Poupe!, Nath Finanças, Primo Rico só quando técnico) — mas avalie cada vídeo pelo conteúdo, não pelo canal.
3. Para cada candidato, **confirme que o vídeo existe e é público**: `curl -s "https://www.youtube.com/oembed?url=<URL>&format=json"` precisa devolver JSON com título e autor. Registre título exato, canal, URL `https://www.youtube.com/watch?v=<id>`, e, se conseguir, data de publicação e duração (a página do vídeo costuma trazer `"publishDate"` e `"lengthSeconds"` no HTML; `curl -s -A "Mozilla/5.0" <url> | grep -o '"publishDate":"[^"]*"'`).
4. Tente obter a **transcrição/descrição** para auditar o conteúdo de verdade (descrição do vídeo, capítulos, legenda automática se acessível). Se só conseguir título + descrição, diga isso e audite com menos confiança.
5. Audite cada vídeo escolhido como o Valério, de forma **compacta**: nota 1–10, risco (Baixo/Médio/Alto), 1–2 frases de veredito, e o principal alerta/omissão que o aluno precisa saber ao assistir (isso vira um aviso no site). Descarte vídeos com promessa de "renda fácil", afiliado escondido sem conteúdo, ou regras claramente desatualizadas — e liste os descartados com o motivo, numa linha.
6. Para cada aula, redija também (em pt-BR, tom claro e sem hype, para iniciante):
   - `porque`: 2–3 frases sobre por que a aula importa.
   - `passos`: 3–5 passos práticos ("Na prática") que o aluno executa depois de assistir.
   - `armadilhas`: 2–4 erros comuns / riscos.
   - `dica`: 1 dica do auditor (pode incluir um cálculo de exemplo; confira a conta).
   Não invente regras específicas de programa (paridades, bônus, preços) como se fossem fixas: quando citar números, diga que são exemplos e que mudam.

## Entrega

Escreva em `dados/etapas/etapa-<N>.json` (caminho absoluto no prompt) um JSON válido neste formato:

```json
{
  "etapa": 1,
  "aulas": [
    {
      "id": "slug-da-aula",
      "nome": "Nome da aula",
      "porque": "...",
      "passos": ["...", "..."],
      "armadilhas": ["...", "..."],
      "dica": "...",
      "videos": [
        {
          "titulo": "título exato do YouTube",
          "canal": "Nome do canal",
          "url": "https://www.youtube.com/watch?v=XXXXXXXXXXX",
          "publicado": "2025-08-14",
          "duracao": "12:34",
          "auditoria": { "nota": 8, "risco": "Baixo", "veredito": "...", "alerta": "..." }
        }
      ],
      "descartados": [ { "url": "...", "motivo": "..." } ]
    }
  ]
}
```

Valide com `python3 -c "import json,sys; json.load(open(sys.argv[1]))" <arquivo>`.

Na resposta final (curta, até ~200 palavras): quantas aulas ficaram com vídeo, quais ficaram sem vídeo bom (e por quê), e qualquer alerta geral sobre a etapa. Não repita o JSON.
