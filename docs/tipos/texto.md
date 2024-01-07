Representa os dados definidos entre aspas.

!!! tip "dica"
    Para converter um tipo de dado em outro do tipo `Texto`, basta usar a função embutida [`texto()`](../embutidos.md/#funcao-texto)

## Métodos

### `texto.junta(obj, obj1, obj2, ...)`

Este método concatena todos os objetos recebidos na sua chamada e usando o `texto` como separador.

Exemplo:

```ptst
imprima(", ".junta(1, 2, 3, 4)) # 1, 2, 3, 4
```

### `texto.titulo()`

Retorna uma cópia de `textp` com todas as letras em minúscula, exceto pela primeira que sempre será maiúscula.

Exemplo:

```ptst
imprima("portuscript".titulo()) # Portuscript
```

### `texto.maiusculas()`

Retorna uma cópia do texto com todas as letras em maiúsculas.

Exemplo:

```ptst
imprima("Olá, mundo!".maiusculas()) # OLÁ, MUNDO!
```

### `texto.minusculas()`

Retorna uma cópia do texto com todas as letras em minúsculas.

Exemplo:

```ptst
imprima("Olá, mundo!".minusculas()) # olá, mundo!oc
```
