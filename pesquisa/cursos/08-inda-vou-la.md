# Inda Vou Lá com Milhas (produto Hotmart "be-a-ba-das-milhas-aereas")

> Auditoria feita em 11/11/2026 por "Valério, o Auditor das Milhas". Curso nº 8 da lista da Mobills.

## Ficha

| Campo | Dado |
|---|---|
| **Título na Hotmart** | "Inda Vou Lá com Milhas". O slug da URL (`be-a-ba-das-milhas-aereas`) vem do nome anterior da oferta, o **"Desafio Bê-a-Bá das Milhas"**, que o autor divulgava no YouTube em março de 2020. |
| **Autor** | **José dos Reis Luz Junior**, que assina como **"José Panda"** no blog Inda Vou Lá (usuário WordPress `jreisjr`, o mesmo handle do Facebook e do Twitter cadastrados na Hotmart). É o "triatleta" citado pela Mobills: a bio da Hotmart termina com "Triatleta rumo a Kona", e o canal dele tem um vídeo da Maratona Internacional de Florianópolis. É engenheiro, de São Luís (MA). A bio na Hotmart diz: mais de 50 países, uma volta ao mundo em 365 dias com a família (2017), "milhões de milhas conquistadas e vendidas", "top cartões de crédito do mercado" e uma agência de viagens em grupo para Ásia e África. No blog, ele se descreve como "consultor de milhas aéreas e cartão de crédito". O blog foi fundado em 2009 por **Renata Marques**, que hoje assina o Instagram. |
| **Plataforma** | Hotmart. productId 1872951, código V65128131T. Formato "Cursos Online e Serviços de Assinatura", área de membros Hotmart Club, categoria Finanças/Negócios. Perfil verificado, conta na Hotmart desde 16/02/2015. |
| **Status de venda (hoje)** | **Não está à venda.** O JSON da página traz `salesEnabled: false`, e o marketplace indica produto indisponível. A Hotmart não mostra preço, avaliações nem contagem de alunos (`totalUsers: 0`, `reviews: []`). |
| **Preço (histórico)** | Na landing page do blog (indavoula.com.br/curso-milhas, de 2022): **"De R$ 497,00 por R$ 297,00"**. O link de checkout trazia o cupom `IVL40`. |
| **Carga** | **9 módulos com 20 aulas**, todas gravadas. A carga horária não foi divulgada: a landing diz "não existe uma duração estimada". **A Mobills está errada ao dizer "9 aulas"**: 9 é o número de módulos. |
| **Extras prometidos (2022)** | 3 planilhas: valor das milhas em R$, passagem por pontos ou dinheiro e desconto equivalente em produtos. Também 3 aulões de tira-dúvidas ao vivo **em 2022**, um "Desafio 14 dias" (checklist de 10 min/dia) e um "programa de bonificação" com "bônus surpresa". |
| **Suporte / acesso** | "Garantimos acesso ao conteúdo por pelo menos um ano. O suporte ficará ativo por 3 meses a partir da sua compra." |
| **Garantia** | 7 dias pela Hotmart (o campo `warranty: 7`). A landing também prometia uma **"garantia condicional de 12 meses"**, analisada no Pilar 2. |
| **Certificado** | Não (`certification: false`). |
| **Datas** | Produto criado na Hotmart em **14/01/2022** e publicado em **07/02/2022**. A landing foi modificada pela última vez em **22/05/2022** e tem rodapé "® 2022". O método começou antes, no Desafio Bê-a-Bá (mar/2020). **Ajuste à Mobills, que fala em "existe há 7 anos na Hotmart"**: o produto atual tem cerca de 4 anos e 10 meses. Contando o Desafio de 2020, são uns 6 anos e 8 meses. A conta do autor na Hotmart tem 11 anos. |
| **Público-alvo declarado** | "Pessoas que querem aprender a ganhar mais pontos e milhas aéreas". A landing diz servir a quem nunca acumulou e "mesmo que você não use cartão de crédito". |
| **Link** | https://hotmart.com/pt-br/marketplace/produtos/be-a-ba-das-milhas-aereas/V65128131T |

