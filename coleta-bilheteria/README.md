# DC x Marvel: bilheteria nos cinemas

Esta é a parte de **bilheteria** do projeto em grupo *Popularidade DC x Marvel: HQs, jogos e bilheteria*, feito para a disciplina de Introdução à Ciência de Dados. A entrega final é uma Análise Exploratória de Dados (EDA). Este README cobre a primeira etapa: a coleta e a preparação dos dados.

---

## 1. Sobre o conjunto de dados

O arquivo final, `data/processed/filmes_dc_marvel.csv`, reúne **120 filmes de cinema baseados em quadrinhos**: **78 da Marvel e 42 da DC**, lançados entre **1978 e 2026**. Cada linha é um filme. Há 18 colunas, com o desempenho financeiro (orçamento, bilheteria de estreia, na América do Norte, no resto do mundo e mundial, lucro e ROI) e a recepção do filme pela crítica especializada (Rotten Tomatoes e Metacritic) e pelo público (nota e número de votos no IMDb).

A ideia é comparar a popularidade das duas editoras no cinema por dois lados: **quanto dinheiro os filmes renderam** e **como foram recebidos**. Entram filmes live-action e animações lançadas nos cinemas (a coluna `formato` separa os dois).

**Sem recorte de anos.** Não há recorte de período: entram todos os filmes de cinema que têm os dados necessários para a análise. O limite é a disponibilidade de dados, e não a data de lançamento. No conjunto final, os filmes vão de 1978 a 2026 (DC: 1978–2026; Marvel: 1986–2025). Os critérios estão na [seção 5](#5-critérios-de-inclusão-e-exclusão).

## 2. Processo de coleta

**Datas da coleta:** tabelas da Wikipedia em 02/11/2026; OMDb em 25/10/2026.

A lista de filmes, a bilheteria, o orçamento e as notas da crítica vêm das páginas da Wikipedia em inglês [List of films based on Marvel Comics publications](https://en.wikipedia.org/wiki/List_of_films_based_on_Marvel_Comics_publications) e [List of films based on DC Comics publications](https://en.wikipedia.org/wiki/List_of_films_based_on_DC_Comics_publications). Usei uma fonte única para não ter filmes repetidos ou com títulos escritos de jeitos diferentes, e porque cada página já traz uma tabela de bilheteria, que cita o Box Office Mojo como fonte, e uma de crítica (Rotten Tomatoes e Metacritic). Fiz web scraping com `requests` e `pandas.read_html` no notebook `01_coleta.ipynb`. Não fiz scraping do Box Office Mojo, do Rotten Tomatoes nem do Metacritic diretamente, porque os termos de uso desses sites restringem a coleta automatizada.

A nota e o número de votos do público vêm do IMDb, pela [OMDb API](https://www.omdbapi.com/), consultada filme a filme pelo título e ano no `02_limpeza.ipynb`. A chave da API fica no arquivo `.env`, que não vai para o repositório. Os dados brutos das duas fontes ficam em `data/raw/`, sem limpeza, e a base final em `data/processed/` (ver seção 8).

## 3. Dicionário de dados

O exemplo usado em todas as linhas é o filme *Black Panther* (2018). Os valores em dinheiro estão em **dólares americanos (US$), sem correção da inflação**.

| Coluna | Tipo | Descrição | Exemplo |
|---|---|---|---|
| `titulo` | texto | Título original do filme (em inglês) | `Black Panther` |
| `ano` | inteiro | Ano de lançamento nos EUA | `2018` |
| `universo` | texto | Editora dos quadrinhos: `Marvel` ou `DC` | `Marvel` |
| `formato` | texto | `live-action` ou `animação` | `live-action` |
| `data_lancamento` | data (AAAA-MM-DD) | Data de lançamento nos cinemas dos EUA | `2018-02-16` |
| `distribuidora` | texto | Estúdio que distribuiu o filme. **Vazio em todos os filmes da DC** (ver limitações) | `Walt Disney Studios Motion Pictures` |
| `orcamento` | número (US$) | Orçamento de produção | `200000000` |
| `bilheteria_estreia` | número (US$) | Bilheteria do fim de semana de estreia na América do Norte (EUA e Canadá) | `202003951` |
| `bilheteria_america_norte` | número (US$) | Bilheteria total na América do Norte | `700059566` |
| `bilheteria_outros` | número (US$) | Bilheteria fora da América do Norte. **Na DC é calculada** (mundial − América do Norte). Vazia em 1 filme, *Supergirl* (1984), porque a fonte só tem a bilheteria da América do Norte (ver limitações) | `646853595` |
| `bilheteria_mundial` | número (US$) | Bilheteria total no mundo | `1346913161` |
| `lucro` | número (US$) | `bilheteria_mundial − orcamento` (lucro bruto aproximado, ver limitações) | `1146913161` |
| `roi` | número | Retorno sobre o investimento: `(bilheteria_mundial − orcamento) / orcamento`. Negativo = prejuízo | `5.73` |
| `rotten_tomatoes` | número (0–100) | % de críticas positivas no Rotten Tomatoes | `96` |
| `metacritic` | número (0–100) | Nota média da crítica no Metacritic | `88` |
| `nota_imdb` | número (0–10) | Nota média do público no IMDb | `7.3` |
| `votos_imdb` | inteiro | Número de votos no IMDb (indica alcance e popularidade) | `928979` |
| `imdb_id` | texto | Código do filme no IMDb, útil para juntar com outras bases | `tt1825683` |

## 4. Google Drive da turma

Os arquivos desta etapa estão no Drive da turma: **https://drive.google.com/drive/folders/1uBvs5oCj5a46YaxwvjYN_9kjNVaAx8Li**

## 5. Critérios de inclusão e exclusão

**Funil:** 131 filmes nas tabelas da Wikipedia (80 Marvel e 51 DC) → **123** depois das exclusões de escopo e de lançamentos recentes → **120** depois do critério de dados suficientes (78 Marvel e 42 DC).

### 5.1 O que entra

Só **filmes lançados nos cinemas**, live-action ou animação, de qualquer ano.

**Animações.** As animações lançadas nos cinemas entram porque algumas estão entre os filmes mais relevantes das editoras (ex: *Big Hero 6* e os dois *Aranhaverso*). A coluna `formato` (`live-action` / `animação`) permite fazer a análise com e sem elas. Há 7 animações na base final.

### 5.2 Exclusões de escopo

| Filme / grupo | Universo | Motivo | 
|---|---|---|
| Selos **Vertigo, WildStorm, Paradox Press e Mad** | DC | Selos secundários (ver abaixo) |
| Constantine (2005) | DC | Selo Vertigo |
| Inhumans (2017) | Marvel | Série de TV |
| Batman: The Killing Joke (2016) | DC | Animação lançada direto em vídeo |
| Batman: Return of the Caped Crusaders (2016) | DC | Animação lançada direto em vídeo |
| Batman and Harley Quinn (2017) | DC | Animação lançada direto em vídeo |
| Batman (1966) | DC | Erro na fonte |

**Selos secundários.** Os filmes de selos secundários ficam de fora porque o público não os identifica como filmes da Marvel ou da DC (ex: *V de Vingança*, do selo Vertigo, e *Men in Black*, do selo Malibu). Na DC, saíram os selos **Vertigo, WildStorm, Paradox Press e Mad**. Os selos da Marvel (**Icon e Malibu**) já não aparecem na página da Wikipedia.
- *Como foi feito:* na página da DC, os filmes desses selos ficam em tabelas separadas, e o código salva só a tabela principal. *Constantine* (Vertigo) é exceção: aparece na tabela principal e por isso foi excluído na mão.

**Série de TV.** *Inhumans* (2017) é uma série de TV e não tem bilheteria de cinema comparável, por isso foi excluída.

**Direto em vídeo.** Na tabela da Wikipedia, as três animações do Batman têm a nota *"From a limited theatrical release"*, não têm bilheteria de estreia e faturaram muito pouco na América do Norte: US$ 3,8 milhões (*The Killing Joke*), US$ 56,7 mil (*Return of the Caped Crusaders*) e US$ 6,4 mil (*Batman and Harley Quinn*). Esses números vêm de exibições limitadas, e não de um lançamento comercial, então não são comparáveis aos dos outros filmes.

**Batman (1966).** A Wikipedia registra uma bilheteria mundial de **US$ 3.315**, um valor impossível para um filme de estúdio, que indica um erro ou um dado incompleto na fonte. O filme foi excluído pelo título **e** pelo ano, para não tirar junto o *Batman* de 1989.

### 5.3 Bilheteria incompleta (filme ainda em cartaz)

Só entram filmes que **já saíram do cinema**, ou seja, com bilheteria completa. Um filme ainda em cartaz tem a bilheteria subestimada, e o lucro e o ROI ficariam errados.

Nenhuma das fontes informa quando um filme saiu de cartaz, então usei uma regra objetiva: o filme precisa ter estreado **pelo menos 120 dias (cerca de 4 meses) antes de 02/11/2026**, a data em que as tabelas da Wikipedia usadas foram baixadas. O prazo de 120 dias (cerca de 4 meses) é uma escolha deste projeto, e não um dado das fontes (ver limitações). Os valores ficam nas variáveis `DIAS_EM_CARTAZ` e `DATA_COLETA` da célula 3 do `02_limpeza.ipynb` e podem ser ajustados.

| Filme | Dias desde a estreia |
|---|---|
| Spider-Man: Brand New Day (2026, Marvel) | 94 |
| Clayface (2026, DC) | 10 |

Observação: *Supergirl* (2026) entrou por pouco, com 129 dias desde a estreia.

### 5.4 Dados suficientes

Para entrar na base final, o filme precisa ter **todos** estes dados:
- **bilheteria mundial** e **orçamento**, sem os quais não dá para calcular lucro e ROI;
- **nota do IMDb**, a opinião do público;
- **pelo menos uma nota de crítica** (Rotten Tomatoes ou Metacritic).

Na prática, a regra da crítica não tirou nenhum filme sozinha: os 120 filmes do conjunto final têm as duas notas, e o único filme sem crítica (*Aztec Batman*) já sairia por falta de orçamento.

Saíram **3 filmes, todos da DC**:

| Filme | O que falta |
|---|---|
| Swamp Thing (1982) | bilheteria mundial |
| The Return of Swamp Thing (1989) | orçamento |
| Aztec Batman: Clash of Empires (2025) | orçamento e crítica |

### 5.5 Orçamento em faixa

A Wikipedia informa o orçamento de alguns filmes como uma faixa (ex: "$75–83", em milhões). Como a análise precisa de um número só, usei **a média das duas pontas**, que é o valor central da faixa. Isso aconteceu em 2 filmes:

| Filme | Faixa na Wikipedia | Valor usado |
|---|---|---|
| Morbius (2022, Marvel) | US$ 75–83 mi | US$ 79 mi |
| The Batman (2022, DC) | US$ 185–200 mi | US$ 192,5 mi |

## 6. Conferências feitas

- **Junção bilheteria × crítica:** nenhum filme sumiu nem ficou duplicado. Títulos repetidos (Superman, Supergirl, Fantastic Four, The Punisher, Batman) foram separados pelo ano.
- **América do Norte + outros = mundial (Marvel):** todos os filmes batem, exceto *The Wolverine*, com uma diferença de US$ 5.892 (irrelevante).
- **Wikipedia × OMDb:** a bilheteria da América do Norte bate com a dos EUA na OMDb (diferença de até 5%) nos 120 filmes da base final.
- **Títulos da OMDb:** 6 filmes voltaram com um nome um pouco diferente (ex: *X2* → *X2: X-Men United*), e todos foram conferidos como o mesmo filme.

## 7. Limitações

1. **Lucro e ROI são aproximações.** Os dois consideram só o orçamento de produção e a bilheteria. Ficam de fora os gastos com marketing e a parte da bilheteria que fica com os cinemas. Na prática, o lucro real dos estúdios é menor.
2. **Valores sem correção da inflação.** Comparar um filme de 1978 com um de 2025 em dólar nominal favorece os filmes mais novos.
3. **Supergirl (1984):** a Wikipedia (e também o [The Numbers](https://www.the-numbers.com/movie/Supergirl-(1984))) só registra a bilheteria da América do Norte. Por isso `bilheteria_outros` ficou **vazia (NaN)**: o dado não existe, o que é diferente de zero. Assim, a `bilheteria_mundial`, o `lucro` e o `roi` desse filme estão **provavelmente subestimados**.
4. **`distribuidora` vazia na DC:** a tabela da Wikipedia da DC não tem essa coluna.
5. **`bilheteria_outros` da DC é calculada:** a tabela de bilheteria da DC não tem a coluna "Other territories" (a da Marvel tem), então o valor foi obtido por `bilheteria_mundial − bilheteria_america_norte`. Para a Marvel, o valor vem direto da fonte. Se o resultado der zero, ele fica vazio (ver item 3).
6. **Critério de 120 dias:** é uma aproximação de "já saiu do cinema", e não uma informação oficial. Um filme pode ficar em cartaz mais tempo, ou sair antes.
7. **Orçamentos em faixa:** usei a média das pontas em 2 filmes (ver seção 5.5).
8. **Os dados mudam com o tempo:** notas e votos do IMDb e valores da Wikipedia mudam. Os números valem para a data da coleta.

## 8. Estrutura das pastas

```
├── data/
│   ├── raw/                     # dados brutos, sem alteração
│   │   ├── marvel_bilheteria_wiki.csv
│   │   ├── marvel_criticas_wiki.csv
│   │   ├── dc_bilheteria_wiki.csv
│   │   ├── dc_criticas_wiki.csv
│   │   └── omdb.csv
│   └── processed/
│       └── filmes_dc_marvel.csv # base final (120 filmes, 18 colunas)
├── notebooks/
│   ├── 01_coleta.ipynb          # scraping da Wikipedia
│   └── 02_limpeza.ipynb         # limpeza, consulta à OMDb, junção e CSV final
├── requirements.txt
└── README.md
```

**Dados brutos x dados limpos.** `data/raw/` guarda os dados como vieram das fontes, sem limpeza: as tabelas da Wikipedia como o pandas as extraiu (a única mudança é que os cabeçalhos de duas linhas viraram uma) e as respostas da OMDb como a API devolveu. Os valores continuam com notas de rodapé, `$` e textos como "—N/a". `data/processed/` guarda só a versão limpa e final. O `02_limpeza.ipynb` só escreve em `data/raw/` para salvar o `omdb.csv`, que é o bruto da API, e só consulta a OMDb se esse arquivo ainda não existir (o limite da chave é de 1.000 consultas por dia). A limpeza em si nunca altera os arquivos brutos, então qualquer pessoa pode refazer todo o processo a partir deles (ver seção 9).

## 9. Como reproduzir

1. Instale as dependências: `pip install -r requirements.txt`
2. Crie um arquivo `.env` na raiz com a sua chave da OMDb: `OMDB_KEY=sua_chave` (é gratuita em [omdbapi.com](https://www.omdbapi.com/apikey.aspx)).
3. Rode os notebooks de dentro da pasta `notebooks/`, em ordem: `01_coleta.ipynb` e depois `02_limpeza.ipynb`.

> Rodar o `01_coleta.ipynb` de novo baixa a versão **atual** da Wikipedia e sobrescreve os dados brutos. Para reproduzir exatamente esta base, rode só o `02_limpeza.ipynb`, que usa os arquivos de `data/raw/`.
