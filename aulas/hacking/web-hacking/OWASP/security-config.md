# Configurações de segurança incorretas

Configurações de segurança incorretas são mais uma categoria de vulnerabilidades OWASP, por que acontecem quando a segurança podia ser melhor planejada mas não foi, mesmo com as versões de software mais atualizadas, uma configuração de segurança errada pode colocar a segurança dos seus dados em jogo

esse tipo de configuração inclui:

- Permissões mal configuradas em serviços em nuvem, como buckets S3.
- Ter recursos desnecessários habilitados, como serviços, páginas, contas ou privilégios.
- Contas padrão com senhas não alteradas.
- Mensagens de erro muito detalhadas que permitem aos atacantes descobrir mais sobre o sistema.
- Não usar cabeçalhos de segurança HTTP.

Essa vulnerabilidade pode dar acesso a outras, como credenciais padrão dando acesso a dados sensiveis, entidades externas XML (XXE) ou injeçõo de comandos em páginas de administração 

## Interfaces de depuração

Uma configuração de segurança incorreta comum diz respeito à exposição de recursos de depuração em software de produção. Recursos de depuração estão disponíveis em frameworks de programação para permitir que os desenvolvedores acessem funcionalidades avançadas para depurar um aplicativo enquanto está sendo desenvolvido. atacantes podem abusar de algumas funcionalidades de depuração se, de alguma forma, os desenvolvedores esquecerem de desativá-las antes de publicar seus aplicativos.

Um exemplo foi usado quando o Patreon foi hackeado em 2015. Cinco dias antes do hack, um pesquisador de segurança relatou que havia encontrado uma interface de depuração aberta para um console Werkzeug. Werkzeug é um componente vital em aplicativos web baseados em Python, por que fornece uma interface para servidores web executarem o código Python. Werkzeug inclui um console de depuração que pode ser acessado via URL em /console, ou será apresentado ao usuário se uma exceção for levantada pelo aplicativo. Em ambos os casos, o console fornece um console Python que executará qualquer código enviado a ele. Para um atacante, isso significa que ele pode executar comandos arbitrariamente.

Console Werkzeug:

w
![Console Werkzeug](/content/Werkzeug.png)