**Fontes consultadas**
- Página do produto na Hotmart. O WebFetch não trouxe os dados, então baixei o HTML e li o `__NEXT_DATA__`. De lá saíram a copy, a lista de vantagens, a **grade completa (`productSummary.modules`)**, a bio do produtor, as datas `createdAt` e `publicationDate`, os campos `salesEnabled`, `warranty` e `certification` e as tags.
- O checkout `pay.hotmart.com/V65128131T` é renderizado no navegador e não trouxe preço. Não preenchi nada.
- Landing do próprio autor: https://www.indavoula.com.br/curso-milhas/ (preço, bônus, garantias, FAQ).
- Blog Inda Vou Lá, via API pública do WordPress (`/wp-json/wp/v2/posts?search=milhas`, `/wp-json/wp/v2/users`). Li na íntegra 8 posts de milhas assinados por José Panda: guia inicial, quanto vale uma milha, meus cartões em 2021, pagar boleto com cartão, eletrodomésticos com desconto, Livelo × LATAM Pass, milhas Smiles vencendo e iPhone mais barato. Também li a página "Quem somos".
- Canal do YouTube `youtube.com/indavoula`, hoje renomeado para **"Enjoy Mundo"** (@EnjoyMundo, 632 inscritos, 36 vídeos), consultado pelo feed RSS, oEmbed e metadados das páginas de vídeo.
- Instagram @indavoula, pelo WebFetch: 12,7 mil seguidores. A bio hoje é assinada por Renata Marques e o foco é blog e consultoria de viagem, não milhas.
- Mobills: "Os melhores cursos de milhas do mercado para 2026", seção 8.

---

## Estrutura (módulos e aulas)

A grade abaixo é a **oficial**, tirada do `productSummary` da página da Hotmart, na ordem original. A Hotmart não publica durações nem prévias.

**Módulo 1. Apresentação do curso** (1 aula)
1. Introdução

**Módulo 2. Introdução ao universo das milhas** (4 aulas)
2. Dicas iniciais e principais dúvidas do universo das milhas
3. Banco x Programa x Companhia Aérea
4. Programas, clubes e transferências
5. Qual programa escolher

**Módulo 3. Programas de fidelidade** (3 aulas)
6. Primeiros passos nos programas
7. Programa gerenciador de pontos
8. Transferindo pontos Livelo

**Módulo 4. Cartões de Crédito** (1 aula)
9. Melhores cartões de crédito

**Módulo 5. Acumulando Milhas** (8 aulas, o maior módulo)
10. Clubes de Fidelidade
11. Comprando produtos
12. Acumulando com aplicativo de transporte
13. Acumulando com hospedagem
14. Acumulando com aluguel de carro
15. Posto de combustível
16. Compra de pontos
17. Reativando milhas

**Módulo 6. Como usar meus pontos** (1 aula)
18. Usando meus pontos e milhas

**Módulo 7. Como vender meus pontos** (1 aula)
19. Vendendo meus pontos e milhas

**Módulo 8. Bônus: melhor comprar em dinheiro ou com pontos?** (1 aula)
20. Aprendendo a usar a planilha comparadora

**Módulo 9. Bônus: planilha controle de pontos** (1 aula + planilha)
21. Planilha Controle de Pontos

> A Hotmart lista 21 títulos. Sem a aula "Introdução", que só apresenta o curso, são **20 aulas de conteúdo**.

**Leitura da grade.**
- A distribuição é desequilibrada. **Acúmulo** tem 8 aulas, enquanto **uso/resgate** e **venda** têm **uma aula cada**.
- **Cartões de crédito** também ganha uma aula só, apesar de ser o eixo da copy.
- Não há aula sobre:
  - emissão de passagem (busca de disponibilidade, tabela fixa × dinâmica, taxas de embarque, parceiras, stopover);
  - programas internacionais;
  - limites de CPF ou beneficiários;
  - riscos de venda (bloqueio, regulamento);
  - imposto de renda;
  - segurança da conta;
  - salas VIP.
