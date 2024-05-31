# Evasão de firewall

Para **contornar uma configuração padrão de firewall** que bloqueia ICMP, o nmap **fornece a opção -Pn**, que instrui o nmap a **não fazer o ping do host antes de fazer o scan**. Isso **contorna o bloqueio ICMP**, mas **pode demorar mais para efetuar a varredura**, **principalmente se o host estiver inativo**, por que o nmap **vai continuar verificando cada porta**

Existem **flags úteis para evasão de firewall**

- -f: Fragmenta pacotes, dividindo-os em partes menores para reduzir a probabilidade de detecção por um firewall ou IDS.
- --mtu <número>: Especifica um tamanho máximo de unidade de transmissão para os pacotes enviados. Isso fornece mais controle sobre o tamanho do pacote em comparação com -f.
- --scan-delay <tempo>ms: Adiciona um atraso em milisegundos entre os pacotes enviados, útil para redes instáveis e para evadir gatilhos de firewall/IDS baseados em tempo.
- --badsum: Gera um checksum inválido para os pacotes. Embora pilhas TCP/IP reais descartem esses pacotes, firewalls podem responder automaticamente sem verificar o checksum, revelando sua presença.

