## Código de status

Códigos de status HTTP informam ao cliente o resultado da requisição e como lidar com ela. Códigos de status podem ser classificados em 5 categorias

1. 100-199 Informações - indicam que a primeira parte da solicitação foi a eita e o cliente deve continuar enviando o restante, não são muito comuns

2. 200-299 Sucesso - informam que a solicitação foi bem sucedida

3. 300-399 Redirecionamento - Informam que o cliente foi redirecionado para outra página

4. 400-499 Erro do cliente - informam que houve um problema com a solicitação do cliente

5. 500-599 Erro do servidor - informam que houve um problema com o servidor

Códigos de status comuns:

- 200 - OK: Solicitação concluída 

- 201 - Created: um recurso foi criado (por exemplo um usuário)

- 301 - Moved permanently: redireciona Para uma nova página permanente

- 302 - Found: Faz um Redirecionamento temporário

- 403 - Forbidden: indica que o cliente não tem permissão para acessar o recurso

- 404 - Page not found: Indica que a solicitação que o cliente fez não existe

- 405 - Method Not Allowed: Indica que o Método de solicitação não é autorizado pelo recurso solicitado

- 500 - Internal Server Error: O servidor um erro ao processar a solicitação 