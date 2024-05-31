# Falha de criptografia

Uma falha Criptográfica se refere a qualquer vulnerabilidade que remete a uso indevidoa (ou falta) de criptografia para proteger dados sensíveis. Uma aplicação web necessita de criptografia para garantir a confidencialidade de seus usuarios

Vamos usar o Gmail como um exemplo:

Quando você acessa sua conta gmail usando o navegador, quer ter certeza de que comunicações entre você e servidor estão criptografadas. assim, qualquer ladrão tentando pegar seus pacotes de rede não consegue recuperar o conteúdo dos emails Quando criptografamos o tráfego entre cliente e o servidor. Uma vez que os emails são armazenados em algum servidor gerenciado pelo provedor, você também precisa ter certeza que ninguém de dentro do provedor pode ler os emails de um clientes. Para isso, seus emails podem ser criptografados quando armazenados nos servidores. Isso é referido como criptografar dados em repouso. falhas criptográficas resultam em aplicativos web divulgando acidentalmente dados sensíveis. Isso geralmente são dados diretamente relacionados aos clientes (por exemplo, nomes, datas de nascimento, informações financeiras), mas também podem ser informações técnicas, como nomes de usuário e senhas.

Em níveis complexos, aproveitar falhas criptográficas envolve técnicas como Man in The Middle Attacks, em que o atacante força conexões do usuário por um dispositivo que eles controlam. depois, eles se aproveitariam da criptografia fraca em qualquer dado transmitido para acessar as informações (se os dados estiverem criptografados em primeiro lugar). Claro, muitos exemplos são muito mais simples, e vulnerabilidades podem ser encontradas em aplicativos web que podem ser exploradas sem conhecimento avançado de rede. De fato, em alguns casos, os dados podem ser encontrados diretamente no próprio servidor web.

A forma mais fácil de armazenar uma grande quantidade de dados em um formato acessível é usando um banco de dados, e isso é perfeito para aplicações web, já que permite o usuário acessar seu perfil em qualquer lugar, normalmente motores de banco de dados seguem a sintaxe da Structured Query Language (SQL)

Em um ambiente de produção é comum ver banco de dados configurados em servidores dedicados  executando serviços como MySQL, um banco de dados também pode rodar em um arquivo, esse tipo de banco de dados é conhecido como flat-file, por que são armazenados em um arquivo. Isso é muito mais fácil de configurar do que um servidor dedicado completo e pode funcionar em aplicativos web menores

Um banco de dados flat-file pode ser acessado diretamente pelo PC em que está sendo executado, isso não seria um problema  problema no aplicativo web, mas e se o banco de dados estiver na raiz do projeto? (ou seja, acessivel para qualquer usuário) nesse caso, você pode baixar o banco de dados na sua máquina e ter acesso total a 100% dos dados

O formato mais comum é mais simples para um DB flat-file é no formato de Sqlite, esse tipo de banco de dados suporta a maioria das linguagens de programação e possuem um cliente dedicado para consultá-lo na CLI

Vamos supor que você conseguiu baixar o banco de dados, agora você pode executá-lo e examiná-lo
```
user@linux$ ls -l 
-rw-r--r-- 1 user user 8192 Feb  2 20:33 example.db

user@linux$ file example.db 
example.db: SQLite 3.x database, last written using SQLite version 3039002, file counter 1, database pages 2, cookie 0x1, schema 4, UTF-8, version-valid-for 1
```

Podemos ver que tem um banco de dados SQLite na pasta, agora podemos executá-lo:

```sql
user@linux$ sqlite3 example.db                     
SQLite version 3.39.2 2022-07-21 15:24:47
Enter ".help" for usage hints.
sqlite> 
```