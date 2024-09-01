# Fundamentos Linux Parte 4

## Gerenciamento de Pacotes

Imagina que o Linux é um buffet de softwares e o apt é o garçom que traz o que você pediu. Quando um dev cria um software, ele coloca em um repositório padrão, no caso o `apt`. Se o software é aprovado, você instala ele com um comando de 3 palavras:  `apt install [serviço]`. É tipo pedir pizza por telefone, mas sem a espera de 30 minutos (ou 90 se for sexta-feira à noite).

O apt é parte do Advanced Package Tool, que é um conjunto de ferramentas que transforma a instalação e remoção de softwares em algo sem um arquivo com a opção .msi que faz o que ele quiser no seu pc e você nem sabe disso. Pra adicionar um repositório, você pode usar o comando add-apt-repository ou fazer isso manualmente, se você gostar de um pouco de aventura e sofrimento.

`sudo apt install sublime-text`
Se você precisar remover um repositório, pode fazer isso muito rápido:

```
sudo add-apt-repository --remove ppa:PPA_Name/ppa
sudo apt remove sublime-text
```

## Logs
Logs são quase cadernos do seu sistema, onde ele anota tudo o que acontece. Desde errinhos que te fazem coçar a cabeça (ou perder 200 reais em um psicólogo) até avisos sobre a vida do servidor, os logs estão lá para garantir que você não passe vergonha em uma apresentação de TI.

### Exemplos de Logs

#### Servidor Web Apache

access.log: Registra todas as solicitações ao servidor, tipo uma lista de quem entrou numa festa. Localizado em `/var/log/apache2/access.log`.

error.log: Onde o servidor desabafa sobre seus problemas, como um diário de um adolescente. Procure ele em `/var/log/apache2/error.log`.

#### Fail2ban
fail2ban.log: Mantém um olho em atividades suspeitas, como se fosse o segurança chato da balada. fica em `/var/log/fail2ban.log.`

#### UFW (Uncomplicated Firewall)

ufw.log: Registra atividades de firewall, como uma câmera de segurança no seu sistema. Localize-o em `/var/log/ufw.log.`

### Importância dos Logs

Os logs são importantes para:

Monitorar a saúde do sistema, como um exame de rotina no médico (que eu sei que você não faz).
Identificar problemas de desempenho ou falhas (para evitar aqueles momentos embaraçosos).
Garantir a segurança (porque você não quer que estranhos entrem na sua festa).
Realizar auditorias e manter um histórico das atividades (como uma linha do tempo das suas aventuras).

#### Tipos de Logs Comuns

##### error.log

O log onde você vai quando precisa de dicas sobre como resolver problemas e erros. Ele é crucial para diagnosticar e resolver problemas – o Sherlock Holmes dos logs.

##### access.log

Armazena informações sobre solicitações, como um livro de visitas. Contém o IP do cliente, data e hora da solicitação e o recurso solicitado – perfeito para saber quem apareceu na sua festa e quando.

##### Logs do Sistema Operacional

Além dos logs dos serviços, o sistema operacional tem seus registros para garantir que tudo esteja funcionando. É como uma folha de acompanhamento para garantir que o motor do carro esteja funcionando.

`/var/log/syslog/`: Onde o sistema registra suas atividades, como uma página de diário que mantém tudo em ordem.

`/var/log/auth.log`: Registra todas as tentativas de autenticação, tanto as que passaram quanto as que falharam – o detector de mentiras do seu sistema.



