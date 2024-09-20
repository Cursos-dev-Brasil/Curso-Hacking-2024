# Nmap

## Por que a Enumeração é Importante
Antes de começar a invadir (ou auditar) qualquer sistema, a primeira regra é conhecer o terreno. Se você não sabe o que tem na sua frente, você vai tropeçar em qualquer armadilha mal feita. Então sua primeira missão é descobrir quais serviços estão rodando no alvo.

Pensa em um IP como uma casa. O Nmap é a ferramenta que você usa para descobrir quais portas dessa casa estão destrancadas e quais serviços (tipo "servidor web" ou netBIOS) estão funcionando dentro. Uma vez que você sabe onde as portas estão, você pode decidir como entrar

### Escaneamento de Portas
O Nmap funciona como um detetive, procurando cada porta no alvo para descobrir quais estão abertas. Pensa nas portas como entradas diferentes para a casa. Algumas portas são padrões, como a 80 (para sites HTTP) ou a 443 (para sites HTTPS), mas, em algumas casas, as portas podem estar em lugares inusitados. Quem sabe, o HTTP rolando na porta 64204 ou o SMB na porta 524

Para garantir que você encontre essas entradas, o Nmap faz uma varredura em todas as 65.535 portas (porque sim, cada computador tem exatamente esse número de portas e normalmente 80% delas são inúteis). Dependendo de como a porta reage, o Nmap te diz se ela está aberta, fechada ou protegida por um firewall (como se a porta estivesse trancada).

Por que Usar o Nmap

Por que o Nmap? A resposta é simples: ele é o melhor no que faz. Nenhuma outra ferramenta de escaneamento de portas chega perto da funcionalidade do Nmap. É como se você estivesse jogando futebol, e o Nmap fosse o Pelé – só que, em vez de marcar gols, ele encontra portas abertas e explora vulnerabilidades.

Além disso, o Nmap tem um mecanismo de script que transforma ele em uma ferramenta capaz de não só descobrir fraquezas, mas até explorá-las.


