Em Portuscript, funções são blocos de código reutilizáveis que podem ser definidos para executar tarefas específicas. Elas permitem modularizar o código, tornando-o mais organizado e facilitando a manutenção.

Aqui está uma explicação sobre como usar funções em Portuscript, junto com exemplos:

## Definição de Funções

Você pode definir uma função usando a palavra-chave `#!ptst func`. A estrutura básica de uma função inclui o nome da função, os parâmetros entre parênteses (optional) e um bloco de código associado. Aqui está um exemplo simples:

```ptst
func saudacao(nome) {
    imprima("Ola, " + nome + "!")
}
```

Neste exemplo, a função `saudacao` aceita um parâmetro `nome` e imprime uma mensagem de saudação.

## Chamada de Funções

Para chamar uma função, use o nome da função seguido pelos argumentos entre parênteses. Aqui está um exemplo de chamada da função `saudacao`:

```ptst
saudacao("Joao")
```

Esta chamada da função imprimirá "Ola, Joao!" no console.

## Retorno de Funções

Funções podem retornar valores usando a palavra-chave `#!ptst retorne`. Aqui está um exemplo de uma função que retorna a soma de dois números:

```ptst
func soma(a, b) {
    retorne a + b;
}

var resultado = soma(3, 4);
imprima(resultado);  # Isso imprimirá "7"
```

Neste exemplo, a função `soma` aceita dois parâmetros, `a` e `b`, e retorna a soma deles. O valor retornado é armazenado na variável `resultado`.

## Escopo de Variáveis

As variáveis definidas dentro de uma função têm escopo local e não são acessíveis fora da função. Isso significa que você pode usar o mesmo nome de variável em diferentes funções sem conflitos.

```ptst
func funcaoA() {
    var x = 10;
    imprima(x);
}

func funcaoB() {
    var x = 20;
    imprima(x);
}

funcaoA();  # Isso imprimirá "10"
funcaoB();  # Isso imprimirá "20"
```

Neste exemplo, ambas as funções têm uma variável chamada `x`, mas elas são independentes uma da outra.

Esses conceitos básicos de definição, chamada e retorno de funções fornecem uma base sólida para o uso efetivo de funções em Portuscript.