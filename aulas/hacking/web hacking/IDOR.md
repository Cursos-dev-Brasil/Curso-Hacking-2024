# Insegure Direct Object Reference (ID OR)

se refere a uma vulnerabilidade de controle de acesso onde você pode acessar recursos que normalmente seriam inacessíveis. isso acontece quando o programador expoe uma referência direta de objeto, que é um identificador que se refere a objetos específicos no servidor. Por objeto, podemos obter acesso a um arquivo, usuário, uma conta bancária ou qualquer outra coisa

## Desafio guiado retirado da Tryhackme

Vamos dizer que você quer acessar sua conta bancária e depois da autenticação, somos redirecionados para 
[Essa URL](https:// bank.thm/account?id=111111)