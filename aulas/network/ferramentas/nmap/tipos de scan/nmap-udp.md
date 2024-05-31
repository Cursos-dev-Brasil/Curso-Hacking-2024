# UDP Scan (-sU)

As conexões UDP são diferentes das TCP, por que são *stateless* (sem estado). Em vez de iniciar uma conexão com um "handshake", as conexões UDP **dependem do envio de pacotes para uma porta e esperam que eles cheguem**. Isso torna o UDP **excelente para conexões que dependem da velocidade** em vez da qualidade, mas a **falta de confirmação** torna o UDP **significativamente mais difícil** (e muito mais lento) de escanear.

Quando o pacote é enviado para uma porta UDP aberta, **não deve ter resposta**, quando isso acontece, o Nmap **se refere a porta como aberta/filtrada**. Em outras palavras, **se ele não tem resposta**, ele **suspeita** de que a **porta está aberta**, mas também **pode ser protegida por um firewall**. Se receber uma **resposta UDP** (oque é bem raro) a porta é **marcada como aberta**. **Normalmente não tem resposta**, nesse caso, uma **segunda solicitação é enviada** como uma **verificação dupla**. se ainda não houver resposta, a porta é **marcada como aberta/filtrada**

Quando um pacote é enviado para uma **porta fechada**, o alvo **responde com um pacote ICMP** contendo uma **mensagem de que a porta é inacessível**. Isso **identifica claramente portas fechadas**, que o nmap marca como tal e continua o scan

Como é **difícil identificar se a porta está aberta**, as varreduras UDP **costumam ser incrivelmente lentas** em comparação a varreduras TCP (20 minutos para 1000 portas com uma boa conexão), por isso, é uma boa prática **executar varreduras udp com --top-ports <numero> ativado**, por exemplo, `nmap -sU --top-ports 20 <alvo>` verifica as **20 portas mais comuns**, oque acaba tendo um **tempo de scan mais aceitável**

Ao escanear portas UDP, o Nmap **geralmente envia solicitações vazias** (apenas pacotes UDP brutos) dito isso, para **portas normalmente ocupadas** por serviços conhecidos, ele **enviará uma carga útil do protocolo que é mais provável obter resposta**, resultando em um resultado mais preciso