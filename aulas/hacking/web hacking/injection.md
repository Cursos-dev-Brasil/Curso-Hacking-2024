# Injeção

Falhas de injeção são muito comuns em aplicações. Elas ocorrem quando a aplicação interpreta a entrada do usuário como comandos ou parâmetros. esse tipo de ataque depende de tecnologias utilizadas e de como essas tecnologias interpretam a entrada

- SQL Injection: Isso acontece quando a entrada do usuário é tratada commo um comando SQL para manipular o resultado, isso pode permitir acesso, modificação e exclusão de informações do banco de dados, como detalhes e credenciais

- Command injection: Acontece quando a entrada é interpretada como um comando do sistema, então o atacante poderia executar comandos arbitrário do sistema do servidor, potencialmente permitindo acesso ao sistema


A principal defesa para esse ataque é garantir que entradas SQL e de comandos do sistema sejam interpretados como texto comum, você pode fazer isso de várias formas:

- Usando uma lista de permissões (allow list): Quando a entrada é enviada para o servidor, a entrada é comparada com uma lista de entradas e caracteres seguros, caso a entrada seja marcada como segura, ela segue com o processamento, caso contrário ela é removida e o sistema emite um erro

- Remover entradas suspeitas: Se a entrada tiver caracteres potencialmente prejudiciais, eles são removidos sem o processamento

Caracteres são considerados perigosos/prejudiciais são classificados como qualquer coisa que possa alterar o processamento dos dados