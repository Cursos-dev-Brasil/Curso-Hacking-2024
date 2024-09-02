# Começando com uma distro de pentest

**OBS: essa aula é baseada na room [getting started](https://academy.hackthebox.com/module/77/section/722) da hack the box, portanto as imagens e referências vão ser retiradas de lá

Se você tá começando agora no mundo dos terminais coloridos com um monte de texto em inglês você precisa estar bem equipado pra isso, o começo pode parecer muito assustador (muito mesmo), mas a sensação de conseguir completar um misero ctf é única

## Escolhendo a distro, o que usar e quando?

Trate as distribuições linux como variantes de uma só, basicamente a primeira foi criada e a partir do código fonte dela foram criadas outras, com funcionalidades e focos diferentes, é aquela famosa história do "nada se cria, tudo se copia" ou até do "o mito cria e o lixo copia", mas isso não vem ao caso

- ParrotOS (a máquina que roda na hack the box, logo nossa aula será voltada para ela)
- Kali linux (É tipo o primo famoso do parrot, os dois sempre brigam no natal pra ver quem é melhor)
- BackBox (O irmão do meio, ele é bom mas pouca gente usa, o foco dele tá na análise forense)

Você pode até criar a sua distribuição própria, mas na volta a gente faz isso, por agora vamos usar o parrot mesmo

![](/content/parrotOS.png)

## Configurando o ParrotOS

Agora que a gente sabe qual distro usar, a gente precisa configurar ela, não é só ligar e usar

Existem 3 maneiras de baixar um sistema operacional na sua máquina

- Instalação completa: Você usa um pendrive qualquer pra instalar a distro diretamente no pc

- Dual boot: Você alterna entre 2 sistemas, é útil pra quem precisa de um linux mas também precisa de outro sistema

- Virtualização: A maioria dos pentesters usa essa opção, é tipo um esconderijo secreto no seu computador, onde você pode executar várias máquinas virtuais sem mexer no sistema principal

### Opções de virtualização

No nosso caso a gente vai usar a virtualização, por que é a mais comum e é o que foi usada na htb

- Hyper-V: Para os fãs do sistema azul, é nativo do sistema, mas como qualquer coisa nele, precisa ser configurada

- VirtualBox: É de graça, funciona direito em qualquer sistema e é a escolha favorita dos iniciantes e experientes

- VMWare Workstation Player: Pra ser sincero nem sei por que isso existe, serve pra vc gastar dinheiro com 2 funções a mais e é mais difícil que a VB

- VMWare Workstation: Esse tá no meio termo, é pago mas funciona bem

Esses softwares maravilhosos que transformam seu pc em uma segunda máquina são chamados de hypervisores, os hipervisores foram criados para que você possa criar e gerenciar ambientes virtuais no seu pc, sem interferir na arquitetura atual, um hipervisor executa uma vm em um espaço isolado do seu pc, é como se você dividisse seu hd pra usar a vm em uma parte menor, e o sistema primário em uma parte maior

### Criando a VM

Depois de escolher a vm você vai criar ela (isso é óbvio), o parrotOS tem dois métodos de instalação:

- ISO: É tipo fazer uma receita do zero. Você baixa o sistema no início e personaliza como quiser. É bom pra quem quer se sentir o Deus do seu sistema

- OVA: mais prática e rápida, tipo pedir uma pizza. Vem pré-configurada com as configurações necessárias (do ponto de vista do fornecedor)

### Ajuda

Depois de instalar e iniciar a vm, talvez você se sinta meio perdido, principalmente se você veio do sistema do capiroto, caso você tenha qualquer dúvida sobre o OS, você pode usar a documentação oficial. O parrot tem documentação, o kali também, o ubuntu também. Resumindo, geral tem uma doc, prontinha pra você tentar ler (quando você começar vai entender o tentar)

