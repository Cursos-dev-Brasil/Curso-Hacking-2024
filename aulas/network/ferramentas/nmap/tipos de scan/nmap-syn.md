# Varreduras SYN (-sS)

Assim como as varreduras TCP, as **varreduras SYN são usadas para escanear a faixa de portas TCP** de um alvo, mas os 2 tipos de varredura funcionam de maneira diferente. As varreduras SYN podem ser chamadas também de **varredura Half-open ou varreduras Stealth**

Enquanto a TCP utiliza um handshake completo de três vias, as **varreduras SYN enviam de volta um pacote TCP RST** após **receberem um SYN/ACK do servidor (isso impede que o servidor tente fazer a solicitação repetidamente)**

![Esquema do envio de pacotes SYN](/content/stealth.png)

Em outras palavras isso tem algumas vantagens para um hacker

1. Pode ser usada para **contornar sistemas de Detecção de intrusão** (IDS) mais **antigos**, por que eles **procuram handshakes completos** de três vias. Isso geralmente não **acontece com as IDS modernas**, e é por isso que as varreduras SYN **ainda** são chamadas de **varreduras stealth**

2. Varreduras SYN **não costumam ser registradas por aplicativos usando portas abertas**, por que o padrão é **registrar a conexão quando ela for totalmente estabelecida**, isso também se encaixa na ideia de varredura stealth

3. **Sem precisar se preocupar em completar (e desconectar) o handshake** para cada porta, as varreduras são **significamente mais rápidas** do que a TCP connect padrão

Mas, obviamente também tem algumas desvantagens

1. **Exigem permissões de sudo** para funcionar no linux, isso acontece por que as **varreduras SYN exigem capacidade de criar pacotes brutos** (em vez do handshake completo), oque por padrão, é um **privilégio que só o root tem**

2. **Serviços instáveis podem ser derrubados por varreduras SYN**, o que pode ser problemático se por exemplo, um cliente tiver fornecido um ambiente de produção para teste, falando a grosso modo, você pode causar um **DoS não intencional** no cliente

No geral, as vantagens superam as desvantagens

Por isso, as varreduras SYN são **varreduras padrão usadas pelo Nmap se executadas com permissões de sudo**, caso seja executado **sem o sudo, o padrão vai ser a TCP connect**


Se a porta estiver fechada, o servidor responde com um pacote TCP RST. Se filtrada por um firewall, o pacote é descartado ou *spoofado* com um RST TCP

nesse sentido, as duas são identicas, a **diferença é como lidam com portas abertas**

![Captura de pacotes wireshark](/content/SYN-wireshark.png)