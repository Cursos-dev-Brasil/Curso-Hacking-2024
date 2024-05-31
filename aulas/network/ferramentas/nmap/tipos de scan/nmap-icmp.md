# Varredura ICMP

Na **primeira conexão a uma rede** de destino, o **primeiro objetivo pode ser conseguir um "mapa"** da estrutura da rede, simplificando queremos **ver quais endereços IP contêm hosts ativos equais não contêm**

Você pode usar o **Nmap para fazer uma varredura de ping** (ping sweep). O Nmap **envia um pacote ICMP para cada endereço IP possível** da rede. **Quando recebe resposta**, **marca o IP que respondeu ativo**. isso **nem sempre é preciso**, mas, pode dar uma **linha de base** e, vale a pena tentar.

Para fazer uma **varredura ping usamos a opção -sn + um intervalo de IP**, que pode ser especificado como um hifen ou **notação CIDR**, então podemos fazer a varredura de duas formas: 

usando intervalos de ip:
**`nmap -sn 192.168.0.1-254`**

ou usando notação CIDR:
**`nmap -sn 192.168.0.0/24´**
A opção -sn **diz ao Nmap para não escanear nenhuma porta**, forçando a confiar em **pacotes de eco ICMP** (**solicitações ARP em uma rede local**, se executado com sudo ou como root) para **identificar alvos**. **Além das solicitações de eco**, a opção -sn também **faz com que o Nmap envie um pacote TCP SYN para a porta 443** do alvo, e um pacote **TCP ACK (ou TCP SYN se não for executado como root) para a porta 80** do alvo.
