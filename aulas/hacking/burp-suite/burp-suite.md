# Básico do burp suite

O Burp Suite é um framework baseado em Java projetado para servir como uma solução para realizar testes de penetração web. Ele se tornou a ferramenta da indústria de segurança  web e móveis, incluindo os que dependem de interfaces de aplicativos (APIs).

Em termos simples, o Burp captura e permite a manipulação de todo o tráfego HTTP/HTTPS entre navegador e servidor web. Essa capacidade é o coração do framework. Ao interceptar, os usuários têm a flexibilidade de direcionar elas para componentes dentro do framework. A capacidade de interceptar, visualizar e modificar solicitações antes que cheguem ao servidor ou até manipular respostas antes que sejam recebidas pelo navegador torna o Burp uma ferramenta inestimável para testes manuais

O Burp está disponível em diferentes edições. Para nós, vamos usar o Burp Suite Community Edition, que é livremente acessível para uso não comercial dentro dos limites legais. No entanto, vale lembrar que o Burp Suite também oferece edições Professional e Enterprise, que vêm com recursos avançados

 
# Burp suite community

A versão community, apesar de oferecer menos recursos em comparação com as outras, tem algumas adições da comunidade importantes, como:

Proxy: O Burp Proxy é o aspecto mais renomado do Burp suite. permite a interceptação e modificação de solicitações e respostas.

Repeater: Outro recurso conhecido. O Repeater permite capturar, modificar e reenviar a mesma solicitação várias vezes. Essa funcionalidade é útil ao criar payloads por tentativa e erro (por exemplo, em SQLi - Injeção de Linguagem de Consulta Estruturada) ou testar a funcionalidade de um endpoint.

Intruder: Apesar das limitações de taxa no Community, o Intruder permite pulverizar endpoints com solicitações. Ele é usado para ataques de força bruta ou fuzzing. 

Decoder: oferece um serviço para transformação de dados. pode decodificar informações capturadas ou codificar payloads antes de enviá-los ao alvo. Embora existam serviços alternativos para isso, aproveitar o Decoder dentro do Burp pode ser eficiente.

Comparer: Como o nome sugere, o Comparer permite a comparação de dois blocos de dados no nível de palavra ou byte. Embora não seja exclusivo do Burp, a capacidade de enviar segmentos grandes de dados para uma ferramenta de comparação com um atalho de teclado acelera o processo. 

Sequencer: O Sequencer é usado ao avaliar a aleatoriedade de tokens, como valores de cookies de sessão ou outros dados gerados aleatoriamente. Se o algoritmo  para gerar essea valores não é aleatório e seguro o suficiente, pode expor brechas para ataques.

Além dos recursos, a base de código Java do Burp Suite facilita o desenvolvimento de extensões para aprimorar o framework. Essas extensões podem ser escritas em Java, Python (usando o interpretador Java Jython) ou Ruby (usando o interpretador Java JRuby). O módulo Burp Suite Extender permite carregar extensões no framework, enquanto o marketplace, conhecido como BApp Store, permite o download de módulos. Embora algumas extensões possam exigir uma licença profissional, ainda tem consideráveis extensões para o Burp Community. Por exemplo, o módulo Logger++ pode estender a funcionalidade de registro integrada do Burp Suite.