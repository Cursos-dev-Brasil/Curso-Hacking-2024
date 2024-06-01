# Falhas na Integridade de Software

Suponha que você tenha um site que utilize bibliotecas armazenadas em servidores externos fora do seu controle. Embora isso possa parecer estranho, é uma prática comum. Tome como exemplo o jQuery, uma biblioteca JavaScript muito usada. Se quiser, pode incluir o jQuery em seu site diretamente dos servidores sem baixá-lo, incluindo a seguinte linha no código HTML do seu site:

`<script src="https://code.jquery.com/jquery-3.6.1.min.js"></script>`

Quando o usuário acessa o site, o navegador dele baixa aa biblioteca diretamente da fonte externa

O problema é que se um atacante hackear o repositório oficial do jQuery, ele pode alterar o conteúdo de https://code.jquery.com/jquery-3.6.1.min.js para injetar código. Como resultado, qualquer pessoa que visite seu site baixa o código e o executa em seus navegadores sem saber. Isso é uma falha na integridade de software, pois seu site não faz verificações contra a biblioteca de terceiros para ver se ela foi alterada. Navegadores modernos permitem que você especifique um hash junto com a URL da biblioteca para que o código da biblioteca seja executado apenas se o hash do arquivo baixado corresponder ao valor esperado. Esse mecanismo de segurança é chamado de Integridade de Sub-Recursos (SRI), e você pode ler mais sobre isso aqui.

A maneira correta de inserir a biblioteca em seu código HTML seria usar o SRI e incluir um hash de integridade, se de alguma forma um atacante conseguir modificar a biblioteca, nenhum cliente que navegue pelo site execute a versão modificada. Veja como isso deve ficar no HTML

