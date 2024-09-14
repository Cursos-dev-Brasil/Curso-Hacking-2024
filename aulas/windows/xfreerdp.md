# xfreerdp

A execução de código remoto é cada vez mais usada em sistemas, ela é muito usada por empresas e adivinha? Essas empresas potencialmente usam windows. E adivinha denovo? É Mais fácil invadir um Windows que uma batata. O xfreerdp serve para acessar uma máquina windows remotamente através de um Unix-like.

## FreeRDP

FreeRDP é uma implementação de código aberto do Remote Desktop protocol(RDP) da Microsoft (eca). o xfreeRDP é a CLI do freeRDP, basicamente é um jeito gratuito de conectar seu linux a um windows

### Comando básico do xfreerdp

1. comando base
`$ xfreerdp [options] <servidor>`

2. Credenciais básicas
`$ xfreerdp /u:usuario /p:senha /v:servidor`

3. Redirecionamento de Área de transferência e Impressoras

`$ xfreerdp /u:usuario /p:senha /v:servidor /clipboard /printer`

- `/clipboard`: habilita a transferência da área de transferências
- `/printer`: Redireciona impressoras do cliente para o servidor , isso significa que tudo que você imprimir na máquina virtual vai ser redirecionado para a impressora no seu pc local

4. Conectar com resolução personalizada

`$ xfreerdp /u:usuario /p:senha /v:servidor /size:1920x1080`

- `/size`: Resolução da tela remota

5. Conectar ignorando certificados
`$ xfreerdp /u:usuario /p:senha /v:servidor /cert:ignore`

- `/cert:ignore`: Controla o comportamento do xfreerdp em relação a certificados SSL/TLS. É útil quando o servidor remoto usa um certificado auto-assinado ou não confiável

`xfreerdp /u:usuario /p:senha /v:servidor /cert:accept`  

- `/cert:accept`: aceita o certificado sem verificar a validade mas não ignora os erros de certificado