- **Formato:** aulas gravadas, planilhas, suporte por 3 meses e, só em 2022, aulões ao vivo. Não há comunidade (`hasCommunity: false`). O blog divulga grupos no Telegram.

---

## Estilo de apresentação

- **Copy de vendas com apelo emocional e de "lucro".** A copy da Hotmart fecha com **"Vamos lucrar!"**, e a resposta gerada por IA na página resume o objetivo como "ajudar as pessoas a **lucrar** com suas milhas". A landing usa urgência ("A cada dia que passa, mais milhas são deixadas de presente para os bancos") e um número sem fonte ("você nunca mais vai ajudar a aumentar o lucro dos bancos em mais de **1 bilhão de reais por ano**"). Também promete "Embarque em uma jornada sem volta" e "Desconto de até 40%" em celulares e eletrodomésticos.
- **Tom do autor nos posts: didático, de blogueiro-viajante, em primeira pessoa.** Usa analogias boas (cartão fidelidade da sorveteria, "capinhas de brinde" para explicar o desconto equivalente), assina "Um abraço de Panda" e conta casos pessoais: ar-condicionado comprado com promoção Riachuelo/Livelo, venda de milhas na Hotmilhas.
- **Conteúdo atravessado por monetização.** Os posts têm banners do curso a cada 2 ou 3 parágrafos, links de indicação de apps (RecargaPay, Ame, PicPay) e convites para consultoria de milhas. Há até um "antes de comprar sua passagem, entre em contato comigo para verificar se consigo um valor mais barato", ou seja, venda de emissões com milhas. O autor é **parte interessada**: vende milhas, emissões e consultoria.
- **Público:** iniciante absoluto. O discurso é "do zero", com promessa de nível "básico ao avançado" num banner, mas a grade é claramente básica a intermediária.

---

## Auditoria do Valério

> **O que foi efetivamente visto e o que foi inferido.** As aulas pagas **não foram vistas**: o produto nem está à venda, e não comprei nem criei conta. O que vi: (a) a grade oficial e a copy da Hotmart; (b) a landing de vendas de 2022; (c) **8 artigos de milhas do mesmo autor**, escritos entre 2020 e 2023 e linkados com banners do curso, que tomo como **amostra do conteúdo e do raciocínio** dele; (d) os metadados e descrições de 2 vídeos de 2020. Tudo o que digo sobre as aulas é **inferência a partir da ementa e dessas amostras**.

### 📑 1. Veredito Geral

- **Nota Global:** **4/10**
- **Nível de Risco para o Leitor:** **Alto** (para quem consumir esse material em 2026)
- **Resumo Executivo:**
  - O esqueleto é um bom "bê-a-bá": banco × programa × companhia aérea, não deixar expirar, não trocar pontos por "panelas", comparar pontos × dinheiro, controlar saldos.
  - O autor tem prática real, e a ideia de "desconto equivalente" é útil.
  - Mas o produto está **parado desde 2022** e **fora de venda**. As amostras mostram valores, programas e plataformas **que já não existem ou mudaram muito**: iupp, TudoAzul, preços de clubes, milheiro a R$ 40 "garantido", venda via HotMilhas/MaxMilhas.
  - A venda de milhas é tratada como rotina, **sem nenhum aviso** de regulamento, bloqueio, risco de contraparte ou imposto.
  - Como material de referência para 2026, **não passa** no crivo.

### 🔍 2. Análise Detalhada por Pilar

#### Alertas / Incorreções Técnicas

**Pilar 1. Precisão técnica e atualização (o ponto crítico deste curso)**

