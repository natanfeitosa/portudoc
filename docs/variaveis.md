## Variáveis

As variáveis são uma das primeiras estruturas de dados que todo programador ou iniciante na programação aprende ao começar nesse mundo.

"Variável" geralmente é um termo associado a um caminho rápido para acessar um dado em memória que pode variar. São caracterizadas por terem um nome e valor.

Em Portuscript, para declararmos uma variável, basta que usemos a palavra-chave `var`.

Exemplo:
```ptst
var nome = "Meu nome";
imprima(nome) # Meu nome
```

Como dito anteriormente, variável é algo que pode variar, então vamos ver um exemplo disso.
```ptst
var ano = 2023;
imprima(ano) # 2023

ano = ano + 1;
imprima(ano) # 2024
```

Para reatribuir valor a uma variável, você não precisa (leia-se "não pode") usar a palavra-chave `var` novamente, apenas o nome da variável.

## Constantes

Constantes por outro lado, apesar de terem a mesma aparência de uma variável, não podem ser redeclaradas, isso quer dizer que uma vez definido um valor, esse não poderá ser alterado.

Exemplo:

```ptst
const ano = 2023;
imprima(ano) # 2023

ano = ano + 1; # Isso vai gerar um erro e o programa fechará
```

Outro exemplo:

```ptst
const nome = "Portuscript";

const nome = "portuscript"; # Também vai gerar um erro aqui
```

## Futuros

Ok, este não é um tipo de "variável", mas sim uma anotação para sintaxe futura.

Futuramente, variáveis e constantes poderão ser declaradas usando um valor padrão e/ou uma tipagem para a variável.

Variáveis já podem ser declaradas sem um valor padrão, o interpretador assumirá o tipo `Nulo` como valor, por outro lado, constantes não poderão ser criadas sem um valor.