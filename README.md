# Candiru Cipher

Projeto desenvolvido durante o curso de Ciências da Computação para chegar a um resultado a partir de uma problematica entregue pelo professor. O objetivo é chegar a um texto cifrado final que tenha passado por três cifras diferentes, sendo elas:

### Passo 1

Cifra de cerco de trilho em que o texto claro é escrito em um retângulo, linha por linha, e o texto cifrado é obtido através da leitura, coluna por coluna, permutando-se seus caracteres de acordo com a ordem estabelecida pela chave. (Devem ser levados em consideração os espaços vazios)

```
Chave: 4   3   1   2
Texto: T   E   X   T
       O   _   Q   U
       A   L   Q   U
       E   R   _   _

Cifra: xqq tuu e lrtoae
```

### Passo 2

Logo em seguida cifre a saída do passo 1 utilizando a Cifra Polialfabética, utilizando achave informada como parâmetro e o tableau abaixo.

Entrada: xqq tuu e lrtoae

Saída: atrbxxvbicmtxrbg

![Imgur](https://i.imgur.com/d3Krss4.png)

### Passo 3

E por fim cifre a saída do passo 2 utilizando a Cifra Fluxo em cada caracter, utilizando a chave informada como parâmetro e o número constante 217 (ou seja, faça XOR entre cada caracter e índice da chave correspondente, juntamente com o número 11011001, 217 em binário).o resultado da cifra acima é passado por uma cifra de fluxo com a operação XOR e com chave 217 ou 1101100.

## Autores

- [@MuriloFuza](https://github.com/MuriloFuza)

## Licença

[MIT](https://choosealicense.com/licenses/mit/)

## Uso/Exemplo

```Python
from candiruCipher import CandiruCipher

candiruCipher = CandiruCipher()
CandiruCipher.encrypt(self=candiruCipher, message='texto qualquer', key='4,3,1,2')
```
