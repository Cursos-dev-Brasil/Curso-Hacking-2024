# NetCat

É uma ferramenta usada pra interagir com portas. o uso principal em pentests é conectar shells (calma, vamo chegar nessa parte apressado)

Ele pode ser usado para se conectar com qualquer porta, e interagir com o serviço rodando na porta. por exemplo: O SSH é programado pra funcionar na porta 22 e enviar todos os dados e chaves, você pode se conectar a porta 22 no netcat assim:

`Klython@root[/~]$ netcat 10.10.10.10 22`

quando você faz isso o SSH responde com o banner dele:

`SSH-2.0-OpenSSH_8.4p1 Debian-3`

Isso se chama banner grabbing, ajuda a identificar o que tá rodando em qual porta, o netcat tem um primo de 3° grau, o PowerCat, ele roda no windows por que pra variar o windows não tem o netcat instalado (nem o powercat)

O netcat pode ser usado pra transferir arquivos, mas como tudo na vida, o netcat tem um primo melhor que ele, o socat. Ele tem alguns recursos que o netcat não tem, como transformar um shell em um TTY (lê-se: Gambiarra pra funcionar mais bonitinho) ou redirecionar portas. Em resumo é aquela carta que todo pentester precisa ter no pendrive

# Banner grabbing

Sabe quando você tá andando no centro da cidade e tem muita gente com planfetos de vários tipos de serviços? Um banner é isso, se você usar o netcat em uma porta especifica, ele entra em contato com essa porta e caso ela esteja aberta ela vai retornar um "cartão de visitas" pro netcat

`nc -nv 10.129.42.253 21`

saída:

`220 (vsFTPd 3.0.3)`
