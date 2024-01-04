Como talvez todos saibam, assim como na matemática, operadores são fundamentais na programação, pois sem eles não teríamos como manipular dados, seja soma, subtair ou comparar dois dados.

Existem diversos operadores em três principais tipos: aritméticos/matemáticos, operadores de comparação e operadores lógicos.

Toda boa linguagem implementa uma variedade deles com uma ordem de execução bem definidas, e em Portuscript não é diferente.

## Operadores matemáticos

- `**` - Exponenciação: Eleva um número (calcula sua potência)
```ptst
imprima(2 ** 2) # 4
```

- `*` - Multiplicação: Multiplica um valor pelo outro
```ptst
imprima(3 * 4) # 12
```

- `/` - Divisão: Divide um valor pelo outro
```ptst
imprima(4 / 4) # 1.0
imprima(1 / 2) # 0.5
```

- `//` - Divisão inteira: Divide um valor pelo outro e retorna apenas a parte inteira da operação
```ptst
imprima(4 / 4) # 1
imprima(1 / 2) # 0
```

- `+` - Adição: Soma dois valores ou concatena textos
```ptst
imprima(3 + 4) # 7
imprima("Olá" + "!") # Olá!
```

- `-` - Subtração: Subtrai valores
```ptst
imprima(11 - 4) # 7
```

## Operadores de comparação

- `>` - Maior que: Verifica se um valor é maior que outro
```ptst
imprima(2 > 0) # Verdadeiro
```

- `>=` - Maior ou igual a: Verifica se um valor é maior ou igual ao outro
```ptst
imprima(2 >= 0) # Verdadeiro
imprima(2 >= 2) # Verdadeiro
imprima(2 >= 3) # Falso
```

- `<` - Menor que: Verifica se um valor é menor que outro
```ptst
imprima(2 < 0) # Falso
```

- `<=` - Menor ou igual a: Verifica se um valor é menor ou igual ao outro
```ptst
imprima(2 <= 0) # Falso
imprima(2 <= 2) # Verdadeiro
imprima(2 <= 3) # Verdadeiro
```

- `==` - Igual a: Verifica se os dois valores são iguais
```ptst
imprima(2 == 2) # Verdadeiro
```

- `!=` - Diferente de: Verifica se os dois valores são diferentes
```ptst
imprima(2 != 0) # Verdadeiro
```

## Operadores lógicos

- `e` - E lógico: Verifica se ambos valores são `Verdadeiro`
```ptst
imprima(Verdadeiro e Falso) # Falso
```

- `ou` - Ou lógico: Verifica se algum dos valores é `Verdadeiro`
```ptst
imprima(Verdadeiro ou Falso) # Verdadeiro
```

- `nao` - Não lógico: Retorna o oposto do booleano equivalente a expressão declarada após ele
```ptst
imprima(nao Verdadeiro) # Falso
imprima(nao Falso) # Verdadeiro
```