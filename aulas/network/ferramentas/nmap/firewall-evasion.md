Evasão de Firewall

Às vezes, tentar escanear uma rede termina em um firewall que se comporta como um guarda de segurança, bloqueando tudo o que parece suspeito (vamo combinar que um comando que bate em todas as portas pra ver se elas estão abertas não costuma ser a coisa mais normal do mundo). Se o firewall decide fazer um bloqueio geral no ICMP, o nmap precisa dar um jeito de burlar isso. Aqui estão algumas técnicas de evasão que o Nmap usa para burlar esses bloqueios

1. Ignorando o Ping com -Pn
 Basicamente o Nmap Se Faz de Desentendido, ele sempre dá uma rápida espiada na rede, fazendo um ping para ver se o host está vivo. Se o firewall diz “não, obrigado” e bloqueia pings, o Nmap não fica triste. Com o -Pn, o Nmap simplesmente ignora o ping e pula para o escaneamento das portas. É como se dissesse: “Se você não quer me responder, tudo bem, eu não preciso de você mesmo”

2. Fragmentação de Pacotes com -f: O Nmap Se Despedaça
Às vezes, o firewall é tão bom no que faz que consegue identificar pacotes de escaneamento logo de cara. Para evitar isso, o Nmap pode usar a opção -f, que fragmenta os pacotes em pedaços menores, como se estivesse fazendo um quebra-cabeça. Isso ajuda a evitar a detecção, já que o firewall não consegue juntar todas as peças tão rápido.

3. Ajustando o Tamanho dos Pacotes com --mtu <número>
Pra um controle mais preciso sobre o tamanho dos pacotes, o Nmap pode usar --mtu <número>. É como se o Nmap estivesse ajustando o tamanho de cada pacote, garantindo que os pacotes tenham o tamanho exato para não chamar a atenção do firewall.

4. Adicionando Atraso com --scan-delay <tempo>ms
Quando a rede está instável ou o firewall está nervoso (ativo ou alerta), o Nmap pode usar a opção --scan-delay <tempo>ms para adicionar um pequeno atraso entre os pacotes. É como se estivesse fazendo uma dança lenta, evitando o gatilho do firewall com movimentos deliberados.

5. Gerando Checksums Ruins com --badsum
Por último, temos a --badsum, que gera um checksum inválido para os pacotes. É como se o Nmap estivesse enviando mensagens cifradas para o firewall, esperando que ele entre em pânico e revele sua localização.

