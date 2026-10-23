# Strength — Jogo da Forca

Jogo da forca desenvolvido em Python para jogar pelo terminal. O jogador precisa descobrir uma palavra sorteada, digitando letras antes de atingir seis erros. Ao final da partida, o nome e a pontuação são salvos em um arquivo de texto.

## Funcionalidades

- Menu com opções para jogar, consultar scores e sair.
- Sorteio de palavras a partir de um arquivo de texto.
- Exibição das letras descobertas e das posições ainda ocultas.
- Desenho da forca atualizado a cada tentativa válida.
- Identificação de letras já utilizadas na partida.
- Encerramento ao descobrir a palavra ou atingir seis erros.
- Registro do nome do jogador e da pontuação em `score.txt`.

## Tecnologias

- Python 3.
- Módulo `random` da biblioteca padrão para sortear palavras.
- Arquivos de texto para armazenar palavras e resultados.

Não é necessário instalar bibliotecas externas.

## Como executar

Tenha o Python 3 e o Git instalados. Depois, execute no terminal:

```bash
git clone https://github.com/gracicosta/-Strength.git
cd ./-Strength
python forca.py
```

Se o seu sistema utiliza o comando `python3`, execute:

```bash
python3 forca.py
```

Execute o jogo a partir da pasta do projeto, pois os arquivos `palavras.txt` e `score.txt` são acessados por caminhos relativos.

## Como jogar

1. Escolha a opção **1 — JOGAR** no menu.
2. Informe o nome do jogador.
3. Digite uma letra por tentativa, preferencialmente sem acentos.
4. Descubra a palavra antes de cometer seis erros.
5. Ao terminar, o resultado será registrado e o menu será exibido novamente.

A opção **2 — SCORE** exibe o conteúdo do arquivo de pontuações. A opção **3 — SAIR** encerra o programa.

## Pontuação

A pontuação depende da quantidade de erros acumulados na partida:

| Erros | Pontos |
| --- | --- |
| 0 | 1.000 |
| 1 | 800 |
| 2 | 600 |
| 3 | 400 |
| 4 | 200 |
| 5 | 100 |
| 6 | 0 |

Os resultados são adicionados ao arquivo `score.txt`, um por linha, no formato:

```text
Nome do jogador;800
```

Os registros são mantidos na ordem de gravação, sem classificação automática por pontuação.

## Organização do projeto

| Arquivo | Responsabilidade |
| --- | --- |
| `forca.py` | Inicia o programa e controla o menu principal. |
| `jogo.py` | Gerencia o sorteio, as tentativas e o encerramento da partida. |
| `desenhos.py` | Exibe a palavra oculta, desenha a forca e calcula a pontuação. |
| `fileHandler.py` | Reúne funções de leitura, criação e gravação de arquivos. |
| `palavras.txt` | Armazena as palavras disponíveis para sorteio. |
| `score.txt` | Armazena os nomes e as pontuações dos jogadores. |

## Personalizar as palavras

Edite o arquivo `palavras.txt` e coloque uma palavra por linha. Use letras minúsculas, de preferência sem acentos, e evite linhas vazias. Mantenha pelo menos uma palavra no arquivo.

## Limitações atuais

- O menu espera uma opção numérica; entradas de texto não são tratadas.
- O campo de tentativa ainda não restringe a entrada a uma única letra. Para jogar conforme as regras, digite apenas uma letra por vez.
- A consulta de scores imprime os registros, mas também mostra a mensagem `Score vazio.` mesmo quando existem resultados. Isso acontece porque a função de listagem imprime o conteúdo sem retorná-lo ao menu.

## Autoria

Projeto disponível no perfil de [gracicosta](https://github.com/gracicosta).

