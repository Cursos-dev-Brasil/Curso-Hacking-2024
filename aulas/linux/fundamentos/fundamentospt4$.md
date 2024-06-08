# fundamentos Linux parte 4

## gerenciamento de pacotes

Quando desenvolvedores criam um software para a comunidade, eles colocam em um repositório padrão Linux chamado "apt", se aprovado, o conteúdo é liberado para instalação com o comando `apt install [serviço]`

o comando apt faz parte de um conjunto de ferramentas Linux chamado apt, o apt permite instalar ou remover softwares e fontes

você pode instalar e remover repositórios com o comando `dpkg` o apt sempre é atualizado com novos repositórios, então acaba sendo uma ótima opção

para adicionar um repositório usamos o comando `add-apt-repository` ou adicionamos manualmente
1. 
```
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
```
2.
```
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
```
3.
`sudo apt update`
4.
`sudo apt install sublime-text`

para remover repositórios use:
```
sudo add-apt-repository --remove ppa:PPA_Name/ppa
sudo apt remove sublime-text
```

## logs
logs sao arquivos essenciais para a manutenção do sistema, e contém informações como erros, avisos, verificações de funcionamento e etc. Os arquivos de log naturalmente ficam no diretório /var/log onde essed arquivos e pastas tem informações de registro para serviços e softwares. O Linux é muito eficiente na questão de automação desses logs, usando o processo de *rotação*

### exemplos de logs

1. servidor web apache
	- access log: contém informações sobre todas as solicitações de um servidor, localizado em /var/log/apache2/access.log
 - error log: contém informações sobre erros de um servidor, localizado em /var/log/apache2/error.log
2. fail2ban
 - fail to ban log: informações sobre atividades suspeitas no Linux, como tentativas de brute force, localizado no em /var/log/fail2ban.log
3. UFW
- UFW (uncomplicated firewall): Registra atividades de firewall, como tentativas de bloqueio de conexão, localizado em /var/log/ufw.log

### Importância de logs:
os logs são importantes para:
- Monitoramento de saúde do sistema
- identificação de problemas de desempenho ou falha de sistemas
- segurança 
- auditoria 

### Tipos de logs comuns

1. error.log
- log normalmente usado para diagnosticar erros e falhas em softwares, crucial para diagnosticar e resolver problemas no software ou dependências

2. access.log
- log usado para armazenar informações sobre solicitações,  como IP do cliente, data e hora da solicitação e recurso solicitado

## logs do sistema operacional
- além dos logs de serviço software, existem os logs do sistema operacional que, servem para diagnosticar e garantir a saúde do kernau e dos arquivos e pastas do sistema.

o caminho dos logs do sistema é: **/var/log/syslog/**
além do arquivo: **/var/log/Auth.log** que salva todas as tentativas de autenticação, bem e mal sucedidas