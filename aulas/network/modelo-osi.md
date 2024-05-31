# **OSI model**

The OSI (**Open System Interconnection**) Model é um modelo padronizado que usamos para demonstrar a teoria por trás das redes de computadores. Na prática, é na verdade o modelo TCP/IP mais compacto que é a base das redes do mundo real, mas, o modelo OSI, de muitas maneiras, é mais fácil de entender.

O modelo OSI consiste em **7 camadas**:

## **Camada 7 - Aplicação:**
- A camada de aplicação consiste em fornecer opções de redes para programas em execução. Trabalha quase exclusivamente com aplicativos, fornecendo uma interface para transmitir dados.

## **Camada 6 - Apresentação:**
- A camada de apresentação recebe dados da camada de aplicação. Esses dados normalmente estão em um formato que o aplicativo entende, mas não necessariamente em um formato padronizado que pode ser entendido pela camada de aplicação no computador receptor. A camada de apresentação traduz os dados em um formato padronizado, além de lidar com a criptografia, compressão ou transformações nos dados. Com isso completo, os dados são passados para a camada de sessão.

## **Camada 5 - Sessão:**
- Quando a camada de sessão recebe os dados formatados da camada de apresentação, ela verifica se pode estabelecer uma conexão com o outro computador pela rede. Se não, envia de volta um erro e o processo não continua. Se uma sessão puder ser estabelecida, então é trabalho da camada de sessão manter a conexão ativa, e cooperar com a camada de sessão do computador remoto para sincronizar as comunicações.

## **Camada 4 - Transporte:**  
- A camada de transporte é uma camada que desempenha funções importantes. Seu primeiro objetivo é escolher o protocolo pelo qual os dados são transmitidos. Os dois mais comuns na camada de transporte são TCP (**Transmission Control Protocol**) e UDP (**User Datagram Protocol**); com TCP, a transmissão é baseada em conexão, o que significa que uma conexão entre os computadores é estabelecida e mantida durante a solicitação.

## **Camada 3 - Rede:**
- A camada de rede é responsável por localizar o destino da sua solicitação. Por exemplo, a Internet é uma rede enorme; quando você quer solicitar informações de uma página da web, é a camada de rede que pega o endereço IP da página e descobre a melhor rota.

## **Camada 2 - Enlace de dados:**
- A camada de enlace se concentra no endereçamento fisíco da transmissão. Ela recebe um pacote da camada de rede (com o IP do computador remoto) e adiciona o MAC (Endereço fisíco) do ponto final do receptor.

## **Camada 1 - Fisíca:**
- A camada fisíca é relacionada ao hardware. É onde os pulsos elétricos são enviados e recebidos. A função dessa camada é traduzir os dados binários em sinais e transimiti-los na rede, além de receber sinais de entrada e converter de volta para binário.

![Representação do modelo OSI](/content/modelo-osi.png)
