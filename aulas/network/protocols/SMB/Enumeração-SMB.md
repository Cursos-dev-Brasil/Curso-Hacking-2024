# Enumeração

Nesse ponto do curso, você já deve saber o que é a enumeração e para o que ela serve, resumindo é o processo de coleta de informações para auxilio em ataques

A Enumeração é essencial para um ataque bem-sucedido, já que perder tempo com explorações que podem travar o sistema pode ser um grande disperdício, ela é usada para coleta de usernames, senhas, informações de redes, nomes de hosts, dados, serviços e qualquer outra informação útil para um ataque em potencial

# Smb

Normalmente, existem **unidades de compartilhamento SMB** que podem ser **conectadas e usadas** para **visualizar ou transferir arquivos**. O SMB é um ótimo ponto de partida para um invasor que procura informações confidenciais (Você ficaria surpreso com o que pode ser incluído em um compartilhamento)

## Port Scanning

O primeiro passo da enumeração é o port scanning, temos uma aula De enumeração usando Nmap [aqui](../ferramentas/nmap/)

## Enum4Linux

Enum4linux é uma **ferramenta usada para enumerar compartilhamentos smb** em sistemas linux e windows, é basicamente um wrapper das ferramentas no pacote Samba e facilita a extração de informações do alvo. para instalar o Enum4linux você pode usar o [Github](https://github.com/CiscoCXSecurity/enum4linux)

A sintaxe é simples: `enum4linux [options] ip`

flags:

-U obtém lista de usuários
-M obtém lista de máquinas
-N obtém dump da lista de nomes (diferente de -U e -M)
-S obtém lista de compartilhamento
-P obtém informações de política de senha
-G obtém lista de grupos e membros
-a todos os itens acima (enumeração básica completa) 

