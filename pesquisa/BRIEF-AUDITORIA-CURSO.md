# Brief: auditoria de um curso de milhas

Contexto: estamos montando um "curso" gratuito de milhas (site estático no GitHub Pages, conteúdo 100% de vídeos gratuitos em pt-BR do YouTube ou de outras plataformas gratuitas). O ponto de partida é o artigo da Mobills "Os melhores cursos de milhas do mercado para 2026" (https://www.mobills.com.br/blog/milhas/curso-de-milhas/), que lista 10 cursos. Para cada curso, um auditor analisa a estrutura e o conteúdo, para depois criarmos a nossa própria trilha do básico ao avançado.

Hoje é 11/11/2026.

## O que fazer

1. Leia `pesquisa/PERSONA-VALERIO.md` e **assuma essa persona integralmente** (Valério, o Auditor das Milhas). Ignore a "Instrução inicial" do fim do arquivo (não peça confirmação nem conteúdo): o conteúdo a auditar é o curso indicado no seu prompt.
2. Levante tudo o que for público sobre o curso: página de vendas, ementa/grade (na Udemy a grade de aulas é pública; na Hotmart, a página do produto), descrição do instrutor, avaliações públicas, e amostras gratuitas (aulas abertas, vídeos do mesmo autor no YouTube, Instagram/blog). Use WebFetch e WebSearch. Os cursos são pagos: **não compre nada, não crie conta, não preencha formulário**. Se uma página não carregar, tente a busca ou a versão em cache e registre o que não foi possível ver.
3. Extraia a **estrutura**: módulos e aulas (com títulos, na ordem), carga horária, formato (gravado, ao vivo, comunidade, planilhas), público-alvo, pré-requisitos, e o estilo de apresentação (didático, vendas, "renda extra", etc.).
4. Faça a **auditoria no formato exato da persona** (Veredito Geral → Análise por Pilar → Plano de Correção), sobre as promessas e o conteúdo que deu para ver. Seja explícito sobre o que é inferido da ementa versus o que foi efetivamente visto.
5. Liste os **tópicos** que o curso cobre, normalizados (ex.: "CPM", "clubes de assinatura", "transferência bonificada", "venda de milhas", "tabela fixa x dinâmica", "stopover", "salas VIP", "limite de CPF", "IR sobre venda", "hotéis", "segurança da conta"), marcando o nível que você atribui (Básico / Intermediário / Avançado).
6. Se encontrar **vídeos gratuitos do autor no YouTube** que cubram parte do conteúdo, liste até 5 com título, canal, URL e uma linha sobre a qualidade (passa ou não no crivo do Valério).

## Entrega

Escreva o relatório completo em Markdown no arquivo indicado no seu prompt (caminho absoluto), com estas seções:

```
# <Nome do curso>
## Ficha (autor, plataforma, preço se público, carga, certificado, link, fontes consultadas)
## Estrutura (módulos e aulas)
## Estilo de apresentação
## Auditoria do Valério
### 📑 1. Veredito Geral
### 🔍 2. Análise Detalhada por Pilar
### 🛠️ 3. Plano de Correção e Melhorias
## Tópicos cobertos (com nível)
## Vídeos gratuitos do autor
## Limitações desta análise
```

Na sua resposta final (curta, até ~250 palavras): nota global, nível de risco, a lista de tópicos com nível, os 3 principais alertas e o caminho do arquivo. Não repita o relatório inteiro.
