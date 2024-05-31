# Falha de criptografia

Uma falha Criptográfica se refere a qualquer vulnerabilidade que remete a uso indevidoa (ou falta) de criptografia para proteger dados sensíveis. Uma aplicação web necessita de criptografia para garantir a confidencialidade de seus usuarios

Vamos usar o Gmail como um exemplo:

Quando você acessa sua conta gmail usando o navegador, quer ter certeza de que comunicações entre você e servidor estão criptografadas. assim, qualquer ladrão tentando pegar seus pacotes de rede não consegue recuperar o conteúdo dos emails Quando criptografamos o tráfego entre cliente e o servidor. Uma vez que os emails são armazenados em algum servidor gerenciado pelo provedor, você também precisa ter certeza que ninguém de dentro do provedor pode ler os emails de um clientes. Para isso, seus emails podem ser criptografados quando armazenados nos servidores. Isso é referido como criptografar dados em repouso. falhas criptográficas resultam em aplicativos web divulgando acidentalmente dados sensíveis. Isso geralmente são dados diretamente relacionados aos clientes (por exemplo, nomes, datas de nascimento, informações financeiras), mas também podem ser informações técnicas, como nomes de usuário e senhas.

Em níveis complexos, aproveitar falhas criptográficas envolve técnicas como Man in The Middle Attacks, em que o atacante força conexões do usuário por um dispositivo que eles controlam. depois, eles se aproveitariam da criptografia fraca em qualquer dado transmitido para acessar as informações (se os dados estiverem criptografados em primeiro lugar). Claro, muitos exemplos são muito mais simples, e vulnerabilidades podem ser encontradas em aplicativos web que podem ser exploradas sem conhecimento avançado de rede. De fato, em alguns casos, os dados podem ser encontrados diretamente no próprio servidor web.

