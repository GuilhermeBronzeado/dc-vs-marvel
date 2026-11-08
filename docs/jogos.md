# DC x Marvel: jogos

> Autor: **Guilherme de Andrade Bronzeado** · [← voltar ao README principal](../README.md)

Esta é a parte de **jogos** do projeto *DC vs Marvel*. Ela cobre a coleta e a preparação da lista de jogos baseados nas duas editoras.

---

## 1. Sobre o conjunto de dados

O arquivo final, `data/processed/jogos_dc_marvel.csv`, reúne **292 jogos**: **175 da Marvel e 117 da DC**, com lançamentos entre 1979 e 2027 (alguns já anunciados e ainda não lançados). Cada linha é um jogo, com título, ano, plataformas, publicadora e universo.

**Esta base é uma referência.** Ela serve de lista base para buscar informações em outras fontes (principalmente IGDB, VGChartz e rawg.io). Esses bancos de dados não têm uma busca que permita filtrar só os jogos relevantes para o projeto, então a lista da Wikipedia indica quais jogos procurar.

## 2. Processo de coleta

**Fontes:**
- Marvel: [Marvel Games](https://pt.wikipedia.org/wiki/Marvel_Games) (Wikipedia em português)
- DC: [List of video games based on DC Comics](https://en.wikipedia.org/wiki/List_of_video_games_based_on_DC_Comics) (Wikipedia em inglês)

**Data da coleta:** 03/11/2026.

A coleta foi feita por web scraping no notebook `01_coleta_jogos.ipynb`:

- `requests` baixa as páginas da Wikipedia;
- `BeautifulSoup` extrai o HTML e localiza as tabelas;
- `pandas` lê as tabelas e monta o DataFrame.

Cada página tem uma tabela por década. O script percorre todas as tabelas, registra de qual seção cada linha veio (`secao_wikipedia`) e gera **um CSV bruto por página**: `wikipedia_jogos_marvel.csv` e `wikipedia_jogos_dc.csv`.

## 3. Limpeza

Feita no `02_limpeza_jogos.ipynb`:

1. Padroniza os nomes das colunas das duas páginas (uma está em português e a outra em inglês).
2. Mantém só as colunas presentes nos dois arquivos e cria a coluna `universo` (`Marvel` ou `DC`).
3. Junta as duas bases.
4. Remove as notas de rodapé da Wikipedia (ex.: `[1]`) e os espaços extras.
5. Confere se há duplicatas. Há 47 linhas com títulos repetidos, mas nenhuma duplicata real: são jogos diferentes com o mesmo nome (ver limitações).
6. Remove as linhas vazias, coletadas por engano, e os jogos sem ano definido (`TBA`, `Upcoming`, `Ainda não lançado`).
7. Cria a coluna `ano_lancamento`, com o primeiro ano de quatro dígitos encontrado na coluna `ano`.

Os CSVs brutos foram mantidos em `data/raw/` porque têm informações que não entraram na base final e podem ser úteis na análise (ex.: a coluna *Propriedades* da página da Marvel).

## 4. Dicionário de dados

Arquivo: `data/processed/jogos_dc_marvel.csv`

| Coluna | Tipo | Descrição | Exemplo |
|---|---|---|---|
| `titulo` | texto | Nome do jogo | `Superman` |
| `ano` | texto | Ano(s) de lançamento como aparece na Wikipedia. Pode ter mais de um ano quando o jogo saiu em datas diferentes | `2011, 2013` |
| `ano_lancamento` | inteiro | Primeiro ano de lançamento. **É a coluna indicada para a análise** | `2011` |
| `plataformas` | texto | Plataformas do lançamento original. Vazio em 1 jogo | `PS5, PS4` |
| `publicadoras` | texto | Empresa(s) que publicaram o jogo. Vazio em 2 jogos | `Atari` |
| `universo` | texto | `Marvel` ou `DC` | `DC` |
| `secao_wikipedia` | texto | Seção (década) da página de onde a linha foi tirada. Os nomes vêm como estão em cada página: em inglês na DC (`1990s`) e em português na Marvel (`década de 1990`) | `1990s` |
| `url_fonte` | texto | Endereço da página da Wikipedia de origem | `https://en.wikipedia.org/...` |
| `data_coleta` | texto (AAAA-MM-DD) | Dia em que a página foi baixada | `2026-11-03` |

## 5. Limitações

1. **Critérios diferentes entre as páginas.** A Wikipedia é a única fonte encontrada que separa os jogos por editora, mas as duas páginas usam critérios diferentes. Por isso aparecem alguns jogos que não são do universo de super-heróis. Exemplo: *Men in Black*, que é propriedade da Marvel, está na base.
2. **Não são todos os jogos.** As páginas listam os títulos mais relevantes de cada época e deixam de fora jogos menores.
3. **Títulos repetidos.** Jogos diferentes podem ter o mesmo nome. Existem, por exemplo, 7 jogos chamados *Batman*, com anos, publicadoras e plataformas diferentes. Para identificar um jogo, use o título **e** o ano.
4. **Jogos ainda não lançados.** Há 7 jogos com lançamento previsto para 2026 ou 2027, que podem não ter dados de vendas ou notas.
5. **Ainda sem dados de vendas ou popularidade.** A base atual é só a lista de jogos. Os dados de vendas e notas vão vir das próximas etapas (IGDB, VGChartz, rawg.io).

## 6. Como reproduzir

1. Na raiz do repositório, instale as dependências: `pip install -r requirements.txt`
2. No `01_coleta_jogos.ipynb`, coloque o seu e-mail no campo indicado. Ele vai no cabeçalho `User-Agent`, como a Wikipedia pede para coletas automatizadas.
3. Rode os notebooks de dentro da pasta `notebooks/`, em ordem: `01_coleta_jogos.ipynb` e depois `02_limpeza_jogos.ipynb`.

> Rodar o `01_coleta_jogos.ipynb` de novo baixa a versão **atual** da Wikipedia e sobrescreve os dados brutos. Para reproduzir exatamente esta base, rode só o `02_limpeza_jogos.ipynb`.
