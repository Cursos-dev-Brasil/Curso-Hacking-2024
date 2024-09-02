# Organização

algumas pessoas não conhecem a palavra organização (é sério, já vi gente colocando imagem na pasta de downloads do windows) mas se você quer entrar nessa área maravilhosa, que é o pentest, você PRECISA, ser organizado, senão você vai acabar perdendo o arquivo com as senhas da máquina que você tentou invadir (experiência própria). Mesmo que você não queira seguir carreira na IS, você precisa de organização, ninguém quer contratar um repositor de mercado desorganizado

## Estrutura de pastas

Quando você for atacar uma máquina, precisa de uma estrutura de pastas clara na máquina de ataque pra salvar informações do escopo, dados de enumeração, evidências de tentativas de exploração, dados sensíveis e até tentativas fracassadas de ataque

Isso serve pra não se perder no meio do pentest, por exemplo, a 50 minutos atrás você fez a enumeração do alvo usando [nmap](../../network/ferramentas/nmap/), você não quer ter que subir o terminal inteiro pra encontrar essa enumeração, por isso você pode simplesmente guardar os dados em um arquivo usando `nmap -oA enumeração <ip>`, esse comando vai criar 3 arquivos onde os dados da enumeração vão ser guardados, o nmap é só um exemplo do por que a documentação é importante

A estrutura de pastas padrão normalmente é assim, os nomes podem mudar, por que se nem Jesus padronizou a humanidade, por que a IS conseguiria?

```
usuárioOrganizado@root[/]$ 

Projetos/
└── Alvo do ataque
    ├── EPT (Teste de Penetração Externo/External Penetration test)
    │   ├── evidencias
    │   │   ├── credenciais
    │   │   ├── dados
    │   │   └── capturas_de_tela
    │   ├── logs
    │   ├── scans
    │   ├── escopo
    │   └── ferramentas
    └── IPT (Teste de Penetração Interno)
        ├── evidencias
        │   ├── credenciais
        │   ├── dados
        │   └── capturas_de_tela
        ├── logs
        ├── scans
        ├── escopo
        └── ferramentas
```

Em cada pasta (IPT e EPT) temos subpastas para alguns tipos de dados, scans, ferramentas, logs, informações de escopo (por exemplo uma lista de IPs para usar com a ferramenta de scan) e uma pasta de evidências, com dados recuperados, dados úteis e prints

Eu sei, pode parecer chato demais fazer isso, e as vezes é mesmo, mas mais chato que isso é ficar 45 minutos procurando seu scan no terminal que nem um idiota

O jeito que você organiza é completamente pessoa, algumas pessoas criam uma pasta pra cada host, e salvam prints nela, outras organizam por host ou rede e salvam em aplicativos de notas. Você pode testar várias estruturas até encontrar uma que você se sinta confortável

### Ferramentas de anotação

Um pentester perfeito tecnicamente mas desorganizado é simplesmente só mais um, um pentester mediano tecnicamente mas muito organizado se destaca muito mais, você com certeza não quer perder a vaga pra alguém menos capaz simplesmente por que você não gosta de criar pastas

Existem várias ferramentas para organização e criação de notas, escolher uma ferramenta é algo pessoal (acho que você entendeu que quase tudo relacionado a organização é pessoal), alguns simplesmente não precisam de um recurso que outra pessoa não consegue viver sem, algumas opções de aplicativos de notas são:

- Cherrytree
- Visual Studio Code
- Evernote
- Notion
- GitBook
- Sublime Text
- Notepad++

Você precisa garantir que qualquer dado do cliente não seja armazenado na nuvem nem fora do seu ambiente local. Não sei se você percebeu mas segurança é um pouquinho importante neessa indústria

**OBS: esse curso que eu sei que você ama é escrito em linguagem markdown, pode ser muito útil aprender ele, fica tudo muito mais bonito, confia no adm que é sucesso**

**OBS (2): Você também precisa de uma base muito sola em alguns conhecimentos básicos, por exemplo, você precisa ter alguns comandos do linux prontos na memória, pra garantir que você não passe vergonha tentando mudar de diretório (é humilhante)**

**OBS: (3): terceira observação, se você acha que o adm do curso só criou o curso e nunca mais tocou nele você tá extremamente errado, você não tem noção de quantas vezes eu volto nas minhas próprias aulas pra lembrar de um comando ou abrir algum site, esse curso começou sendo uma anotação pessoal minha e depois a ideia de fazer um curso surgiu**

Também é importante manter checklists, modelos de relatórios e ter um banco de dados de vulnerabilidades e descobertas. Esse banco de dados pode ser uma planilha do exel ou até um banco de dados mesmo, tanto faz. Ter isso faz você ficar na frente de mais da metade dos pentester e economizar um tempo gigantesco, que você gastaria repetindo pesquisa

É isso, essa aula não teve muito humor já que é um assunto mais sério (eu tava sem criatividade)