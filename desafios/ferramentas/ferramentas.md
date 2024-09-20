# Desafio ferramentas de rede
**Desafio referente as aulas [ferramentas de rede](/aulas/network/ferramentas/)**

## **Desafio 1**:

- ### *Ping*
Execute o comando ping no endereço google.com, a flag é a saída do comando
O formato da flag é: xxxx:xxx:xxxx:xxx::xxxx:

- ### *Traceroute / Tracert*

Esse desafio vai funcionar de uma maneira diferente. Já que o traceroute é um comando de rastreamento, não existe um caminho fixo, ou seja, cada IP poderá ter uma saída diferente, dependendo da sua geo-localização até seu provedor de internet.

Portanto, não vamos usar o formato de flags padrão. Nesse desafio, nossa flag será toda saída do comando, ou seja: 

```
Disparando google.com [172.217.29.142] com 32 bytes de dados:
Resposta de 172.217.29.142: bytes=32 tempo=22ms TTL=57
Resposta de 172.217.29.142: bytes=32 tempo=19ms TTL=57
Resposta de 172.217.29.142: bytes=32 tempo=23ms TTL=57
Resposta de 172.217.29.142: bytes=32 tempo=23ms TTL=57

Estatísticas do Ping para 172.217.29.142:
    Pacotes: Enviados = 4, Recebidos = 4, Perdidos = 0 (0% de
             perda),
Aproximar um número redondo de vezes em milissegundos:
    Mínimo = 19ms, Máximo = 23ms, Média = 21ms
```

essa saída deve ser alterada pela saída exata do comando no seu dispositivo

- ### *Who-is*

Nesse desafio você precisará das respostas para as perguntas:

Domain name
Registry Domain ID
Creation Date
Name server (2)

Todas as respostas estão presentes no comando usando a CLI

- ### *nmap*

como o nmap possui vários tipos de escaneamentos, esse desafio terá duas "partes":


a resposta deve conter:

Quantidade de portas abertas
Número das portas tcp abertas
Número de portas filtradas
tipo de programa rodando (web, servidor, software...) 

realize um scan padrão no dominio *discord.com*
realize um scan padrão no IP *8.8.8.8*

obs: vamos estudar scans udp na prática mais pra frente
