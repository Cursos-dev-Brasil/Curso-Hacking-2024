# O que é FTP

O *file transfer protocol*(FTP) é um protocolo usado para **permitir transferência de arquivos pela rede**. é implementado no **modelo cliente-servidor** e **retransmite comandos e dados** de forma eficiente

## Como funciona

Quando um serviço que aceita conexões remotas é iniciado, ele **escuta em uma porta** especifica. Quando o **cliente faz uma conexão** a uma porta de um serviço FTP, eles podem **trocar informações**. Inicialmente, isso é na **forma de comandos**. Comandos estabelecem **detalhes da conexão e as operações** executadas

Geralmente, a **porta que roda o servidor FTP é a 21**


uma sessão FTP padrão **opera com dois canais**

- um canal de comando (as vezes controle)
- um canal de dados

O **canal de comando** é **usado para transmitir comandos** (e as respostas desse comando) e o canal de dados é **responsável por transferir os dados**

O ftp funciona da seguinte forma: O **cliente inicia a conexão**, o **servidor valida as credenciais** de login e **abre a sessão**

**com a sessão aberta**, o **cliente pode executar comandos** ftp no sistema

## Ativo e passivo

O servidor ftp suporta **3 tipos de conexão** 

1. ativa
2. passiva
3. ambas

**Em uma conexão ativa, o cliente abre uma porta, escuta e o servidor precisa se conectar a ele**

**Na passiva, o servidor abre uma porta, escuta e o cliente se conecta a ele**


Essa separação de informações de comando e dados em canais separados é um modo de **enviar comandos sem esperar a transferência de dados** terminar. Se os canais fossem interligados, você só poderia utilizar comandos entre as transferências de dados. O que não seria eficiente para transferências grandes, internets lentas ou até UX

como não quero que cada aula tenha 500 linhas, não vou detalhar 100% do protocolo ftp, caso queira aprender mais sobre, visite o site da [Internet engineering task force](https://www.ietf.org/rfc/rfc959.txt). A IETF é uma das agências que definem padrões de protocolos na internet

## Enumeração FTP

Para fazer login em um servidor ftp, você precisa saber se existe um cliente ftp no sistema. Na **maioria dos sistemas linux** o cliente já vem instalado, você pode testar isso digitando `ftp` no terminal. Se você for redirecionado para um prompt que diz: `ftp>`, você tem um cliente ftp. Caso contrário, o comando `sudo apt install ftp` deve funcionar

No ftp, o comando `cwd` (change work directory) é muitas vezes associado a uma vulnerabilidade, por exemplo, `cwd /home/user` mudaria o diretório atual para /home/user

Algumas versões do ftp, como in.ftpd têm um comportamento diferente em relação a esse comando

1. Se você mudar para um diretório existente, o servidor responde com um código de sucesso, muitas vezes 250 OK
2. Se não ele responde com um erro como 550 Not Found

Como o comando cwd pode ser usado antes da autenticação, você pode usar isso para descobrir diretórios e contas de usuário

um exemplo prático seria o seguinte:

```
CWD /home
250 OK

CWD /home/user1
250 OK

CWD /home/user2
550 Not Found
```

Lembrando que isso pode variar de versão em versão do ftp