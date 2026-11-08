# DC x Marvel: vendas de HQs

> Autora: **Gabriely Medeiros Amorim** · [← voltar ao README principal](../README.md)

Esta é a parte de **HQs** do projeto *DC vs Marvel*. Ela cobre a coleta e a preparação dos dados de vendas mensais de quadrinhos.

---

## 1. Sobre o conjunto de dados

Os dados cobrem o **ranking mensal de vendas de quadrinhos entre janeiro de 1997 e dezembro de 2019**: 23 anos, 276 meses. Cada linha representa um título que apareceu no ranking dos mais vendidos daquele mês, com posição, título, edição, preço de capa e editora.

| Arquivo | Linhas | Conteúdo |
|---|---|---|
| `data/raw/total_comics_1997_2019.csv` | 90.833 | Ranking completo, com **todas as editoras** |
| `data/processed/marvel_dc_1997_2019.csv` | **45.841** | Só Marvel (22.443) e DC (23.398) |

**Por que 1997–2019?** Antes de 1997, o formato das tabelas do site muda várias vezes, o que quebra o parser. A partir de 2020, o site passa a publicar num formato completamente diferente.

## 2. Processo de coleta

**Fonte:** [ComicChron](https://www.comichron.com/monthlycomicssales/), que publica rankings mensais baseados em dados do mercado direto (vendas para as lojas especializadas de quadrinhos, as *comic shops*).

A coleta foi feita por web scraping no notebook `01_coleta_hqs.ipynb`, com as funções auxiliares de `src/coletaComics.py`:

- `requests` baixa a página HTML de cada mês;
- `BeautifulSoup` extrai as tabelas;
- `pandas` junta tudo num CSV único.

O script percorre os 276 meses, com uma requisição por mês e uma pausa de 1 segundo entre elas (`time.sleep(1)`) para não sobrecarregar o servidor.

Detalhes do parser:
- **Colunas lidas pelo nome, não pela posição.** A ordem e a presença das colunas mudam ao longo do período, então o cabeçalho de cada tabela é lido dinamicamente.
- **Tabelas sem a coluna "Issue" são descartadas.** Isso exclui tabelas das páginas que não fazem parte do ranking.
- **O rank vem da posição da linha na tabela**, porque o HTML não tem uma coluna de rank explícita em todas as épocas.

## 3. Limpeza

Feita no `02_limpeza_hqs.ipynb`:

1. Remove espaços extras no nome da editora.
2. Mantém só as linhas com editora `Marvel` ou `DC`.
3. **O rank original é mantido.** Ele continua sendo a posição entre **todas** as editoras, e não um ranking só de Marvel e DC.
4. Os nomes das colunas passam para minúsculas, no padrão do projeto.

## 4. Dicionário de dados

Arquivo: `data/processed/marvel_dc_1997_2019.csv`

| Coluna | Tipo | Descrição | Exemplo |
|---|---|---|---|
| `ano` | inteiro | Ano do ranking (1997 a 2019) | `1997` |
| `mes` | inteiro | Mês do ranking (1 a 12) | `1` |
| `rank` | inteiro | Posição do título no ranking do mês, entre **todas** as editoras. O ranking tem cerca de 300 posições por mês | `1` |
| `titulo` | texto | Nome da revista | `X-Men` |
| `edicao` | texto | Número da edição. Vazio em 716 linhas | `62` |
| `preco` | decimal (US$) | Preço de capa em dólares. Vazio em 22 linhas, principalmente em edições antigas | `1.95` |
| `editora` | texto | `Marvel` ou `DC` | `Marvel` |

## 5. Limitações

1. **Só o mercado direto.** Os números do ComicChron representam vendas para as *comic shops*. Ficam de fora as vendas em bancas, livrarias e no formato digital.
2. **O tamanho do ranking varia.** A maioria dos meses tem cerca de 300 posições, mas alguns anos chegam a mais de 500. Por isso, comparar a posição de um título entre meses diferentes exige cuidado.
3. **Preços sem correção da inflação.** Um preço de 1997 e um de 2019 estão em dólares nominais.
4. **Período fixo.** Os dados param em 2019 por causa da mudança de formato do site (ver seção 1).

## 6. Como reproduzir

1. Na raiz do repositório, instale as dependências: `pip install -r requirements.txt`
2. Rode os notebooks de dentro da pasta `notebooks/`, em ordem: `01_coleta_hqs.ipynb` e depois `02_limpeza_hqs.ipynb`.

> O `01_coleta_hqs.ipynb` faz 276 requisições (cerca de 5 minutos) e **sobrescreve** o arquivo bruto. Para reproduzir exatamente esta base, rode só o `02_limpeza_hqs.ipynb`.
