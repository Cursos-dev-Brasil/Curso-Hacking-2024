# Cabeçalhos http

Cabeçalhos HTTP são informações adicionais que podem ser enviadas ao servidor ao fazer solicitações. Nenhum Header é necessário, mas alguns são importantes para funcionalidades de exibição adequada

## Headers de solicitação comuns

Host: Específica qual site o usuário deseja acessar, importante para servidores que hospedam muitos sites

user-Agent: Informa o servidor sobre o softwares do navegador e a versão, ajudando a formatar a página corretamente

content-length: Indica ao servidor a quantitade de dados que estão sendo enviados, como em um formulário, para se certificar que nada foi perdido

Accept-Encoding: Indica os métodos de compressão usados pelo navegador, permitindo que os dados sejam comprimidos e sejam transmitidos de forma eficiente

Cookies: Envia dados para ajudar o servidor a "lembrar" das informações do usuário

## Cabeçalhos de resposta comuns

Set-cookie: Informa o cliente para armazenar informações para serem reenviadas ao servidor  nas próximas sessões

Cache-Control: Indica por quanto tempo armazenar o conteúdo na resposta no cache do navegador até ate solicitar novamente

Content-Type: Informa ao cliente quais dados são retornados, como HTML, CSS, JS, Imagens, PDF, vídeos e etc... permitindo ao navegador processar os dados

Content-Encoding: Específica o Método de compressão usado para reduzir o tamanho dos dados enviados