| Afirmação nas amostras do autor (2021–2023) | Situação em 11/11/2026 |
|---|---|
| Recomenda vender milhas pela **Maxmilhas e Hotmilhas**: "nunca tive nenhum tipo de problema". Cita a Hotmilhas como referência de cotação do milheiro. | O grupo **123milhas** (dono da HotMilhas) entrou em **recuperação judicial em agosto de 2023**, e a MaxMilhas, do mesmo grupo, foi incluída no processo. Muitos vendedores de milhas ficaram sem receber. Hoje esse conselho é **perigoso** sem uma ressalva de risco de contraparte. |
| "Sempre Presente **ou IUPP**, do Itaú" e "uma milha Itaú/**Iupp** vale R$ 0,04". | A marca **iupp foi descontinuada** pelo Itaú. Os pontos voltaram a programas próprios do banco. É **regra desatualizada**. |
| "**Tudo Azul**, da Azul". | O programa virou **Azul Fidelidade** em 2024. Além disso, a Azul entrou em **Chapter 11 nos EUA em maio de 2025** e a Gol passou pelo mesmo processo entre jan/2024 e jun/2025. Um curso de 2026 precisa falar de **risco de programa/companhia**, e este não fala. |
| Clubes "a partir de 1.000 pontos": **R$ 35,00** (Tudo Azul), **R$ 39,90** (Smiles), **R$ 42,90** (LATAM Pass). | Preços e estruturas de clube mudaram várias vezes desde 2022. Os valores citados **não servem para cálculo hoje**. |
| "Cerca de uma vez por mês acontece uma promoção de transferência com bônus **entre 70% e 120%**", portanto "1.000 milhas no cartão valem **R$ 40,00**". | Generaliza um momento do mercado (2021–2023). Frequência, teto e condições (muitas vezes **exclusivas para assinantes de clube**) variam, e as regras de bônus mudaram. Tratar como constante é erro de premissa. Veja o Pilar 2. |
| "15.000 pontos é o suficiente para uma passagem ida e volta de São Paulo a Recife." | É tabela de 2021 e caso de promoção. Smiles, LATAM Pass e Azul Fidelidade operam com **preço dinâmico**, e o mesmo trecho pode custar várias vezes mais. |
| "38 mil pontos [TAP] já é suficiente para emitir uma passagem do Brasil para o México, Canadá ou Europa." | Sem dizer que é **só ida**, em **baixa temporada**, sujeito a disponibilidade e **com taxas e sobretaxas** em dinheiro. A afirmação é **irrealista** como regra. |
| Melhor cartão "em 2023" é o **Pão de Açúcar Itaucard**, 1 ponto/real, com transferência de 1:1 para TudoAzul e 1:0,88 para Smiles/LATAM. Amex Platinum Bradesco com 2,2 pts/US$. | Paridades, pontuação e até a emissão desses cartões mudaram desde então. Não validei a situação atual de cada um. **Precisa ser reverificado**, nunca ensinado como verdade. |
| Pagar boletos com cartão "sem taxas" via RecargaPay, Ame, PicPay, Mercado Pago e 99Pay. | O próprio post já registrava taxas de 2,99% e limites cortados. Desde então o cenário mudou de novo (a Ame, por exemplo, foi afetada pela crise da Americanas). É estratégia de **validade curtíssima**. |
| Reativação Smiles a **R$ 60 por mil milhas**. | Valor de 2020–2021, sem data no texto. |

**Pilar 2. Viabilidade matemática e financeira**

- **"Milha do cartão vale o dobro" (R$ 40 o milheiro).** A conta assume três coisas ao mesmo tempo, e nenhuma é garantida:
  1. que **toda** transferência pegue 100% de bônus;
  2. que o aluno **venda** as milhas pelo preço de mercado;
  3. que o custo do clube exigido para o bônus seja **zero**.
  
  Com 100% de bônus e milheiro vendido a R$ 20, 1.000 pontos do banco valem R$ 40 **brutos**. Mas, se o bônus exige um clube de R$ 40 a R$ 80 por mês, quem transfere pouco **perde dinheiro**. O curso precisa mostrar o ponto de equilíbrio. Ainda falta descontar a anuidade do cartão que gerou os pontos.
