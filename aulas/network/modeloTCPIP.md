# Modelo TCP/IP

O modelo TCP/IP é **semelhante ao OSI**, ele é alguns anos mais antigo e serve como **base para redes no mundo real**. O modelo consiste em 4 camadas: *Aplicação, Transporte, Internet e Interface de Rede*. Juntas, cobrem a mesma variedade de funções das sete camadas do modelo OSI

**nota: Algumas fontes dividem TCP/IP em 5 camadas, separando a camada interface de rede por Enlace de dados e Física, é aceito e conhecido mas oficialmente é indefinido (ao contrário das 4 originais definidas no *RFC1122) no geral as 2 versões são válidas**

Você pode se perguntar por que eu ensinei o modelo OSI, já que ele **não é usado no mundo real** e a resposta é bem simples, o modelo OSI (por ser **menos condensado** e **mais rigído** que o TCP/IP) tende a ser mais fácil para aprender a teoria inicial

Comparação:<br>
![Comparação](/content/comparaçãoTCp-OSI.png)

Os processos de encapsulamento e desencapsulamento funcionam da mesma forma nos modelos TCP/IP e OSI, em cada camada do TCP/IP, um header é adicionado no encapsulamento e removido no desencapsulamento

Um modelo de camadas é ótimo para auxilio visual, mas como isso acontece?

No sentido de TCP/IP, é bom pensar em uma tabela com 4 camadas, mas nesse caso estamos falando de uma **suite de protocolos** (conjunto de regras que definem como uma ação deve ser realizada). O TCP/IP l**eva no nome 2 dos protocolos mais importantes**: O **protocolo de Controle de Tranmissão** (TCP), que controla o fluxo de dados entre 2 pontos finais, e o **protocolo de internet** (IP) que controla como os pacotes são enviados e endereçados. Existem outro protocolos que compõe a suíte TCP/IP mas TCP e IP são os principais por agora

TCP é um protocolo **baseado em conexão**. Antes de enviar qualquer dado via TCP, é preciso formar uma conexão chamada **handshake de três vias**

## handshake de três vias 

Ao tentar estabelecer uma conexão, seu **computador envia primeiro uma solicitação especial** para o servidor remoto indicando que deseja iniciar uma conexão. Essa solicitação **contém bit SYN** (abreviação de sincronização), que faz o **primeiro contato para iniciar a conexão**. O servidor responde com um pacote contendo o bit SYN, além de outro **bit "de reconhecimento"** (ACK). **Seu computador envia um pacote com apenas o bit ACK**, confirmando que a conexão foi estabelecida. Com o handshake de três vias concluído, os dados podem ser **transmitidos de forma confiável** entre os dois computadores. **Qualquer dado perdido ou corrompido na transmissão é reenviado**, resultando em uma conexão que parece ser sem perdas.

## História 

é importante entender por que os modelos TCP/IP e OSI foram criados. Inicialmente, não tinha padronização, cada fabricante tinha a própria metodologia e sistemas feitos por fabricantes diferentes tinham 0 compatibilidade no quesito de redes. O modelo TCP/IP foi introduzido pelo Departamento de Defesa dos Estados Unidos em 1982 para fornecer um padrão (Algo para todas as fabricantes seguirem) Isso resolve o problema de inconsistência. Mais tarde, o modelo OSI foi introduzido pela ISO (Organização Internacional de Normalização). Mas ele é usado como guia mais abrangente para aprendizado.