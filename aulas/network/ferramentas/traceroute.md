# Traceroute
O comando lógico que segue o ping é o **traceroute**, que pode ser usado para mapearo caminho que a solicitação percorre até á máquina de destino

A **internet é composta por muitos, muitos e muitos servidores e pontos finais**, todos conectados. Isso significa que para chegar no conteúdo, você precisa passar por um monte de servidores. o Traceroute **permite que você veja cada uma dessas conexões**, ele permite que você veja cada passo entre o seu computador e o destino. A sintaxe básica do comando traceroute é `traceroute <endereço>`

Por padrão, o traceroute no windows (tracert) opera usando o mesmo protocolo que o ping utiliza (ICMP), em Unix like, ele opera usando. Obviamente isso pode ser alterado com flags

![traceroute](/content/traceroute.png)

Nesse caso, antes de chegar me discord.com, eu passei por exatamente 8 rotas do meu roteador até o servidor do discord