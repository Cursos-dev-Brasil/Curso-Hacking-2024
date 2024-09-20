# Redefinição de senha insegura

Um bom exemplo dessas vulnerabilidades aconteceu no Instagram há um tempo. O Instagram permitia que os usuários redefinissem as senhas enviando um código de 6 dígitos para seus números de celular via SMS para validação. Se um atacante quisesse acessar a conta de uma vítima, ele poderia tentar forçar o código de 6 dígitos. Como esperado, isso não era diretamente possível, por que o Instagram tinha uma limitação de taxa implementada para que, após 250 tentativas, o usuário fosse bloqueado de tentar novamente.

Mas, foi descoberto que a limitação só se aplicava a tentativas feitas a partir do mesmo IP. Se um atacante tivesse vários endereços IP diferentes de onde enviar solicitações, ele poderia tentar 250 códigos por IP. Para um código de 6 dígitos, existem um milhão de possíveis combinações, então um atacante precisaria de 1000000/250 = 4000 IPs para cobrir todos os códigos possíveis. Isso pode parecer uma quantidade insana de IPs para ter, mas os serviços em nuvem tornam fácil obtê-los a um custo relativamente baixo, tornando esse ataque viável.

![Vulnerabilidade do instagram](/content/instagram-vuln.png)
a vulnerabilidade é relacionada a ideia de que nenhum usuário seria capaz de usar mais de 1 ip. O problema é no design, e não na implementação

Como esse tipo de vulnerabilidade costuma estar em uma fase muito inicial do desenvolvimento, frequentemente você precisaria reconstruir a parte afetada do zero, e é mais difícil do que qualquer outra relacionada a código. A melhor opção para evitar essa vulnerabilidade seria realizar a modelagem de ameaças desde o inicio do desenvolvimento,

