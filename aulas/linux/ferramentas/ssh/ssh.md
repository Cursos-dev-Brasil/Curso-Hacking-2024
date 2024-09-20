# Secure shell

O SSH é um protocolo de rede que roda na porta 22, ele é um jeito seguro de se conectar a um pc remotamente (Se fosse seguro não estaria no curso mas tudo bem). É como se você invadisse a sua própria casa usando uma chave mestra ao invés de arrombar a porta. Ele normalmente é configurado por senha ou por chaves públicas e privadas (se você tiver neurônios pra configurar isso) 

Aula sobre chaves públicas e privadas(Criptografia no geral) [aqui](/aulas/CyberSec/criptografia.md)

O SSH é aquele amigo multi-tarefas que todo mundo adora, você pode acessar sistemas na mesma rede, pela internet, usando port Forwarding (como se você saisse abrindo a porta de todo mundo na sua rua) e fazer upload (Ou até baixar) arquivos, ele funciona em sistema cliente-servidor, com um usuário com o cliente, por exemplo o OpenSSH e um servidor ssh

Enquanto você ataca (ou faz uma avaliação), você consegue uma chave privada ou credenciais em texto claro (plaintext) que podem ser usadas pra se conectar num sistema SSH. Se conectar num sistema SSH é tipo trocar de internet wi-fi pra eth0, é mais estável que um reverse shell e pode ser usado como uma ponte pra atacar outros hosts, transferir ferramentas e etc. 

```
Klython@root[/~]$ ssh Bob@10.10.10.10

Bob@remotehost's password: 

Bob@remotehost#
```

Bob é só um exemplo, mas se seu nome for Bob... Qualquer coincidência é mera conhecidência. Também da pra ler chaves privadas locais de um sistema comprometido ou adicionar a sua pública para ter acesso ao servidor SSH 
