# Packet sniffer

Um packet sniffer (ou um analisador de pacotes) é uma **ferramenta de captura de pacotes de rede**, costuma ser usada por administradores de sistemas (para diagnósticos de redes e etc) ou por hackers ou crackers. Cain and Abel, tcpdump ou Wireshark são exemplos de packet sniffers.

Um sniffer funciona **capturando primeiro o pacote que ele recebe** da rede (incluindo pacotes destinados a hosts externos). Isso pode ser feito em uma LAN (Local Area network) que **conecta hosts em um hub**. Um **hub funciona encaminhando todos os pacotes que recebe para todos os hosts** conectados. **Independente do destino** do pacote

![](/content/hub.png)

Tudo que você precisa para interceptar pacotes é um sniffer em um host com uma NIC (Network Interface card) no modo promíscuo

Promíscuo é um modo que algumas NICs assumem que permitiria o recebimento de todos os pacotes, Por padrão as NICs são programadas para descartar todos os dados que não foram endereçados a elas. Se você quiser fazer um ataque de sniffing você usaria o modo de promíscuo


## Arp-poisoning

### Ataque man-in-the-middle

Não vamos entrar em detalhes sobre um ataque man-in-the-middle por que já temos uma aula sobre isso [aqui](/aulas/hacking/network-hacking/MITM/). O que você precisa saber é que ele é um tipo de espionagem e interceptação de pacotes com dados como senhas, usuários, emails e etc. Em um ataque MITM, os dados que deveriam passar de uma ponta a outra (como um cliente e um servidor) sofrem interceptação no meio desse processo, fazendo com que os dados interceptados possam ser lidos porém ainda são enviados ao servidor, como se nada estivesse acontecendo

Arp-poisoning é um exemplo de MITM, ele tira proveito do protocolo arp (usado para converter IPs em MACs). Mais detalhes do protocolo [aqui](/aulas/network/protocols/arp.md)


