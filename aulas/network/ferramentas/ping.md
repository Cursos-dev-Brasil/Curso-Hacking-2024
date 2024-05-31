# Ping

O comando `ping` é usado para testar a conexão com um recurso remoto. isso pode ser um site, ou um computador na mesma rede que a sua. Ping funciona com o protocolo ICMP, que é um dos protocolos TCP/IP um pouco menos conhecido. O protocolo opera da camada de Rede (Network) do modelo OSI, e no modelo Internet do TCP/IP. A sintaxe básica do comando é `ping <endereço>`

Você pode por exemplo testar sua comunicação com o google.com

![ping Google](/content/ping.png)

o comando retorna o ip do servidor, ao invés da URL fornecida. Essa é uma função secundária útil do ping, por que pode ser usado para determinar o ip do servidor que hospeda o site. Uma das vantagens do ping é que ele é onipresente em qualquer dispositivo habilitado para rede. 

Tente usar o comando ping no site *https://discord.com/*, tente exibir os 2 tipos de ip (IPV4 e IPV6) usando flags