# Varredura TCP connect (-sT)

Para entender essas varreduras, você precisa estar **confortável com o TCP three-way handshake** (handshake de 3 vias), explicamos isso em [Modelo TCP/IP](../../modeloTCPIP.md)

Esse é um **principio fundamental da rede TCP/IP.** Como o nome sugere, essa varredura **funciona realizando o three-way handshake com cada porta** alvo. Em outras palavras, o Nmap tenta se conectar a cada porta TCP, e dependendo da resposta ele sabe se o serviço está rodando ou não

"... **Se a conexão não existir** (CLOSED), então um **reset é enviado** em resposta a qualquer segmento de entrada, exceto outro reset. Um **segmento SYN que não corresponda a uma conexão existente é rejeitado** por esse meio."

*O RFC 9293 afirma.*

simplificando mais ainda, se o **nmap envia uma solicitação** TCP com a **flag SYN para uma porta fechada**, o servidor alvo **responde com um pacote TCP com a flag RST** (reset). com essa definição, o Nmap **estabelece a porta como fechada**. Da mesma forma, se a **solicitação é enviada para uma porta aberta**, o **servidor responde com um pacote TCP** com as **flags SYN/ACK.** O nmap então **marca essa porta como aberta** e completa o handshake e completa o handshake **enviando a 3° via com o pacote com a flag ACK**

Ok, sabemos oque o nmap faz para definir se uma porta está aberta ou fechada, mas e **se a porta estiver aberta, mas atrás de um firewall?**

Muitos firewalls são **configurados para descartar/ignorar pacotes de entrada.** Então quando o nmap **envia a solicitação TCP**, não tem saída nenhuma, isso indica que a **porta é protegida por um firewall** e é considerada **filtrada**

Dito isso, é **fácil configurar um firewall** para **responder com um pacote TCP RST**, por exemplo no **IPtables para linux**, uma versão simples do comando seria:

`iptables -I INPUT -p tcp -dport <port> -j REJECT --reject-with tcp-reset`

Isso pode tornar **extremamente difícil (ou até impossivel)** obter uma leitura precisa do alvo