- **Caso do ar-condicionado (post de 2022).** Preço de R$ 1.799 × 12 pts/R$ = 21.588 pontos Livelo. Com +80% de bônus na transferência para a TAP, viram cerca de 38.880. Vendidos a R$ 30 o milheiro, rendem cerca de R$ 1.166. Resultado: "saiu por R$ 635". A aritmética fecha, mas:
  - a promoção era **só para assinantes do Clube Livelo**, e a mensalidade foi omitida;
  - o milheiro de **R$ 30** contradiz o próprio post "Quanto vale uma milha", que cotava a HotMilhas a **R$ 18–27**. Com R$ 20, o "desconto" cai de 65% para cerca de 43%;
  - o post também tem data inconsistente ("último trimestre de 2021" contra "18 de novembro de 2022").
  
  É um caso de **melhor cenário apresentado como replicável**.
- **"Desconto de até 40%" (landing).** Depende de promoção pontual, de clube pago e de **vender milhas**. Sem esse contexto, é promessa enganosa.
- **"Bancos lucram mais de R$ 1 bilhão/ano" com pontos expirados.** O número não tem fonte. Exijo comprovação.
- **"Garantia condicional de 12 meses."** Promete devolver o dinheiro se, gastando R$ 2.500/mês, o aluno não acumular **4.000 pontos em 12 meses**. Esses R$ 30.000/ano num cartão básico de 1 pt/US$ (com dólar a ~R$ 5) já rendem cerca de 6.000 pontos sem curso nenhum. A barra é tão baixa que a garantia é **marketing**, não compromisso de resultado. E 4.000 pontos valem cerca de R$ 70–160.
- **Custos ocultos.** O guia inicial menciona anuidade e isenção por gasto mínimo, o que é ponto positivo. Mas não há, nas amostras:
  - IOF/spread em compras internacionais nos cartões "por dólar";
  - taxas de embarque e sobretaxas nos resgates;
  - custo de oportunidade de antecipar gastos;
  - **imposto de renda sobre a venda recorrente de milhas**.

**Pilar 3. Transparência e gestão de risco**

- **Venda de milhas sem aviso de regulamento.** O módulo 7 e os posts tratam a venda como natural ("Vamos lucrar!"). Os regulamentos dos programas de companhias aéreas **proíbem a comercialização** de milhas e prevêem cancelamento de conta e de saldo. **Não há uma linha sobre isso** nas amostras.
- **Risco de contraparte ignorado.** O autor chancela as plataformas que depois entraram em recuperação judicial, sem errata no post (modificado pela última vez em 2022).
- **Conflito de interesses não declarado.** O autor vende milhas e emissões ("entre em contato comigo"), consultoria e assessoria, e ganha com links de indicação de apps. O leitor não é avisado de que a recomendação pode ser enviesada.
- **Limites de CPF/beneficiários e bloqueios** por emissões para terceiros: ausentes.
- **Desvalorização e tabela dinâmica**: ausentes. Há só um genérico "mudanças acontecem da noite para o dia".
- **Endividamento e limite.** O "troque débito por crédito" vem com a ressalva "desde que você não pague mais caro", o que é bom, mas não há alerta sobre concentrar contas no cartão e o risco de rotativo. O post de boletos ensina a **concentrar todas as contas no cartão** e até a transferir saldo entre cônjuges para fugir da taxa, sem nenhum aviso de disciplina financeira.

#### Pontos Fortes

- **Separação clara entre banco, programa de fidelidade e companhia aérea** (aula 3). É a confusão nº 1 de iniciantes.
- **"Milha é moeda".** Ensinar a **precificar** o ponto antes de trocar ("nunca mais troque milhas por panelas que custam 3x mais", a sanduicheira de R$ 60 que sai por R$ 180 em pontos) é a lição mais valiosa do material.
- **Planilha comparadora "pontos × dinheiro"** e o conceito de **"desconto equivalente"**, explicado com a analogia das capinhas. São boa didática, desde que alimentados com dados atuais.
- **Controle de saldos e validade** (apps como AwardWallet e planilha), e a regra "a única coisa que não pode acontecer é deixar seus pontos expirarem".
- **Prioridade de uso sensata:** transferir com bônus, depois passagem, venda, produtos e, por último, doação. É coerente com a lógica de valor, ressalvada a questão regulatória da venda.
- **Cobertura ampla das fontes de acúmulo** (shopping, transporte, hotel, locadora, combustível), adequada a quem não tem cartão premium.
- Fala de **isenção de anuidade por gasto mínimo** e de "o melhor cartão que a sua renda permita". O tom é menos agressivo que o de outros cursos da lista.

