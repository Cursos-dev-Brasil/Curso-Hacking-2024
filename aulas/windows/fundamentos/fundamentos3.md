# Fundamentos windows pt 3

Continuação [Fundamentos windows pt 2](fundamentos2.md)

# Computer management 

Ainda nas ferramentas do MSConfig a gente tem a computer management (compmgmt). Com 3 seções principais, System tools, storage e Services and applications

## System Tools

### Tarefas agendadas

Começando pelas tarefas agendadas (task scheduler), é basicamente as contrabs do windows, você pode criar e gerenciar tarefas comuns ou repetitivas de tempos em tempos (Normalmente é um bom lugar pra implantar malwares)

### visualizador de eventos

O visualizador de eventos (Event viewer) permite que você veja os eventos que aconteceram no pc. A gravação desses eventos é basicamente uma trilha usada para entender o que aconteceu no pc. É muito usado em análise forense para detecção de atividade suspeita (me senti muito inteligente escrevendo essa frase)

O event viewer tem 3 painéis


1. O painel da esquerda te fornece uma lista (hierárquica) dos provedores de log (de evento).

![](/content/eventViewer.png)

2. O painel no meio exibi uma overview e um resumo de eventos de um provedor.
3. O painel da direita é o painel de ações.


![](/content/eventRegistryTable.png)

![](/content/eventRegistryLog.png)

## Pastas compartilhadas

Pastas compartilhadas (shared folders) são pastas onde arquivos e listas podem ser compartilhadas e acessadas por qualquer um

![](/content/sharedFile.png)

A pasta de compartilhamento padrão do windows é a C$ e o compartilhamento de administração remota padrão é o ADMIN$

Se você clicar com o botão direito em qualquer pasta e clicar em propriedades, pode ter informações úteis, como quem pode acessar o recurso compartilhado ou o dono do compartilhamento
