
# Varredura ICMP

Quando você chega em uma nova rede, é como "Descobrir" um país. O primeiro passo é conseguir um "mapa" da área para saber onde estão os hosts ativos e onde não há nada. É aqui que entra a varredura ICMP, ou ping sweep.

## O Que É Varredura ICMP?
Imagine que você quer verificar quais das casas na sua rua estão ocupadas. Você manda um ping (ou seja, um tipo de chamado) para cada casa. Se alguém responde, você sabe que a casa está ocupada. Se ninguém responde, a casa pode estar vazia.

isso é feito com o Nmap, que envia pacotes ICMP para cada endereço IP na rede. Se um endereço IP responde, significa que há um host ativo lá. É uma forma rápida e prática de ver quem está em casa.

Como Fazer Isso com o Nmap?
Você pode usar a opção -sn para realizar uma varredura ping. Isso instrui o Nmap a não escanear as portas e apenas verificar a presença de hosts com pacotes de eco ICMP.


### Usando Intervalos de IP:

`nmap -sn 192.168.0.1-254`
Isso vai verificar todos os IPs de 192.168.0.1 a 192.168.0.254.

Usando Notação CIDR:

`nmap -sn 192.168.0.0/24`
Isso faz o mesmo, mas usando notação CIDR para indicar a rede inteira (é um jeito mais chique)

#### O Que Acontece Nos Bastidores?
Quando você usa a opção -sn:

O Nmap envia pacotes ICMP Echo Request para cada IP no intervalo.
Se o host responder com um ICMP Echo Reply, ele é marcado como ativo.
Além dos pacotes ICMP, o Nmap também envia:
Um pacote TCP SYN para a porta 443.
Um pacote TCP ACK (ou SYN se não for root) para a porta 80.
Por que isso é útil? Às vezes, os pacotes ICMP podem ser bloqueados por firewalls, então o Nmap também usa pacotes TCP para verificar se o host está ativo de forma alternativa.

Esse conteúdo é tão monótono que eu não consigo nem fazer piada, mas confia por que ele é importante