#### Omissões Perigosas

1. **Proibição de venda nos regulamentos** e risco de bloqueio ou cancelamento de conta e saldo.
2. **Risco de contraparte** em plataformas de compra de milhas, com o caso 123milhas/MaxMilhas.
3. **Risco do programa e da companhia**: recuperação judicial e Chapter 11 de companhias aéreas brasileiras, desvalorização, mudança unilateral de regras.
4. **Tabela dinâmica × fixa** e como **buscar disponibilidade real**. Uma aula só de "usar pontos" não ensina a emitir bem.
5. **Limites de CPF e beneficiários** por programa.
6. **Imposto de renda** sobre ganhos com venda recorrente de milhas, que tem enquadramento controverso e pede orientação contábil.
7. **IOF/spread** nos cartões que pontuam por dólar, **taxas de embarque** e sobretaxas.
8. **Data de validade das informações.** O material não avisa o aluno de que números e programas de 2022 podem não valer mais.
9. **Segurança da conta**: senha, 2FA, golpes de "compro suas milhas".

### 🛠️ 3. Plano de Correção e Melhorias (Sugestões Concretas)

**Reescritas propostas**

- *Original (post "Quanto vale uma milha"):* "Os pontos dos cartões de crédito valem mais do que as milhas das companhias aéreas porque existem diversas promoções que fazem os seus pontos dobrarem. [...] 1.000 milhas no cartão de crédito vão valer R$ 40,00."
  *Proposta:* "Um ponto de banco **pode** render mais que uma milha de companhia **se** você transferir numa promoção de bônus. Exemplo: com 100% de bônus, 1.000 pontos viram 2.000 milhas. Esse valor só se realiza se as condições da promoção estiverem disponíveis para você (muitas exigem clube pago) e se as milhas forem bem usadas. Antes de assinar um clube para pegar o bônus, calcule: (mensalidade × meses) ÷ milhas extras ganhas = custo por mil das milhas de bônus. Se esse custo for maior que o valor que você atribui ao milheiro, o bônus não compensa."

- *Original (guia inicial):* "Eu, particularmente, já vendi milhas por essas duas plataformas [Maxmilhas e Hotmilhas] e nunca tive nenhum tipo de problema."
  *Proposta:* "⚠️ Atualização: em 2023 o grupo 123milhas, dono da HotMilhas, entrou em recuperação judicial e a MaxMilhas foi incluída no processo. Muitos vendedores ficaram sem receber. Além disso, os regulamentos de Smiles, LATAM Pass e Azul Fidelidade **proíbem a comercialização** de milhas e prevêem cancelamento da conta. Vender milhas é uma operação de **risco regulatório e de contraparte**, não uma 'renda garantida'."

- *Original (Hotmart):* "Saiba como vender os seus pontos. Vamos lucrar!"
  *Proposta:* "Entenda quanto valem seus pontos, para nunca trocá-los por menos do que valem, e conheça os riscos de quem decide vendê-los."

- *Original (landing):* "Aprender a usar pontos para garantir até 40% de desconto na compra de produtos."
  *Proposta:* "Em promoções pontuais de pontos extras por real, a compra pode gerar um 'desconto equivalente' relevante. O percentual depende da promoção, do custo de clubes exigidos e do valor que você consegue obter com as milhas. Mostramos a conta completa, com cenários pessimista, realista e otimista."

