Este módulo provê funções e constantes úteis a serem usadas quando precisar fazer operações matemáticas mais otimizadas do que seria escrevendo tudo em `ptst`.

!!! example
    ```ptst
    de "matematica" importe ... o que desejar importar;
    ```

!!! note
    Para fins de praticidade, vamos chamar o objeto do módulo `matematica` de `mat`.

## `mat.PI`
A constante matemática `π = 3.14159...` conforme a precisão do tipo [`decimal`](/tipos/decimal) usado no seu sistema

## `mat.E`
A constante matemática `e = 2.71828...` conforme a precisão do tipo [`decimal`](/tipos/decimal) usado no seu sistema

## `mat.raiz(randicando, indice=2)`
Calcula e retorna a raiz representada pelo tipo decimal.

Se o indice não for especificado, por padrão ele será igual a `2` e será calculado a raiz quadrada do valor de `radicando`.

A fórmula matemática é: \\(\sqrt[ind]{rad}\\) ou \\(\sqrt[2]{rad}\\)

```ptst
de "matematica" importe raiz;

imprima(raiz(4)) # 2.0
imprima(raiz(4, 3)) # 1.5874010519681994
```

## `mat.potencia(base, expoente)`
Calcula e retorna a potencia da base pelo expoente representada pelo tipo decimal.

A fórmula matemática é: \\(b ^ e\\)

```ptst
de "matematica" importe potencia;

imprima(potencia(4, 2)) # 16.0
imprima(potencia(4, 3)) # 64.0
```

## `mat.absoluto(numero)`
Retorna o valor absoluto de um número, isso é, sem sinal caso houver

```ptst
de "matematica" importe absoluto;

imprima(absoluto(-10)) # 10.0
imprima(absoluto(+10)) # 10.0
imprima(absoluto(-4.3)) # 4.3
imprima(absoluto(+4.3)) # 4.3
```

## `mat.piso(numero)`
Retorna o numero arredondado para baixo

```ptst
de "matematica" importe piso;

imprima(piso(3)) # 3
imprima(piso(3.77)) # 3
imprima(piso(3.99)) # 3
```

## `mat.teto(numero)`
Retorna o numero arredondado para cima

```ptst
de "matematica" importe teto;

imprima(teto(3)) # 3
imprima(teto(3.77)) # 4
imprima(teto(3.99)) # 4
```