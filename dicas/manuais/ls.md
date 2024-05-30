# Manual do comando `ls` para Leigos

**Uso:** `ls [OPÇÃO]... [ARQUIVO]...`  
Lista informações sobre os ARQUIVOS (o diretório atual por padrão).  
Ordena as entradas alfabeticamente se nenhuma opção de ordenação for especificada.

## Opções Comuns

- `-a, --all`  
  Mostra todos os arquivos, incluindo os ocultos (aqueles que começam com `.`).

- `-A, --almost-all`  
  Mostra quase todos os arquivos, mas exclui `.` (ponto) e `..` (ponto duplo).

- `--author`  
  Mostra o autor de cada arquivo (usado com `-l`).

- `-b, --escape`  
  Mostra caracteres especiais como sequências de escape (por exemplo, `\n` para nova linha).

- `--block-size=TAMANHO`  
  Ajusta o tamanho da unidade de medida dos arquivos (exemplo: `--block-size=M` para megabytes).

- `-B, --ignore-backups`  
  Ignora arquivos de backup (aqueles que terminam com `~`).

- `-c`  
  Ordena e mostra arquivos por tempo de modificação de status (usado com `-lt`).

- `-C`  
  Lista os arquivos em colunas.

- `--color[=QUANDO]`  
  Coloriza a saída (por exemplo, `--color=auto` para colorir somente se a saída estiver em um terminal).

- `-d, --directory`  
  Lista apenas os diretórios, não os arquivos dentro deles.

- `-D, --dired`  
  Formata a saída para ser usada no modo `dired` do Emacs.

- `-f`  
  Mostra todos os arquivos na ordem do diretório, sem ordenar.

- `-F, --classify[=QUANDO]`  
  Adiciona um indicador aos arquivos (por exemplo, `/` para diretórios).

- `--file-type`  
  Adiciona um indicador de tipo de arquivo, mas não adiciona `*`.

- `--format=FORMATO`  
  Define o formato de saída (exemplo: `long`, `commas`, `horizontal`, `vertical`).

- `--full-time`  
  Mostra o tempo completo (usado com `-l`).

- `-g`  
  Mostra como `-l`, mas sem o proprietário.

- `--group-directories-first`  
  Agrupa diretórios antes dos arquivos.

- `-G, --no-group`  
  Não mostra os nomes dos grupos na listagem longa.

- `-h, --human-readable`  
  Mostra os tamanhos de arquivos em um formato legível (exemplo: 1K, 234M, 2G).

- `--si`  
  Similar a `-h`, mas usa potências de 1000 em vez de 1024.

- `-H, --dereference-command-line`  
  Segue links simbólicos listados na linha de comando.

- `--hide=PADRÃO`  
  Oculta arquivos que correspondem ao padrão do shell (anulado por `-a` ou `-A`).

- `--hyperlink[=QUANDO]`  
  Cria links nos nomes dos arquivos.

- `-i, --inode`  
  Mostra o número de índice (inode) de cada arquivo.

- `-I, --ignore=PADRÃO`  
  Ignora arquivos que correspondem ao padrão do shell.

- `-k, --kibibytes`  
  Usa blocos de 1024 bytes para o uso do sistema de arquivos.

- `-l`  
  Usa um formato de listagem longa.

- `-L, --dereference`  
  Mostra informações do arquivo referenciado por links simbólicos.

- `-m`  
  Lista arquivos separados por vírgulas.

- `-n, --numeric-uid-gid`  
  Mostra IDs numéricos de usuário e grupo.

- `-N, --literal`  
  Mostra nomes de arquivos sem aspas.

- `-o`  
  Mostra como `-l`, mas sem as informações de grupo.

- `-p, --indicator-style=slash`  
  Adiciona ` /` aos diretórios.

- `-q, --hide-control-chars`  
  Mostra `?` em vez de caracteres não gráficos.

- `-Q, --quote-name`  
  Coloca nomes de arquivos entre aspas duplas.

- `-r, --reverse`  
  Inverte a ordem de classificação.

- `-R, --recursive`  
  Lista subdiretórios recursivamente.

- `-s, --size`  
  Mostra o tamanho alocado de cada arquivo, em blocos.

- `-S`  
  Ordena por tamanho de arquivo, do maior para o menor.

- `--sort=PALAVRA`  
  Ordena por PALAVRA em vez de nome (exemplo: `none`, `size`, `time`, `version`, `extension`).

- `--time=PALAVRA`  
  Usa um tempo diferente para a ordenação e exibição (exemplo: `atime`, `ctime`, `birth`).

- `-t`  
  Ordena por tempo, do mais recente para o mais antigo.

- `-T, --tabsize=COLS`  
  Define o tamanho das tabulações.

- `-u`  
  Ordena e mostra o tempo de acesso (usado com `-lt`).

- `-U`  
  Não ordena; lista na ordem do diretório.

- `-v`  
  Ordena naturalmente por números de versão.

- `-w, --width=COLS`  
  Define a largura da saída.

- `-x`  
  Lista os arquivos por linhas.

- `-X`  
  Ordena alfabeticamente por extensão de arquivo.

- `-Z, --context`  
  Mostra o contexto de segurança de cada arquivo.

- `--zero`  
  Termina cada linha de saída com NUL, não com nova linha.

- `-1`  
  Lista um arquivo por linha.

- `--help`  
  Mostra a ajuda e sai.

- `--version`  
  Mostra a versão e sai.

## Notas Adicionais

- O argumento `TAMANHO` é um número inteiro e unidade opcional (exemplo: `10K` é `10*1024`).  
  As unidades podem ser `K, M, G, T, P, E, Z, Y` (potências de 1024) ou `KB, MB, ...` (potências de 1000).

- O argumento `TIME_STYLE` pode ser `full-iso`, `long-iso`, `iso`, `locale`, ou `+FORMATO`.  
  Se `FORMATO` for `FORMATO1<newline>FORMATO2`, então `FORMATO1` se aplica a arquivos não recentes e `FORMATO2` a arquivos recentes.

- O argumento `QUANDO` para cores e links pode ser `always`, `auto`, ou `never`.

- O comando `ls` emite códigos de cores apenas quando a saída está conectada a um terminal, a menos que `--color=never` seja usado.

- A variável de ambiente `LS_COLORS` pode alterar as configurações de cores. Use o comando `dircolors` para configurá-la.
