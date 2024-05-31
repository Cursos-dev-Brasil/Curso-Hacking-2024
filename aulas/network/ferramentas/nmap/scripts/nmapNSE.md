# Nmap Scripting Engine (NSE)

O **NSE é uma adição do nmap**, ampliando sua funcionalidade. Os **scripts são escritos na linguagem de programação Brasileira *Lua*** e **podem ser usados para muitas coisas**, **de varredura de vulnerabilidades até automação da exploração dessas vulnerabilidades**. O NSE é especialmente **útil para reconhecimento**, mas vale mencionar o tamanho do sistema (604 scripts e 139 bibliotecas atualmente)

**Existem algumas categorias dentro da NSE**, as principais são:

- safe: não afetam o alvo
- intrusive: provavelmente vai afetar o alvo
- vuln: varredura de vulnerabilidade
- exploit: tentativa de exploração de vulnerabilidade
- auth: Tentativa de contornar autenticação para serviços em execução (por exemplo fazer login anonimamente em um servidor FTP)
- brute: Tentativa de ataque Brute force para credenciais em serviços em execução
- discovery: tentativa de consulta de serviços em execução para mais informações (Por exemplo consultar um server SNMP)

## Usando NSE

Você pode **executar todos os scripts de uma categoria** usando --script=<categoria>

**nota: só vão ser ativados scripts de serviços em execução**

Para executar scripts especificos, usamos --script=<nome_do_script>. Por exemplo: `script=http-fileupload-exploiter`.

você pode **executar mais de um script de uma vez** separando os nomes por ","

Alguns **scripts precisam de argumentos** (por exemplo, credenciais, se estiver explorando uma vulnerabilidade autenticada). Argumentos podem ser **fornecidos com a opção --script-args**. Um exemplo  seria com http-put (usado para fazer upload de arquivos usando PUT). Ele requer dois argumentos: a URL para o upload e a localização do arquivo.

`nmap -p 80 --script http-put --script-args http-put.url='/shell.php',http-put.file='./shell.php'`

**obs: argumentos são separados por "," e conectados ao script com pontos, ou seja <nome>.<args>**

[link da documentação oficial do NSE](https://nmap.org/nsedoc/)

**scripts Nmap vêm com menus de ajuda**, que **podem ser acessados no nmap** --script-help <nome-do-script>. Isso **tende a não ser extenso quanto no link**, mas, pode ser útil quando se trabalha localmente

## Encontrar scripts NSE

Sabemos usar os scripts, mas como podemos encontrar eles?

Temos duas opções, que **devem ser usadas em conjunto**. A primeira é a **página do site do Nmap que contém uma lista de todos os scripts**. A segunda é o **armazenamento local na máquina de ataque.** O Nmap **armazena seus scripts** no *Linux* **em /usr/share/nmap/scripts.** Todos os **scripts NSE são armazenados nesse diretório** por padrão - é lá que o Nmap procura por scripts quando você os especifica.

Existem **duas maneiras de procurar scripts**. Uma é **usando o arquivo /usr/share/nmap/scripts/script.db** Apesar da extensão, isso **não é realmente um banco de dados**, **mas um arquivo de texto formatado** contendo **nomes de arquivos e categorias** para cada script disponível.

podemos usar o grep para procurar scripts

`grep "ftp" /usr/share/nmap/scripts/script.db`

A segunda maneira é usando ls, por exemplo, podemos conseguir o mesmo resultado do exemplo acima com: 

`ls -l /usr/share/nmap/scripts/*ftp*`

**Note que eu usei um asterisco no começo e final da palavra ftp**

Mencionei que a página do site do Nmap tem uma lista de scripts, então, o que acontece se um deles estiver faltando no diretório local? Um comando sudo apt update && sudo apt install nmap deve corrigir isso, mas, é possível instalar os scripts manualmente baixando o script do Nmap:

`sudo wget -O /usr/share/nmap/scripts/<nome-do-script>.nse https://svn.nmap.org/nmap/scripts/<nome-do-script>.nse`

seguido por:

`nmap --script-updatedb`

Vale notar que você precisaria do mesmo comando "updatedb" se fosse criar seu script NSE e adicioná-lo ao Nmap - uma tarefa mais do que gerenciável com algum conhecimento básico de Lua


