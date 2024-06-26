# Fundamentos linux parte 3 

Até agora você sabe adicionar conteúdo a um arquivo com `echo "conteúdo" > arquivo.txt`, mas esse método é horrível, principalmente quando você precisa colar várias linhas ou outros tipos de dados

## editores de texto de terminal

Existem opções, nesse curso, o foco vai ser sempre o *nano*

### Nano

É fácil começar com o Nano. Para editar um arquivo com nano usamos `nano nome_do_arquivo`

Interface nano:
```
root@linux3:/tmp# nano arquivo
  GNU nano 4.8                                             meu_arquivo                                                       

^G Obter Ajuda    ^O Escrever    ^W Onde Está    ^K Cortar Texto    ^J Justificar     ^C Posição Atual     M-U Desfazer       M-A Marcar Texto
^X Sair        ^R Ler Arquivo   ^\ Substituir     ^U Colar Texto  ^T Verificar Ortografia    ^_ Ir Para Linha  M-E Refazer       M-6 Copiar Texto
```
Quando enter é pressionado o nano é executado e podemos editar o arquivo. para navegar entre as linhas você pode usar as teclas de seta pra cima e pra baixo

O nano tem recursos fáceis de lembrar e cobre coisas gerais incluindo:
- pesquisa de texto
- copy e paste
- ir para uma linha pelo número dela
- descobrir em qual linha você está

Você pode usar os recursos do nano usando ctrl (representado na interface por "^") + a letra correspondente. Por exemplo, para sair você usa ctrl + X

### Vim

Não vamos entrar em detalhes por enquanto por ser um editor mais avançado, foca em se acostumar com o nano por agora.

### Baixar arquivos usando o Wget

O comando Wget faça download de arquivos web via HTTP - como se você estivesse acessando o arquivo pelo navegador. A única coisa que você precisa é do caminho completo do script, desde o https:// até o link do download, se eu quisesse baixar um arquivo "arquivo.txt" pela web eu usaria:
`wget https://XXXXX.XXXXXX/XXXXX.XXXXXX/XXXXXXXXXXX-XXXXXX/XXXX/XXX/arquivo.txt`

### Transferir arquivos do seu host usando o Scp

Secury copy, ou SCP é um jeito de copiar arquivos sem um ladrãozinho capturar seus dados. Diferente do cp, ele permite transferir arquivos de dois computadores usando SSH para autentificar e criptografar

O SCP trabalha com um modelo de fonte (computador com o arquivo original) e destino (computador em que o arquivo vai ser copiado)
o SCP permite:
- copiar arquivos e diretórios da sua máquina para um sistema remoto
- copiar arquivos e diretórios do sistema remoto para a sua máquina

desde que você saiba o nome de usuário e senha no sistema local e remoto

o comando scp para transferir dados de um sistema em que você está logado é:
`scp flag.txt ubuntu @192.168.1.30:/home/ubuntu/transfer.txt`
o comando scp para transferir dados de um sistema em que você não está logado é:
`scp ubuntu@192.168.1.30:/home/ubuntu/documents.txt nota.txt`

### Servindo arquivos do seu host - Web

O python3 vem com um módulo fácil de usar, o HTTPServer. Isso transforma o seu pc literalmente em um servidor você pode usar para distribuir arquivos que podem ser baixados remotamente

o HTTPServer serve os arquivos no diretório onde o comando foi usado, para transformar o seu pc no servidor, é só usar o comando `python3 -m http.server` no terminal

Agora você pode usar o wget para baixar o arquivo remotamente usando o ip da sua máquina que hospeda o server.
**nota: o servidor roda na porta *8000* <br>Você precisa abrir um novo terminal para executar o wget enquanto o servidor roda, caso você cancele o script o servidor para de rodar**

## Visualizar processos
Você pode usar `ps` para conseguir uma lista de processos em execução na sessão e algumas informações como status, sessão, quantos gigas de ram o chrome tá usando e o nome e pid(process id) do programa ou comando

pra xeretar os processos usados por outros usuários, você pode usar:

`ps aux`

Outro comando útil é o `top`. ele fornece dados em tempo real dos processos em vez de visualização única, o top atualiza a lista a cada 10 segundos. 

