Representa uma sequência mutável de objetos definidos entre colchetes.

!!! note
    Ainda não há implementado um meio de converter outros tipos de dados em um do tipo `Lista` através de código portuscript.

Exemplo:
```ptst
const lista = [1, 2];
imprima(lista)
```

## Métodos

### `lista.adiciona(objeto)`

Recebe um objeto e o adiciona ao fim da lista

Exemplo:

```ptst
lista.adiciona(3)
imprima(lista) # [1, 2, 3]
```

### `lista.extende(objeto)`

Recebe uma lista e adiciona os itens ao fim da lista atual

Exemplo:

```ptst
lista.extende([4, 5])
imprima(lista) # [1, 2, 3, 4, 5]
```

### `lista.remove(objeto)`

Recebe um objeto, e se ele existir na lista, é removido

Exemplo:

```ptst
lista.remove(5)
imprima(lista) # [1, 2, 3, 4]
```

### `lista.pop(objeto?)`

Recebe o índice de um objeto a ser removido, se não for definido um índice, automaticamente ele será 0. O objeto removido também é retornado.

Exemplo:

```ptst
imprima(lista.pop()) # 1
imprima(lista) # [2, 3, 4]

imprima(lista.pop(1)) # 3
imprima(lista) # [2]
```

### `lista.indice(objeto)`

Recebe um objeto, se ele existir na lista, retorna o indíce correspondente.

Exemplo:

```ptst
imprima(lista.indice(2)) # 0
```

### `lista.limpa()`

Limpa totalmente a lista

Exemplo:

```ptst
lista.limpa()
imprima(lista) # []
```