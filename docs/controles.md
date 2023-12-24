O controle de fluxo em programação refere-se à capacidade de direcionar a execução do código de acordo com condições específicas.

Estruturas como "se", "senao" e "escolha" permitem que o programa tome decisões com base em avaliações lógicas. O uso de loops, como "para" e "enquanto", possibilita a repetição de blocos de código.

Essas ferramentas são fundamentais para criar algoritmos eficientes e adaptáveis, proporcionando maior flexibilidade e controle no desenvolvimento do seu software.

Como toda boa linguagem, o Portuscript também implementa alguma dessas estruturas. Veremos a seguir.

## `#!ptst se` / `#!ptst senao se` / `#!ptst senao`

Em Portuscript, a estrutura condicional é composta por blocos `#!ptst se`, `#!ptst senao se` e `#!ptst senao`. Essa estrutura permite que o código tome decisões com base em condições específicas. Aqui está uma explicação básica de como esses blocos funcionam, seguida de exemplos:

### Bloco `#!ptst se`
O bloco `#!ptst se` é usado para executar um bloco de código apenas se uma condição específica for verdadeira. A estrutura básica é a seguinte:

```ptst
se (condicao) {
    # código a ser executado se a condição for verdadeira
}
```

Exemplo:

```ptst
var x = 5;

se (x > 0) {
    imprima("x é positivo");
}
```

Neste exemplo, o código dentro do bloco `#!ptst se` será executado porque a condição `x > 0` é verdadeira.

### Bloco `#!ptst senao se`
O bloco `#!ptst senao se` é usado quando você tem várias condições e deseja verificar se uma delas é verdadeira. A estrutura básica é a seguinte:

```ptst
se (condicao1) {
    # código a ser executado se a condição1 for verdadeira
} senao se (condicao2) {
    # código a ser executado se a condição2 for verdadeira
} senao {
    # código a ser executado se nenhuma das condições anteriores for verdadeira
}
```

Exemplo:

```ptst
var x = 0;

se (x > 0) {
    imprima("x é positivo");
} senao se (x < 0) {
    imprima("x é negativo");
} senao {
    imprima("x é zero");
}
```

Neste exemplo, o código dentro do bloco `#!ptst senao` será executado porque nenhuma das condições anteriores é verdadeira.

### Bloco `#!ptst senao`
O bloco `#!ptst senao` é usado para executar um bloco de código quando nenhuma das condições anteriores é verdadeira. A estrutura básica é:

```ptst
se (condicao) {
    # código a ser executado se a condição for verdadeira
} senao {
    # código a ser executado se a condição não for verdadeira
}
```

Exemplo:

```ptst
var x = -5;

se (x > 0) {
    imprima("x é positivo");
} senao {
    imprima("x não é positivo");
}
```

Neste exemplo, o código dentro do bloco `#!ptst senao` será executado porque a condição `x > 0` não é verdadeira.

Esses blocos condicionais fornecem uma maneira flexível de controlar o fluxo de execução do código em Portuscript, permitindo que você tome decisões com base em diferentes condições.

## Bloco `#!ptst enquanto`

O bloco `#!ptst enquanto` permite que você crie um loop que executa um bloco de código enquanto uma determinada condição for verdadeira. A estrutura básica é a seguinte:

```ptst
var contador = 0;

enquanto (contador < 5) {
    # código a ser repetido enquanto a condição for verdadeira
    imprima(contador);
    contador = contador + 1;
}
```

Neste exemplo, o bloco de código dentro do `#!ptst enquanto` será repetido enquanto a condição `contador < 5` for verdadeira.

## Operador `#!ptst continue`

O operador `#!ptst continue` é usado para interromper a execução do bloco de código atual dentro de um loop `#!ptst enquanto` e continuar com a próxima iteração do loop. A estrutura básica é a seguinte:

```ptst
var contador = 0;

enquanto (contador < 5) {
    contador = contador + 1;

    se (contador == 2) {
        continue;  # Pula para a próxima iteração do loop
    }

    imprima(contador);
}
```

Neste exemplo, quando `contador` é igual a 2, a execução do bloco de código é interrompida e o loop continua com a próxima iteração.

## Operador `#!ptst pare`

O operador `#!ptst pare` é usado para interromper completamente a execução de um loop `#!ptst enquanto`. A estrutura básica é a seguinte:

```ptst
var contador = 0;

enquanto (contador < 5) {
    contador = contador + 1;

    se (contador == 3) {
        pare;  # Sai completamente do loop
    }

    imprima(contador);
}
```

Neste exemplo, quando `contador` é igual a 3, a execução do bloco de código é interrompida, e o loop `#!ptst enquanto` é encerrado imediatamente.

Esses recursos fornecem controle flexível sobre loops em Portuscript, permitindo que você decida quando continuar para a próxima iteração (`#!ptst continue`) ou sair completamente do loop (`#!ptst pare`).