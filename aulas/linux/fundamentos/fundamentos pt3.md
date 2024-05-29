# Fundamentos linux parte 3 

Até agora só sabemos adicionar conteúdo a um arquivo usando `echo "conteúdo" > arquivo.txt`, mas esse método não é eficiente, principalmente quando você precisar colar múltiplas linhas de código ou outros tipos de conteúdo

## editores de texto de terminal

Existem opções com uma variedade de utilidades e funções, nesse curso, o foco vai ser sempre o *nano*

### Nano

É fácil começar com o Nano. Para editar um arquivo com nano usamos nano nome_do_arquivo

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

Não vamos entrar em detalhes sobre o vim por enquanto por ser um editor muito mais avançado, mas no futuro vamos.

### Baixar arquivos usando o Wget

O comando Wget permite que você faza downloads de arquivos web via HTTP - como se estivesse acessando o arquivo pelo navegador web. A única coisa que precisamos é o caminho completo do script que vamos baixar, desde o https:// até o link do download, por exemplo, se eu quisesse baixar um arquivo "arquivo.txt" pela web eu usaria:
`wget https://XXXXX.XXXXXX/XXXXX.XXXXXX/XXXXXXXXXXX-XXXXXX/XXXX/XXX/arquivo.txt`

### Transferir arquivos do seu host usando o Scp

Secury copy, ou SCP é uma forma de copiar arquivos de forma segura. Diferente do cp, ele permite transferir arquivos de dois computadores usando SSH para autentificar e criptografar

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

O python3 vem com um módulo fácil de usar chamado HTTPServer. Esse módulo transforma o seu pc em um servidor HTTP rápido e fácil de usar que você pode usar para distribuir seus arquivos que podem ser baixados remotamente com curl ou wget

o HTTPServer serve os arquivos no diretório onde o comando foi usado, para transformar o seu pc no servidor, é só usar o comando `python3 -m http.server` no terminal

Agora você pode usar o wget para baixar o arquivo remotamente usando o ip da sua máquina que está hospedando o server.
**nota: o servidor python roda na porta *8000* <br>Você precisa abrir um novo terminal para executar o wget enquanto o servidor roda, caso você cancele o script HTTPServer o servidor para de rodar**

## Visualizar processos
Você pode usar o comando `ps` para fornecer uma lista de processos em execução na sessão e algumas informações como código de status, sessão que está executando, quanto tempo de CPU é consumido e o nome e pid do programa ou comando

para ver os processos rodados por outros usuários podemos usar o comando

`ps aux`

Outro comando útil é o `top`. Que fornece estatisticas em tempo real dos processos rodando em vez de visualização única, o top atualiza a lista a cada 10 segundos. 

Gerenciar processos

Você pode terminar processos, existem vários tipos de sinais que se correlacionam como o processo é tratado pelo kernel. Para encerrar um comando, podemos usar o comando kill e o PID associado que desejamos encerrar. Por exemplo, para encerrar o PID 1337, usaríamos kill 1337.

- SIGTERM - Encerra o processo, mas permite que ele execute algumas tarefas de limpeza antes
- SIGKILL - Encerra o processo - não faz nenhuma limpeza depois
- SIGSTOP - Para/suspende um processo

O OS usa namespaces para dividir recursos disponíveis no PC (ram, cpu e prioridade), é como dividir o PC em partes, cada parte terá acesso a uma parte de recursos que ele pode usar
namespaces são bons para segurança, já que só processos do msm namespace podem se ver

O processo com o pid 0 é iniciado quando o OS é inicializado. Esse processo é o init (no ubuntu), como o systemd, usado para fornecer uma forma de gerenciar processos de um usuário entre o OS e o usuário

Quando o sistema é inicializado e ele se inicializa, o systemd é um dos primeiros processos iniciados. Qualquer software iniciado começa como um processo filho do systemd. Ou seja, ele é controlado pelo systemd, mas é executado como um processo independente para tornar mais fácil a identificação

# Iniciar processos na inicialização

alguns aplicativos são iniciados na inicialização do sistema. Por exemplo, servidores web, banco de dados ou servidores de transferência de dados, normalmente esse tipo de software é crucial e é instruído para iniciar com o sistema.

Podemos usar o comando systemctl -, esse comando permite interagir com o processo/demon no systemd. systemctl é um comando fácil de usar e a sintaxe dele é: *`systemctl [opção] [serviço]`*. Por exemplo, para iniciar um servidor apache, usamos o comando `systemctl start apache2`, para por exemplo parar o apache, usamos `systemctl stop apache2`

O systemctl tem 4 opções possíveis:
- start (Iniciar processo)
- stop (parar processo)
- enable (ativar processo)
- disable (desativar processo)

## Backgrounding e foregrounding no Linux

os processos podem ser iniciados em **segundo plano** e em **primeiro plano**, comando X mo echo são executados em primeiro plano, pois é o que o único comando e não foi instruído para rodar em segundo plano
exemplo: 
```
root@linux1:~/ echo "hello, World!" &
[1]16532
```
ao invés de executar a saída do comando echo, o operador `&` faz com que o comando seja executado no id 16532

## Crontabs
Crontabs são usados pelo Linux para agendar tarefas em horários específicos, Crontabs são essenciais para executar tarefas que não são muito usadas, mas acontecem de tempos em tempos, como backups, atualizações de sistemas ou scripts agendados

Cada linha de comando tem 6 parâmetros que definem como é quando vão ser executados
- MIN (o minutodahora que o comando é executado)
- HOUR (a hora do dia em que o comando é executado)
