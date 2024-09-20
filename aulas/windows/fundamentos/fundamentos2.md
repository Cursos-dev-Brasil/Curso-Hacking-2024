# Pentest e análise forense no Windows

Continuação [Fundamentos windows pt 1](fundamentos1.md)

Ok, agora que você já sabe o basicão do windows a gente vai entrar numa área um pouco mais divertida do sistema, por mais que eu odeie o windows (deixei isso claro na aula passada) ele é um sistema bem... útil (não acredito que eu disse isso)

Se você trabalhar em uma empresa onde o windows sofreu um ataque por exemplo, o windows de certa forma facilitaria todo o trabalho da análise forense pra pegar o meliante

## Desktop

Não tem muito o que falar do desktop, é aquela tela que aparece

![](/content/windowsDesktop.png)

Tem gente que deixa a Desktop de qualquer jeito, sem se importar nenhum pouco com a organização do ambiente. Poxa, se você quer ter um sistema ruim e caro pelo menos cuida bem do bixinho

![](/content/windowsDesktop2.png)

No exemplo acima (Se você olhar pra isso por muito tempo vai começar a sentir dor nos olhos, cuidado) essa Desktop tem um pouco de tudo, pasta, atalho, arquivo, script, imagem, documento, tudo o que você quiser

## Sistema de arquivos do Windows

Até que o sistema de arquivos do windows é bem feito (mentira, é bem desorganizado na verdade), mas dá pra aguentar

- Unidade C: Por padrão o windows é instalado nela, a maioria dos arquivos e programas ficam lá

- Pastas e arquivos: Não tem muito o que falar

## Controle de conta do usuário (UAC)

Nesse ponto eu preciso elogiar o windows (meu Deus, o que eu tô dizendo) o UAC é aquele pop-up que aparece sempre que você quer baixar alguma coisa, principalmente se essa coisa fizer alterações importantes no pc, por exemplo alterações na pasta Program files ou na Program files (x86)

Essa tela aparece quando o windows pede sua permissão pra instalar ou executar um app que pode afetar o sistema. Se você confiar na origem do arquivo é só permitir

![](/content/UAC.png)

O UAC seria uma boa camada de segurança extra ao windows, mas o problema é que o sistema tem muitas vulnerabilidades e muitas vezes o UAC nem influencia na invasão


## Painel de controle

O painel de controle é literalmente um painel de controle, lá você controlava todas as configurações do sistema antes do app Configurações

Ele pode ser usado pra personalizar a aparência do sistema, adicionar impressoras ou configurar redes, sinceramente hoje ele é meio inútil (parece o windows)

![](/content/controlPanel.png)

### Configurações

No windows 10, o painel de controle foi praticamente aposentado com a chegada das configurações, tudo que você podia fazer no painel de controle pode ser feito nas configurações, ele ainda existe (provavelmente a equipe de devs do windows tava com preguiça de tirar) mas ninguém usa

![](/content/config.png)

## Gerenciador de tarefas

O gerenciador de tarefas é um fiscal de programas, ele te lista todos os programas/arquivos em execução no sistema e te detalha exatamente o RAM, CPU e etc que esse programa consome (não, não é exatamente)

![](/content/taskManager.png)

## MSConfig 

O MSConfig (System configuration) é um tipo de solução de problemas avançados, ele é útil pra diagnosticar problemas (wow, que surpresa)

![](/content/msconfig.png)

**OBS: Pra acessar o msconfig você precisa de privilégios de administrador (root no linux)**

O msConfig tem 5 abas importantes (são as únicas abas)

1. general - geral: Selecionar dispositivos ou serviços pra carregar na inicialização
2. boot: Definir as opções de inicialização do sistema
3. services - Serviços: Lista todos os serviços configurados, independente do estado (running ou stopped). Um serviço é uma aplicação que roda em segundo plano
4. startup - Inicialização:  a Microsoft aconselha usar o taskmgr para gerenciar (habilitar/desabilitar) itens de inicialização. O utilitário de Configuração do Sistema NÃO é um programa de gerenciamento de inicialização.
5. tools - Ferramentas: A aba tools tem algumas coisas para configurar sistema. Cada ferramenta da aba tem uma descrição rápida


![geral](/content/msconfigTabsGeneral.png)
![Boot](/content/msconfigTabsBoot.png)
![Services](/content/msconfigTabsService.png)
![Startup](/content/msconfigTabsStartup.png)
![Tools](/content/msconfigTabsTools.png)


--- 

Ainda nas ferramentas, as configurações de UAC podem ser alteradas ou desligadas (Não recomendado)

![](/content/changeUAC.png)

