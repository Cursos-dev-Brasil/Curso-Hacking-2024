# Cookies

Cookies são pedaços de dados no seu computador. cookies são salvos quando você recebe o Header "set-cookie" de um servidor de resposta. Em cada solicitação, você envia os Cookies de volta ao servidor. Como o HTTP é Stateless, os Cookies podem ser usados para  lembrar o servidor de quem você é, algumas configurações pessoais ou se você já visitou o site

Os cookies são usados para muitos propósitos, mas são muito usados para autenticação de sites. O valor do cookie geralmente não será uma string de texto onde você pode ver a senha, mas um token (código único que não é adivinhavel por humanos).

# vendo Seus Cookies

Você pode visualizar quais cookies seu navegador está enviando para um site usando as ferramentas de desenvolvedor do navegador. Se você não sabe como acessar as ferramentas de desenvolvedor: no Chrome, clique nos três pontos no lado direito superior, depois em mais ferramentas, depois em ferramentas de desenvolvedor

com as ferramentas de desenvolvedor abertas, clique na aba "Network/rede". Essa aba mostra uma lista de recursos que seu navegador solicitou. Você pode clicar em cada um para receber uma descrição detalhada da solicitação e resposta. Se seu navegador enviou um cookie, você verá isso na aba "Cookies" da solicitação. 