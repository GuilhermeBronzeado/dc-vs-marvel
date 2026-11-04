# dc-vs-marvel
Projeto da matéria Introdução da ciência de Dados da UFPB, turma 2026.2

COMICS

Explicação do conjunto de dados:
Os dados das comics cobrem o ranking mensal de vendas entre janeiro de 1997 e dezembro de 2019, ou seja, 23 anos, 276 meses, 90.833 registros no total. Cada linha representa um título que apareceu no ranking de mais vendidos daquele mês, com posição, título, edição, preço de capa e editora. A fonte é o site ComicChron (https://www.comichron.com/monthlycomicssales/), que publica rankings mensais baseados em dados do mercado direto de comic shops. A base original cobre todas as editoras do ranking, não só Marvel e DC. O período foi recortado em 1997–2019 porque antes de 1997 o formato das tabelas do site muda várias vezes, quebrando o parser, e a partir de 2020 o site passa a publicar um formato completamente diferente.

Como os dados foram coletados:
A coleta foi realizado scraping, feita com um script Python em notebook, usando requests para baixar as páginas HTML de cada mês, BeautifulSoup para extrair as tabelas e pandas para consolidar tudo num CSV único. O script percorre os 276 meses de janeiro de 1997 a dezembro de 2019, um request por mês, com time.sleep(1) entre eles para não sobrecarregar o servidor. Cada página tem uma tabela HTML com o ranking daquele mês; o parser lê o cabeçalho da tabela dinamicamente (procurando as colunas por nome, não por posição) porque a ordem e a presença de colunas mudam ao longo do período, e descarta tabelas que não têm coluna Issue, o que exclui tabelas não relacionadas presentes nas páginas. O Rank é gerado pela posição da linha na tabela, já que o HTML não expõe uma coluna de rank explícita em todas as épocas.

Dicionário de dados
Ano: Numero inteiro de 1997 a 2029;
Mês: Numero inteiro de 1 a 12;
Rank inteiro: Numero inteiro que representa a posição do título no ranking mensal, entre todas as editoras, de 1 a 300 na média;
Titulo: texto que contem o nome da HQ, ex: death in family;
Edicao: texto que contem o numero da edição, ex: 35;
Preço: numero decimal que representa o preço de capa em dólares (pode ser vazio em edições antigas), ex: 7.85;
Editora: texto que contem a editora que publicou o título, ex: DC.

COMICS

JOGOS

Explicação do conjunto de dados atual:
O conjunto de dados cobre apenas os principais títulos da Marvel e DC coletados das fontes: https://pt.wikipedia.org/wiki/Marvel_Games, e https://en.wikipedia.org/wiki/List_of_video_games_based_on_DC_Comics. A base atual tem o objetivo de apenas servir como referência para realizar a extração das informações de outras fontes (principais: IGBD, VGchartz, rawg.io), uma vez que esses bancos de dados não possuem ferramentas de pesquisas que permitem filtrar apenas as informações relevantes para o projeto. Os arquivos possuem informações sobre: nome, publicadora, desenvolvedora, universo pertencente, data de lançamento e outras informações relacionadas à extração. 
 Limitações: As páginas da wikipedia foram as únicas fontes disponíveis com os jogos separados por marca (Marvel e DC), e o critério de seleção delas diverge, causando a listagem de alguns poucos jogos que se diferenciam da classificação de personagens do universo Marvel (Exemplo: O jogo Man In Black é propriedade da Marvel, e está presente nos dados). Os arquivos não possuem todos os jogos existentes relacionados as marcas, eles cobrem apenas os títulos mais relevantes de acordo com a sua época, deixando de fora jogos de menor escopo. Alguns jogos possuem o mesmo nome, porém com anos de lançamento, publicadora, desenvolvadora, e plataformas diferentes (Ex: Existem 7 jogos com o mesmo título "Batman" e anos de lançamentos próximos, porém classificam-se como jogos diferentes)

 Como os dados foram coletados: 
 A coleta foi feita com scrapping, através de um script Python em notebook, usando requests para poder baixar as páaginas da wikipedia, BeautifulSoup foi utilizado para extrair o htlm e filtrar as tabelas, pandas foi essencial para ler o html das tabelas e montar o dataframe, e posteriormente formata-lo em csv. O script percorre todas as 5 tabelas de cada site (cada uma representando uma década), determina as colunas e armazenas as linhas, formando dois csv's distintos para cada site (Um da Marvel e outro da DC). Após isso um script, também em um notebook python, de tratamento foi realizado com o intúito de juntar os csv's em um só, primeiro padronizando o nome das colunas e selecionando apenas as relevantes e presentes em ambos os arquivos e criando colunas de classificação, como "universo", depois carregamento das linhas dos dois arquivos, isso transformando-os em data frame e por fim formatando o arquivo final em csv. (Os arquivos csv brutos foram mantidos pois possuem informações individuais que podem ser úteis na análise dos dados, Ex: coluna Propriedades).

 Dicionário de dados:
 
titulo: String (Nome do jogo)
ano: String (Anos de publicação de um jogo Ex: 2011, 2013 no caso do mesmo jogo ter publicações diferentes)
plataformas: String (Plataformas em que o jogo foi lançado originalmente Ex: PS5, PS4)
publicadora(s): String (Ex: Sony Interactive Entertainment)
universo: srt (Diferencia-los em Marvel e DC)
secao_wikipedia: str (De qual tabela foram retirados os dado)
url_fonte: str (Página da wikipedia a qual os dados pertencem)
data_coleta: str (Ex: 2026-11-03)
ano_lancamento: Int64 (Ex: 2011) (Ano do primeiro lançamento daquela versão do jogo)

JOGOS
