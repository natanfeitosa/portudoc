As bibliotecas/módulos são partes fundamentais no desenvolvimento de software a medida que este cresce, e como toda linguagem que se preze, Portuscript tem sintaxe para importação e um conjunto de bibliotecas padrão da linguagem.

Para importar algo em Portuscript, devemos seguir a seguinte sintaxe:
```ptst
de "modulo" importe nome;
```

ou ainda
```ptst
de "modulo" importe nome, outronome;
```

??? info
    Há ainda outras sintaxes de importação sendo estudadas para ser implementadas como as seguintes.

    - Importa tudo e joga no escopo/contexto atual
    ```ptst
    de "modulo" importe *;
    ```

    - Executa o módulo apenas
    ```ptst
    importe "modulo";
    ```

    - Importa o módulo renomear e poderá acessar os membros como que fossem métodos através do novo nome
    ```ptst
    importe "modulo" como novonome;
    ```

!!! note
    Por enquanto, apenas módulos que fazem parte da biblioteca padrão podem ser importados