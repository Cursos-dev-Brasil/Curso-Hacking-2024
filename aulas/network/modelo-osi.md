# OSI model

The OSI (Open System Interconnection) Model é um modelo padronizado que usamos para demonstrar a teoria por trás das redes de computadores. Na prática, é na verdade o modelo TCP/IP mais compacto que é a base das redes do mundo real, mas, o modelo OSI, de muitas maneiras, é mais fácil de entender

o modelo OSI consiste em 7 camadas

Camada 7 - aplicação:
    - A camada de aplicação consiste em fornecer opções de redes para programas em execução. Trabalha quase exclusivamente com aplicativos, fornecendo uma interface para transmitir dados
Camada 6 - Apresentação:
    - A camada de apresentação recebe dados da camada de aplicação. Esses dados normalmente estão em um formato que o aplicativo entende, mas não necessariamente em um formato padronizado que pode ser entendido pela camada de aplicação no computador receptor. A camada de apresentação traduz os dados em um formato padronizado, além de lidar com a criptografia, compressão ou transformações nos dados. Com isso completo, os dados são passados para a camada de sessão.
Camada 5 - Sessão:
    - Quando a camada de sessão recebe os dados formatados da camada de apresentação, ela verifica se pode estabelecer uma conexão com o outro computador pela rede. Se não, envia de volta um erro e o processo não continua. Se uma sessão puder ser estabelecida, então é trabalho da camada de sessão manter a conexão ativa, e cooperar com a camada de sessão do computador remoto para sincronizar as comunicações. A camada de sessão é importante porque a sessão que ela cria é única para a comunicação. E permite que você faça várias solicitações para endpoints diferentes sem que todos os dados se misturem (tipo abrir duas abas em um navegador ao mesmo tempo) Quando a camada de sessão regista com êxito uma conexão entre o host e o computador remoto, os dados são passados para a Camada 4
Camada 4 - Transporte:  
    - A camada de transporte é uma camada que desempenha funções importantes. Seu primeiro objetivo é escolher o protocolo pelo qual os dados são transmitidos. Os dois mais comuns na camada de transporte são TCP (Transmission Control Protocol) e UDP (User Datagram Protocol); com TCP, a transmissão é baseada em conexão, o que significa que uma conexão entre os computadores é estabelecida e mantida durante a solicitação. Isso permite uma transmissão confiável, pois a conexão pode ser usada para garantir que os pacotes cheguem ao lugar certo. Uma conexão TCP permite que os dois computadores permaneçam em comunicação para garantir que os dados sejam enviados em uma velocidade aceitável e que quaisquer dados perdidos sejam reenviados. Com o UDP, é o oposto; pacotes de dados são essencialmente lançados no computador receptor -- se ele não conseguir acompanhar, esse é o problema dele (é por isso que uma transmissão de vídeo em algo como o Skype pode ficar pixelada se a conexão estiver ruim). O que isso significa é que o TCP geralmente seria escolhido para situações em que a precisão é favorecida em relação à velocidade (por exemplo, transferência de arquivos ou carregamento de uma página da web), e o UDP seria usado em situações em que a velocidade é mais importante (por exemplo, streaming de vídeo).

Camada 3 - Rede:    
    - A camada de rede é responsável por localizar o destino da sua solicitação. Por exemplo, a Internet é uma rede enorme; quando você quer solicitar informações de uma página da web, é a camada de rede que pega o endereço IP da página e descobre a melhor rota. Neste estágio, estamos trabalhando com o endereçamento lógico (ou seja, endereços IP), que são controlados por software. Endereços lógicos são usados para fornecer ordem às redes, categorizando e permitindo classificação correta. Atualmente, a forma mais comum de endereçamento lógico é o formato IPV4 (por exemplo, 192.168.1.1 é um endereço comum para um roteador residencial).

Camada 2 - Enlace de dados:
    - A camada de enlace se concentra no endereçamento fisíco da transmissão. Ela recebe um pacote da camada de rede (com o IP do computador remoto) e adiciona o MAC (Endereço fisíco) do ponto final do receptor. dentro de cada computador habilitado para rede tem um Cartão de Interface de rede (NIC) que vem com o endereço MAC (*Media Access Control*) 

O endereço MAC é definido pela fabricante e literalmente gravado no NIC, eles não podem ser alterados (podem ser falsificados). Quando uma informação é enviada por uma rede, é o endereço fisíco que é usado para identificar onde enviar as informações

também é funcão da camada de enlace apresentar os dados em um formato adequado para transmissão

A camada de enlace tem papel fundamental ao receber dados, por que verifica as informações para garantir que não tenham sido corrompidos

Camada 1 - Fisíca:
    A camada fisíca é relacionada ao hardware. É onde os pulsos elétricos são enviados e recebidos. A função dessa camada é traduzir os dados binários em sinais e transimiti-los na rede, além de receber sinais de entrada e converter de volta para binário

        








