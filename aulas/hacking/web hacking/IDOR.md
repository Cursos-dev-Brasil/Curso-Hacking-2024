# Insegure Direct Object Reference (ID OR)

se refere a uma vulnerabilidade de controle de acesso onde você pode acessar recursos que normalmente seriam inacessíveis. isso acontece quando o programador expoe uma referência direta de objeto, que é um identificador que se refere a objetos específicos no servidor.

Exemplo: estamos acessando nossa conta bancária e, após autenticar, somos redirecionados para uma URL como essa: https://nu.bank/account?id=111111. nessa página, vamos supor que podemos ver todos os nossos detalhes bancários importantes, e um usuário faria o que precisasse fazer e seguiria em frente, achando que não há nada de errado.

Mas baseado no seu conhecimento até agora, oque você acha que pode ser explorado nessa situação?
