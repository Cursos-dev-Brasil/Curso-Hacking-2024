# Pesquisa de vulnerabilidades
no Hacking, Quase sempre você vai encontrar aplicativos ou softwares abertos a uma possível exploração de vulnerabilidades

Por exemplo, Content Management Systems (sistemas de gerenciamento de conteúdo ou CMS), como o wordpress, FuelCMS, Ghost e etc... São usados para facilitar a configuração de um site e todos esses são vulneráveis a ataques por meio de exploits

Para encontrar uma vulnerabilidade em um sistema, você pode procurar em alguns bancos de dados de vulnerabilidades

- ExploitDB
- NVD
- CVE Mitre

o ExploitDB costuma ser útil para hackers, por que contém exploits que podem ser baixados e usados imediatamente. Costuma ser uma das primeiras paradas quando você encontra um software potencialmente vulnerável

o NVD (National Vulnerability Database) acompanha as CVE's (Common Vulnerabilities and Exposures) é um lugar bom para procurar vulnerabilidades em um software especifico. O formato de um CVE é: **CVE-ano-número**

Se você prefere usar a CLI no linux, o Kali vem pré-instalado com a ferramenta *searchsploit*, que permite pesquisar exploits no ExploitDB a partir da própria máquina, de forma offline e usando uma versão baixada do banco de dados, uma desvantagem disso é que talvez o DB não esteja atualizado

Vamos supor que você está fazendo um pentest e descobriu esse site: <br>
![FuelCMS](/content/fuelCMS.png)

Claramente isso é um site feito usando o fuelCMS, nunca vai ser tão óbvio

Use algum dos DB anteriores para procurar por um exploit 

Se você tiver chegado em uma saída parecida com essa: 
![exploitDB](/content/exploitDB.png)

Você encontrou as vulnerabilidades

**Nota: Os CVE's são atribuidos de acordo com a *data* da descoberta, não quando são publicadas, se uma vulnerabilidade for descoberta no fim do ano, ou se o processo de confirmação e correção levar muito tempo, a data de lançamento pode ser no ano seguinte do ano da descoberta**