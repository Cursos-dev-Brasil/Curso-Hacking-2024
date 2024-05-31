# URL

Um URL (Uniform Resource Locator) é um endereço que especifica como e onde acessar um recurso na internet. As partes principais de uma url são: 

- Esquema: Instrui qual protocolo utilizar, HTTP, HTTPS, FTP etc...
- Usuário: alguns serviços precisam de autenticação, você pode colocar um usuário e senha na URL para logar
- Host: nome do dominio ou ip do servidor
- Porta: Porta em que você está se conectando, geralmente 80 em http e 443 em https, mas pode ser hospedado em todas as portas
- Caminho: Nome do arquivo, recurso ou pasta que você tenta acessar
- Query String: Bits extra de informação enviados no caminho solicitado, por exemplo /blog?id=1, informaria ao caminho que você quer receber o artigo com o id 1
- Fragmento: referência a um local na página. Isso é usado para páginas com conteúdo longo e pode ter uma parte específica da página vinculada a ela, para ser visível para o usuário assim que acessar a página.

para fazer solicitações para um servidor web, seu computador envia dados como:

GET / HTTP/1.1
Host: instagram.com
User-Agent: Mozilla/5.0 Firefox/87.0
Referer: https://instagram.com/

1. Método de solicitação (GET para obter o conteúdo)
2. o host que você solicita
3. o Agente do usuário (navegador que você usa)
4. Referenciador, a página de onde você veio
5. Um espaço em branco para indicar o fim da solicitação

Uma resposta comum incluiria:

HTTP/1.1 200 OK
Server: nginx/1.15.8
Date: Fri, 09 Apr 2021 13:34:03 GMT
Content-Type: text/html
Content-Length: 98