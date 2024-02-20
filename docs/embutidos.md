As funções e constantes embutidas servem para facilitar o desenvolvimento ou tornar algumas coisas possíveis, vamos ver uns exemplos.


## Constantes

1.  **Verdadeiro**: Representa o valor booleano verdadeiro.
    ```ptst
    imprima(Verdadeiro)  # Saída: Verdadeiro
    ```
    
2.  **Falso**: Representa o valor booleano falso.
    ```ptst
    imprima(Falso)  # Saída: Falso
    ```
    
3.  **Nulo**: Representa um valor nulo.
    ```ptst
    imprima(Nulo)  # Saída: Nulo
    ```    

## Funções/métodos

### Função "imprima"

-   **Descrição**: Imprime no console a representação ou a conversão em string dos objetos passados como argumentos, separados por espaço.
-   **Uso**: `imprima(...objetos)`
-   **Exemplo**:
    
    ```ptst
    imprima("Olá", 42, Verdadeiro)  # Saída: Olá 42 Verdadeiro
    ```

### Função "leia"

-   **Descrição**: Imprime um texto se especificado e lê uma entrada do usuário, retornando-a como texto.
-   **Uso**: `leia(frase_para_imprimir)`
-   **Exemplo**:
    
    ```ptst
    var texto_lido = leia("Digite algo:")
    imprima("Você digitou:", texto_lido)
    ```

### Função "doc"

-   **Descrição**: Obtém a documentação do objeto passado como argumento e a imprime. Se o objeto implementar a interface `I_ObtemDoc`, usa o método `ObtemDoc`; caso contrário, usa a documentação do tipo do objeto.
-   **Uso**: `doc(objeto)`
-   **Exemplo**:
    
    ```ptst
    doc(imprima)  # Imprime a documentação da função imprima
    ```

### Função "int"

-   **Descrição**: Recebe um objeto e retorna uma representação numérica do tipo inteiro, se possível.
-   **Uso**: `int(objeto)`
-   **Exemplo**:
    
    ```ptst
    var num = int("42")  
    imprima(num)  # Saída: 42
    ```

### Função "texto"

-   **Descrição**: Recebe um objeto e retorna uma representação no tipo texto, se possível.
-   **Uso**: `texto(objeto)`
-   **Exemplo**:
    
    ```ptst
    var texto_num = texto(42)
    imprima(texto_num)  # Saída: 42
    ```

### Função "tamanho"

-   **Descrição**: Recebe um objeto e retorna o tamanho dele, se implementar a interface `I__tamanho__`.
-   **Uso**: `tamanho(objeto)`
-   **Exemplo**:
    
    ```ptst
    var texto_tam = tamanho("portuscript")
    imprima(texto_tam)  # Saída: 11
    ```

### Função "instanciaDe"

!!! warning
    Ainda não há como usar no lado `ptst` do código.

-   **Descrição**: O parâmetro `tipos` pode ser um tipo ou uma tupla de tipos/classes. Verifica se o obj é instancia de algum dos tipos.
-   **Uso**: `instanciaDe(obj, tipos)`
-   **Exemplo**:
    
    ```ptst
    var e_inteiro = instanciaDe(1, Inteiro)
    imprima(e_inteiro)  # Saída: Verdadeiro
    ```

### Função "mesmoTipo"

-   **Descrição**: Verifica se os dois objetos são do mesmo tipo.
-   **Uso**: `mesmoTipo(obj1, obj2)`
-   **Exemplo**:
    
    ```ptst
    imprima(mesmoTipo(1, 2))  # Saída: Verdadeiro
    imprima(mesmoTipo(1, 2.0))  # Saída: Falso
    ```