## Gerenciar processos

Você pode encerrar processos, existem vários tipos de sinais que se correlacionam como o processo é tratado pelo kernel. Para encerrar um comando, podemos usar o comando kill e o PID associado . Por exemplo, para encerrar o processo com PID 1337, usaríamos kill 1337.

- SIGTERM - Encerra o processo, mas permite que execute algumas tarefas de limpeza
- SIGKILL - Encerra o processo - não faz nenhuma limpeza
- SIGSTOP - Para/suspende um processo

O Sistema usa namespaces para dividir recursos do PC (ram, cpu e prioridade), é tipo dividir o PC e impedir que o google ocupe 20 gigas de ram, cada parte do pc tem acesso a uma partição de recursos que ele pode usar
namespaces são bons para segurança, já que só processos do mesmo namespace podem se ver, é como se só pessoas autorizadas pudessem ver a sua casa.

O processo com o pid 0 é iniciado quando o sistema é ligado. Esse processo é o init (no ubuntu), como o systemd, usado como uma forma de gerenciar processos entre o sistema e o usuário

Quando o sistema é iniciado, o systemd é um dos primeiros processos iniciados. Qualquer software  começa como processo filho do systemd. Então, ele é controlado pelo systemd, mas é executado como processo independente para tornar a identificação mais fácil

## Iniciar processos na inicialização

alguns aplicativos são iniciados com o sistema. Por exemplo, servidores, banco de dados, normalmente esse tipo de software é importante e é programado para iniciar com o sistema.

Podemos usar `systemctl -`, esse comando permite interagir com o processo/demon no systemd. systemctl é um comando fácil e a sintaxe é: *`systemctl [opção] [serviço]`*, para iniciar um servidor apache, usamos o comando `systemctl start apache2`, para parar o apache, usamos `systemctl stop apache2`

O systemctl tem 4 opções:
- start (Iniciar)
- stop (parar)
- enable (ativar)
- disable (desativar)

## Backgrounding e foregrounding no Linux

os processos podem ser iniciados em **segundo plano** e em **primeiro plano**, o comando echo é executado em primeiro plano, por que é o único comando e não foi instruído para rodar em segundo plano

Iniciar um processo em segundo plano te ajuda a não ficar olhando pra tela sem fazer nada enquanto uma varredura de 2h funciona 
```
root@linux1:~/ echo "hello, World!" &
[1]16532
```
ao invés de executar a saída do comando echo, o operador `&` faz com que o comando seja executado no id 16532

## Crontabs
Crontabs são usadas para agendar tarefas em horários específicos, Crontabs são boas para executar tarefas que não são muito usadas, mas acontecem de tempo em tempo, como um backup, atualizações ou scripts agendados

Cada linha de comando demtro de uma crontab tem 6 parâmetros que definem como e quando vão ser executados
- MIN (o minuto da hora que o comando é executado)
- HOUR (a hora do dia em que o comando é executado)
- DOM (o dia do mês que o comando vai ser executado)
- MON (o mês em que o comando vai ser executado)
- DOW (Dia da semana em que o comando vai ser executado)
- CMD (Comando ou script que vai ser executado)

para fazer um backup de 12 em 12h você pode usar:
```
0/12*** cp -R /home/cmnatic/documents/var/backups
```
"0" representa o minuto
"*/12" representa a hora (12), e os 3 asteriscos representam que não importa DOW, MON, e DOM em que o comando vai ser executado, restante é o comando

### Edição de crontabs
Para editar uma crontab, você pode usar o comando `crontab -e`, esse comando abre o editor de texto onde você pode adicionar, deletar e editar suas crontabs

### Wildcards

um wildcard (*) é usado para especificar que uma tarefa deve ser executada em todos os valores possíveis
- `* * * * * *` executa o comando a todo minuto
- `0 0 * * * *` executa o comando toda meia noite

##### Recursos para iniciantes
Existem algumas ferramentas para facilitar a criação de crontabs, essas ferramentas são boas para iniciantes:
- crontab generator (online): você fornece os parâmetros e o crontab Gen cria o comando organizado

cronGuru (online): outro recurso para entender e gerar códigos crontab