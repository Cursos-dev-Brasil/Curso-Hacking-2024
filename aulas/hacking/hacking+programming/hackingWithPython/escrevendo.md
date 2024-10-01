# Escrevendo um script

Antes de começar o hacking, vamos recaptular alguns principios da linguagem em scripts, escreva isso na sua IDE ao invés do interpretador

```py
# Arquivo: var.py

i = 5
print(i)
i = i + 5
print(i)

s = """ Isso é uma string 
    de linhas 
            múltiplas
"""

print(s)
```

## linhas física e lógica

O que você vê quando digita um código é a linha física. O que o python recebee quando você executa é chamado de linha lógica. Com isso dito, você precisa saber que o python interpreta toda linha física que você digita resulta em uma linha lógica (ou mais, depende do tamanho dela). Nessa linguagem, uma linha lógica pode ser dividida em várias linhas físicas usando o comando de escape (barra invertida - \\)


