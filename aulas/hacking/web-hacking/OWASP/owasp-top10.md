# OWASP
Essa aula detalha cada tópico OWASP e inclui informações sobre vulnerabilidades, como ocorrem e como explorá-las.

- Controle de Acesso Quebrado
- Falhas Criptográficas
- Injeção
- Design Inseguro
- Configuração de Segurança Incorreta
- Componentes Vulneráveis e Desatualizados
- Falhas na Identificação e Autenticação
- Falhas na Integridade de Software e Dados
- Falhas no Registro e Monitoramento de Segurança
- Falsificação de Solicitação do Lado do Servidor (SSRF)

## Controle de acesso

algumas paginas são protegidas de acesso de visitantes comuns, vamos usar a página /wp-admin do WordPress, só o admin poderia ter acesso a essa página, e caso um usuário comum consiga acesso não autorizado, o controle de acesso está quebrado

caso um usuário obtenha acesso a página /wp-admin ele pode:

- visualizar informações sensíveis dos usuários 
- acessar funcionalidades não autorizadas, como edição de conteúdo 

A quebra do Controle de Acesso, em resumo, permite que o atacante ignore qualquer configurações de autenticidade.

Em 2019, uma vulnerabilidade foi encontrada, na qual era possível obter qualquer frame de um vídeo no YouTube marcado como privado. O pesquisador que encontrou a vulnerabilidade, mostrou que era possível pegar frame por frame e reconstruir o vídeo. Como um vídeo privado não deveria ser visto por ninguém além dele mesmo, essa vulnerabilidade foi aceita como uma vulnerabilidade de controle de acesso