- *Original (guia inicial):* "Se esperasse uma promoção dessas [...] você poderia ganhar 15.000 pontos! Isso é o suficiente para uma passagem ida e volta de São Paulo a Recife."
  *Proposta:* "...15.000 pontos. Em 2021 isso chegou a pagar um ida e volta SP–Recife em promoção. Hoje os programas usam **preço dinâmico**: o mesmo trecho pode custar de poucos a dezenas de milhares de pontos conforme data e demanda. Sempre pesquise o preço em pontos e em reais antes de decidir."

**Disclaimers obrigatórios**

1. "**Conteúdo gravado em 2022.** Valores de milheiro, preços de clubes, paridades de transferência, cartões e até nomes de programas mudaram. Confira tudo no regulamento vigente antes de agir."
2. "**Venda de milhas** é vedada pelos regulamentos dos principais programas e pode levar ao cancelamento da conta e do saldo. Plataformas intermediárias podem quebrar (caso 123milhas, 2023). Venda recorrente pode ter implicações de imposto de renda: consulte um contador."
3. "**Conflito de interesses:** o autor vende consultoria, emissões e milhas, e recebe por links de indicação."
4. "**Cartão de crédito é dívida.** Só concentre gastos no cartão se pagar a fatura integral. Os juros do rotativo anulam qualquer ganho com milhas."
5. "**Disponibilidade de assentos** com milhas é limitada e variável. Exemplos de 'X mil pontos para a Europa' são casos de promoção e baixa temporada, normalmente só ida, mais taxas."

**Melhorias estruturais**
- Dividir "Como usar meus pontos" em pelo menos 4 aulas:
  - busca de disponibilidade e tabela fixa × dinâmica;
  - parceiras e programas internacionais;
  - taxas e sobretaxas;
  - stopover, upgrade e salas VIP.
- Substituir "Como vender meus pontos" por uma aula sobre **valor do milheiro, CPM e riscos**, com a venda tratada como exceção arriscada.
- Fazer a "Planilha controle de pontos" pedir a **data da cotação** em cada célula de valor.
- **Tirar o produto do ar ou atualizá-lo de fato.** O produto já está fora de venda, mas segue listado no marketplace e indicado pela Mobills como opção de 2026.

---

## Tópicos cobertos (com nível)

Fonte: grade oficial e amostras do blog. ✓ = está na grade. (blog) = só aparece nos posts do autor, não na grade.

| Tópico normalizado | Nível | Fonte |
|---|---|---|
| Conceitos: milhas × pontos, banco × programa × companhia aérea | Básico | ✓ aulas 2–3 |
| Programas brasileiros (Smiles, LATAM Pass, Azul) e bancários (Livelo, Esfera, Itaú) | Básico | ✓ aulas 4–6 |
| Escolha de programa | Básico | ✓ aula 5 |
| Gerenciamento e controle de saldos (apps e planilha), expiração | Básico | ✓ aulas 7, 21 |
| Transferência de pontos / transferência bonificada (Livelo) | Básico → Intermediário | ✓ aulas 4, 8 |
| Escolha de cartão de crédito (pontos por real/dólar, anuidade, isenção) | Básico | ✓ aula 9 |
| Clubes de assinatura | Intermediário | ✓ aulas 4, 10 |
| Compra bonificada / shopping de parceiros (pontos por real) | Intermediário | ✓ aula 11 |
| Acúmulo com app de transporte, hotéis, locadoras, combustível | Básico | ✓ aulas 12–15 |
| Compra de pontos (lotes e promoções) | Intermediário | ✓ aula 16 |
| Reativação de milhas expiradas | Básico | ✓ aula 17 |
| Resgate de passagens / uso de pontos (genérico) | Básico | ✓ aula 18 |
| Venda de milhas | Intermediário | ✓ aula 19 |
| Valor do milheiro / pontos × dinheiro (CPM simplificado) | Intermediário | ✓ aula 20 |
| "Desconto equivalente" em produtos com pontos extras | Intermediário | (blog) e bônus da landing |
| Pagamento de boletos com cartão para pontuar | Básico | (blog) |
| Benefícios de cartão: salas VIP (LoungeKey), seguro viagem, proteção de preço | Básico | (blog) |
| Upgrade de cabine LATAM | Intermediário | (blog) |
| **Não cobertos (pela ementa):** tabela fixa × dinâmica, stopover, programas internacionais/alianças, limite de CPF/beneficiários, IR sobre venda, segurança da conta, risco de contraparte, hotéis como resgate | n/a | n/a |

