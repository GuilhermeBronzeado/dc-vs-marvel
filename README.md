# DC vs Marvel: quem vende mais?

Projeto da disciplina **Introdução à Ciência de Dados**, UFPB, turma 2026.2.

## Objetivo

> **Qual editora, Marvel ou DC, vende mais e é mais popular em cada mídia: HQs, jogos e cinema?**

Para responder, o grupo coletou e preparou três bases de dados, uma para cada mídia. A entrega final é uma Análise Exploratória de Dados (EDA), apresentada em sala. Este repositório documenta o **processo**: de onde vieram os dados, como foram coletados e limpos, e como reproduzir tudo.

## Integrantes

| Nome | Responsável por |
|---|---|
| Gabriely Medeiros Amorim | HQs |
| Guilherme de Andrade Bronzeado | Jogos |
| Sofia Lima | Filmes |
| Claudio Junior | README e organização do repositório |

## Bases de dados

| Base | Arquivo final | Linhas | Período | Fonte | Documentação |
|---|---|---|---|---|---|
| HQs | `data/processed/marvel_dc_1997_2019.csv` | 45.841 | 1997–2019 | [ComicChron](https://www.comichron.com/monthlycomicssales/) | [docs/hqs.md](docs/hqs.md) |
| Jogos | `data/processed/jogos_dc_marvel.csv` | 292 | 1979–2027 | Wikipedia | [docs/jogos.md](docs/jogos.md) |
| Filmes | `data/processed/filmes_dc_marvel.csv` | 120 | 1978–2026 | Wikipedia + OMDb (IMDb) | [docs/filmes.md](docs/filmes.md) |

### HQs
Ranking mensal dos quadrinhos mais vendidos nas lojas especializadas dos EUA, filtrado para Marvel (22.443 linhas) e DC (23.398 linhas). Cada linha é um título que entrou no ranking de um mês, com posição, edição, preço e editora. → [documentação completa](docs/hqs.md)

### Jogos
Lista de jogos baseados nas duas editoras: 175 da Marvel e 117 da DC. Por enquanto a base tem título, ano, plataformas e publicadora. Ela serve de referência para buscar vendas e notas em outras fontes (IGDB, VGChartz, rawg.io). → [documentação completa](docs/jogos.md)

### Filmes
Filmes de cinema baseados nas duas editoras: 78 da Marvel e 42 da DC. Para cada filme, a base traz bilheteria, orçamento, lucro, ROI, notas da crítica (Rotten Tomatoes e Metacritic) e do público (IMDb). → [documentação completa](docs/filmes.md)

### Padrão das colunas
Em todas as bases, os nomes das colunas estão **em minúsculas, sem acento e com `_`** (ex.: `ano`, `editora`, `bilheteria_mundial`). A editora aparece como `Marvel` ou `DC`, na coluna `editora` (HQs) ou `universo` (jogos e filmes).

## Estrutura de pastas

```
dc-vs-marvel/
├── data/
│   ├── raw/                            # dados brutos, como vieram das fontes (nunca editar à mão)
│   │   ├── total_comics_1997_2019.csv      # HQs
│   │   ├── wikipedia_jogos_dc.csv          # jogos
│   │   ├── wikipedia_jogos_marvel.csv      # jogos
│   │   ├── dc_bilheteria_wiki.csv          # filmes
│   │   ├── dc_criticas_wiki.csv            # filmes
│   │   ├── marvel_bilheteria_wiki.csv      # filmes
│   │   ├── marvel_criticas_wiki.csv        # filmes
│   │   └── omdb.csv                        # filmes (respostas da API OMDb)
│   └── processed/                      # bases finais, limpas, usadas na análise
│       ├── marvel_dc_1997_2019.csv
│       ├── jogos_dc_marvel.csv
│       └── filmes_dc_marvel.csv
├── notebooks/                          # 01_ = coleta, 02_ = limpeza
│   ├── 01_coleta_hqs.ipynb
│   ├── 02_limpeza_hqs.ipynb
│   ├── 01_coleta_jogos.ipynb
│   ├── 02_limpeza_jogos.ipynb
│   ├── 01_coleta_filmes.ipynb
│   └── 02_limpeza_filmes.ipynb
├── src/
│   └── coletaComics.py                 # funções auxiliares da coleta de HQs
├── docs/                               # documentação detalhada de cada base
│   ├── hqs.md
│   ├── jogos.md
│   └── filmes.md
├── requirements.txt
└── README.md
```

**Dados brutos x dados limpos.** `data/raw/` guarda os dados exatamente como vieram das fontes. Os notebooks de limpeza leem o bruto e gravam o resultado em `data/processed/`, sem alterar o bruto. Assim, qualquer pessoa pode refazer a limpeza do zero.

## Como reproduzir

1. Clone o repositório e instale as dependências (Python 3.11 ou mais novo):
   ```bash
   pip install -r requirements.txt
   ```
2. **Só para filmes:** crie um arquivo `.env` na raiz do repositório com a sua chave da OMDb: `OMDB_KEY=sua_chave` (é gratuita em [omdbapi.com](https://www.omdbapi.com/apikey.aspx)). O `.env` não vai para o GitHub.
3. Abra o Jupyter e rode os notebooks **de dentro da pasta `notebooks/`**. Todos os caminhos são relativos a ela (`../data/...`).
4. Para cada base, rode primeiro o `01_coleta_*` e depois o `02_limpeza_*`.

> ⚠️ **Os notebooks `01_coleta_*` baixam os dados de novo da internet e sobrescrevem `data/raw/`.** Como os sites mudam, os números podem sair diferentes dos deste repositório. Para reproduzir exatamente as bases daqui, rode **só os notebooks `02_limpeza_*`**.

## Links

- 📁 [Google Drive da turma](https://drive.google.com/drive/folders/1uBvs5oCj5a46YaxwvjYN_9kjNVaAx8Li)
- Fontes: [ComicChron](https://www.comichron.com/monthlycomicssales/) · [Marvel Games (Wikipedia)](https://pt.wikipedia.org/wiki/Marvel_Games) · [Video games based on DC Comics (Wikipedia)](https://en.wikipedia.org/wiki/List_of_video_games_based_on_DC_Comics) · [Films based on Marvel Comics (Wikipedia)](https://en.wikipedia.org/wiki/List_of_films_based_on_Marvel_Comics_publications) · [Films based on DC Comics (Wikipedia)](https://en.wikipedia.org/wiki/List_of_films_based_on_DC_Comics_publications) · [OMDb API](https://www.omdbapi.com/)

## Como o grupo trabalha no Git

Para ninguém sobrescrever o trabalho de outra pessoa:

1. **Nunca trabalhe direto na `main`.** Crie uma branch para a sua tarefa:
   ```bash
   git checkout main
   git pull
   git checkout -b nome-da-tarefa      # ex.: vendas-jogos
   ```
2. Faça as alterações e salve no Git:
   ```bash
   git add arquivo1 arquivo2
   git commit -m "Descreve o que mudou"
   git push -u origin nome-da-tarefa
   ```
3. No GitHub, abra um **Pull Request** da sua branch para a `main`. Alguém do grupo revisa e faz o merge.
4. **Cada um mexe nos seus arquivos.** O README principal é mantido por Claudio. Se quiser mudar algo nele, avise ou abra um Pull Request.
