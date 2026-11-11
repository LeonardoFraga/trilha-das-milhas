# Trilha das Milhas

Trilha de estudos gratuita sobre milhas e pontos, do básico ao avançado, só com vídeos gratuitos em português.

**Site:** https://leonardofraga.github.io/trilha-das-milhas/

- 7 etapas: dos fundamentos à proteção do patrimônio (segurança, desvalorização, venda de milhas e imposto de renda)
- Vídeos gratuitos do YouTube, cada um com o parecer de um auditor: nota, risco e o que o vídeo não conta
- Calculadoras: valor do milheiro num resgate, custo do milheiro (CPM) e se a anuidade do cartão se paga
- Glossário com busca, regras de ouro e mapa do ecossistema
- Progresso salvo no próprio navegador

Conteúdo educativo, não é recomendação financeira. Regras dos programas mudam sem aviso: confira sempre o regulamento oficial.

## Como a trilha foi feita

1. **Ponto de partida:** o artigo da Mobills ["Os melhores cursos de milhas do mercado para 2026"](https://www.mobills.com.br/blog/milhas/curso-de-milhas/), com 10 cursos (9 pagos e 1 gratuito).
2. **Auditoria dos cursos:** cada curso foi analisado por um agente com a persona do *Auditor das Milhas* ([`pesquisa/PERSONA-VALERIO.md`](pesquisa/PERSONA-VALERIO.md)), que avalia precisão técnica, matemática, transparência de risco, didática e aplicabilidade. Os relatórios estão em [`pesquisa/cursos/`](pesquisa/cursos/), e o resumo em [`pesquisa/RESUMO-CURSOS.md`](pesquisa/RESUMO-CURSOS.md).
3. **Estrutura própria:** os tópicos que os cursos têm em comum, em ordem do básico ao avançado, mais o que o auditor apontou que eles omitem. Veja [`pesquisa/TRILHA.md`](pesquisa/TRILHA.md).
4. **Curadoria de vídeos:** para cada aula, vídeos gratuitos em pt-BR, conferidos e auditados com a mesma persona ([`pesquisa/BRIEF-CURADORIA-VIDEOS.md`](pesquisa/BRIEF-CURADORIA-VIDEOS.md)). Os vídeos descartados e o motivo ficam registrados em `dados/etapas/`.

## Usar como app no celular

O site é um Progressive Web App: pode ficar na tela de início do celular, com ícone próprio (um avião), e abrir em tela cheia, sem a barra do navegador. Não precisa de loja de aplicativos.

### iPhone (Safari)

1. Abra o site no **Safari**. Pelo Chrome ou outro navegador do iPhone, a opção pode não aparecer.
2. Toque no botão **Compartilhar**, o quadrado com uma seta para cima. Nas versões mais novas do iOS, ele fica dentro do menu **•••**.
3. Role a lista e toque em **Adicionar à Tela de Início**.
4. Se aparecer a opção **Abrir como App Web**, deixe ligada.
5. Confirme o nome ("Milhas") e toque em **Adicionar**.

O ícone do avião aparece na tela de início. Abra sempre por ele.

### Android (Chrome)

1. Abra o site no **Chrome**.
2. Toque no menu **⋮** no canto superior direito.
3. Toque em **Instalar app** ou **Adicionar à tela inicial**.
4. Confirme em **Instalar**.

### Seu progresso no app

O progresso (Assisti, Pratiquei, Apliquei) fica salvo no aparelho, dentro do app. No iPhone, o app da tela de início guarda os dados separado do Safari: o que você marcou no Safari não aparece no app, e vice-versa. Escolha um dos dois para usar sempre.

Apagar o app da tela de início ou limpar os dados do navegador apaga o progresso.

O app precisa de internet para abrir e para tocar os vídeos.

## Como funciona

O site é estático e não tem build no navegador: `index.html`, mais `manifest.webmanifest`, `favicon.svg`, `favicon.ico` e a pasta `icons/`.

Os dados ficam em `dados/`:

- `dados/trilha.json`: etapas e a ordem das aulas, glossário, regras de ouro, mapa do ecossistema e a página "Como esta trilha foi feita".
- `dados/etapas/etapa-N.json`: as aulas de cada etapa (texto, passos, armadilhas, dica) e os vídeos com o parecer do auditor.

Depois de editar qualquer arquivo de `dados/`, rode:

```bash
python3 scripts/montar_site.py
```

O script embute os dados no `index.html` (a linha `const SITE = ...;`). A cada push na `main`, o workflow `.github/workflows/pages.yml` publica a versão nova no GitHub Pages.

Os ícones saem de um único desenho em `icons/gerar_icones.py` (precisa do Pillow: `pip install pillow`).

## Vídeos fora do ar

O workflow `.github/workflows/verificar-videos.yml` confere todos os vídeos toda segunda às 9h (horário de Brasília) e sempre que o `index.html` muda na `main`. Se algum vídeo sair do ar, ele abre uma issue "Vídeos fora do ar" com a etapa, a aula e o link para trocar. Para conferir na hora: `python3 scripts/verificar_videos.py`.

Os vídeos tocam dentro do site pelo player do YouTube (`youtube-nocookie.com`), com um link para abrir no YouTube; nenhum vídeo é hospedado aqui e nenhum link é de afiliado.
