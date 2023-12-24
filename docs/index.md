# Bem vindos ao Portuscript

## O que é o Portuscript

Portuscript é uma linguagen de programaçao baseada em português e amplamente inspirada por [Python](https://www.python.org/){:target="_blank"} e [Typescript](https://www.typescriptlang.org/){:target="_blank"}.

Tem por objetivo facilitar a entrada de pessoas ainda leigas e/ou sem muito conhecimento de inglês no mundo da progamação através de uma linguagem mais próxima da lingua materna e com comunidade totalmente em português, também sem esquecer de focar nas demandas do mercado por tecnologia e ferramentas de uso geral, além do foco acadêmico.

## Instalação

### Compilar a partir do código fonte

Uma opção que provavelmente nunca vai mudar é a de instalar através do código fonte.

Para esta instalação, certifique-se de ter o [git](https://git-scm.com/){:target="_blank"} ou [gh](https://cli.github.com/){:target="_blank"} e o [Go](https://golang.org/){:target="_blank"} instalados.

#### Clonando o repositório

=== "git"
    ```bash
    git clone https://github.com/natanfeitosa/portuscript.git
    ```
=== "gh"
    ```bash
    gh repo clone https://github.com/natanfeitosa/portuscript
    ```

#### Agora é só acessar o diretório criado
```bash
cd portuscript
```

#### Fazendo o build
Antes, vamos rodar o código para o `Go` lidar com as dependências

```bash
go run ./main.go -v # portuscript version dev
```

Estando tudo certo, podemos fazer o build

=== "Unix"

    ```bash
    go build -o build/portuscript
    ```

=== "Windows"
    ```bash
    go build -o build/portuscript.exe
    ```

Teremos um diretório `build` com nosso binário dentro.

### Usar o binário disponível no repositório
!!! warning
    Os instaladores ainda não são definitivos, podem sofrer alterações no futuro para facilitar a instalação multiplataforma ou permitir mais funcionalidades.

Navegue até a página do [lançamento mais recente](https://github.com/natanfeitosa/portuscript/releases/latest){:target="_blank"}, vá até o fim da página e lá terá diversos arquios compactados para cada arquitetura e sistema operacional. Escolha o que melhor se adequa ao seu ambiente.

Ao clicar, o download será feito e você poderá descompactar.

Dentro há o binário, uma cópia do arquivo [LICENSE](https://github.com/natanfeitosa/portuscript/blob/main/LICENSE){:target="_blank"} e do [README.md](https://github.com/natanfeitosa/portuscript/blob/main/README.md){:target="_blank"}

Basta executar o binário ou mover para o diretório certo a ser disponibilizado no env, de acordo com seu sistema.