---

## Vídeos gratuitos do autor

O canal do autor (`youtube.com/indavoula`, hoje **"Enjoy Mundo"**, @EnjoyMundo, 632 inscritos, 36 vídeos) é sobretudo de viagem: volta ao mundo, Indonésia, Nova Zelândia, Lençóis Maranhenses. Encontrei **só 2 vídeos sobre milhas**, ambos de março de 2020 e ligados ao "Desafio Bê-a-Bá das Milhas". **Não assisti aos vídeos.** A avaliação abaixo se baseia em título, descrição, duração e data.

| # | Título | Canal | URL | Crivo do Valério |
|---|---|---|---|---|
| 1 | Quantas passagens aéreas podem render os meus boletos? (37 min 34 s, 68 views, 09/03/2020) | Enjoy Mundo (ex-Inda Vou Lá) | https://www.youtube.com/watch?v=sSTW-IkbY2w | **Não passa.** A estratégia (apps de boleto sem taxa) mudou várias vezes desde 2020. A ideia geral de pontuar contas no cartão pode ser coberta por material mais recente. |
| 2 | A promoção bumerangue Latam Pass e Livelo Vale a Pena? (17 min 55 s, 145 views, 04/03/2020) | Enjoy Mundo (ex-Inda Vou Lá) | https://www.youtube.com/watch?v=UP2CZQ6dHnM | **Não passa.** Analisa uma promoção específica de 2020. A descrição é de captação para o Desafio pago, com formulário de "avaliação de perfil". O conceito "calcular se uma promoção vale a pena" é útil, mas o caso está datado. |

Não há vídeos gratuitos do autor aproveitáveis para a nossa trilha.

---

## Limitações desta análise

- **Nenhuma aula paga foi vista.** O produto está com `salesEnabled: false`, e eu não compraria nem criaria conta de qualquer forma. A auditoria do conteúdo usa a grade oficial mais 8 posts do mesmo autor (2020–2023) como amostra. Pode ser que as aulas tenham nuances ou ressalvas que os posts não têm.
- **Preço:** o único preço encontrado é o da landing de 2022 (R$ 297, "de R$ 497"). O checkout da Hotmart não mostrou valor.
- **Durações:** a Hotmart não divulga a duração das aulas, e a landing diz que não há duração estimada.
- **Avaliações:** a Hotmart não mostra nenhuma (`reviews: []`, `totalUsers: 0`). A Mobills também não encontrou. A landing tinha uma seção "Quem já aprendeu com a gente", mas os depoimentos (provavelmente imagens ou vídeos) não vieram no HTML.
- **Instagram @indavoula:** só consegui ver os dados do perfil, sem os posts. Hoje o perfil é assinado por Renata Marques e foca em viagem. Não achei Instagram de milhas próprio do José Panda.
- **Vídeos do YouTube:** avaliados por metadados e descrição, sem assistir.
- **Fatos de mercado de 2023–2026** citados como contraponto (recuperação judicial do grupo 123milhas/MaxMilhas, fim do iupp, rebranding para Azul Fidelidade, Chapter 11 de Azul e Gol, preço dinâmico) vêm do meu conhecimento de mercado, não de fontes abertas nesta sessão. A situação atual de cartões específicos (Pão de Açúcar Itaucard, Amex Bradesco) e de preços de clubes **não foi verificada** e fica marcada como "reverificar".
- **"7 anos na Hotmart" (Mobills):** pelos dados da própria Hotmart, o produto atual foi criado em 14/01/2022. O número da Mobills pode estar contando o Desafio de 2020 ou a conta do autor, que existe desde 2015.
