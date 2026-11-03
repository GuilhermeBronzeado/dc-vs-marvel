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
