Módulo do tipo utilitário para dar cores e estilo ao terminar/linha de comando.

!!! note
    Para fins de praticidade, vamos chamar o objeto do módulo `colorize` de `color`.

## `color.SUPORTA`
Esta é uma constante que diz se seu terminal aceita cores, ela tem o valor de acordo com a variável de ambiente `NO_COLOR`, se está variável de ambiente não existir no sistema ou estiver preenchida com string vazia, nossa constante vai ser `#!ptst Verdadeiro`.

## `color.imprimac(...objetos)`
Esta é uma função que funciona de forma bem parecida com a outra dos [Embutidos](../embutidos.md#funcao-imprima), porém diferente dela, essa está mais preparada pra trabalhar com cores. Isso é, se o sistema não aceitar cores, os caracteres adicionais referentes a cores e estilos serão removidos.

## `color.converteRGB(vermelho, verde, azul, background?)`

Esta é uma função que recebe os atributos já bem descritos acima, e retorna uma representação de código aceita pelo terminal caso [tenha suporte](#colorsuporta)

O último parâmetro é do tipo Booleano — isto é, só aceita `#!ptst Verdadeiro` ou `#!ptst Falso` — e seu valor padrão é `#!ptst Falso`.

```ptst
de "colorize" importe converteRGB;

converteRGB(255, 255, 255) # 38;2;255;255;255
converteRGB(255, 0, 20) # 38;2;255;0;20

converteRGB(255, 255, 255, Verdadeiro) # 48;2;255;255;255
converteRGB(255, 0, 20, Verdadeiro) # 48;2;255;0;20
```

## `color.FUNDO`
## `color.TEXTO`

!!! note
Por terem exatamente os mésmos métodos, este dois estão agrupados aqui

Apesar de terem as mesmas coisas, eles não definem as cores nos mesmos lugares, como talvez já esteja nítido.

Eles implementa uma sintaxe como `#!ptst color.<FUNDO ou METODO>.<cor>(...objeto)`. Para mostrar melhor como é, vamos a um exemplo.

```ptst
de "colorize" importe FUNDO, TEXTO;

imprimac(FUNDO.branco("este texto pode não ser visível")) # o texto vai ficar com a cor padrão do sistema para o terminal, porém o fundo será branco

imprimac(TEXTO.preto("este texto pode não ser visível")) # o fundo vai ficar com a cor padrão do sistema para o terminal, porém o texto será preto

imprimac(FUNDO.vermelho(TEXTO.lima("Um texto na cor lima e com fundo vermelho")))
```

### Cores disponíveis:

- vermelho - `#!css #ff0000`
- lima - `#!css #00ff00`
- azul - `#!css #0000ff`
- amarelo - `#!css #ffff00`
- agua - `#!css #00ffff`
- fuchsia - `#!css #ff00ff`
- branco - `#!css #fff`
- preto - `#!css #000`
