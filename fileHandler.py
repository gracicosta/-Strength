def valid_int(pergunta, min, max):

    x = int(input(pergunta))

    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError: #Se o programa dar erro vai retornar falso para a variavel arquivo
        return False
    else: #Se ocorrer tudo certo, vai retornar verdadeiro para a variavel arquivo
        return True
    
def criarArquivo(nomeArquivo): #Essa função só ocorre se o arquivo com o nome escolhido não existir em sistema
    try:
        a = open(nomeArquivo, 'wt+') #wt+ vai fazer a criação do arquivo
        a.close()
    except: #Se der errado retorna isso
        print('Erro na criação do arquivo.')
    else: #Se der certo retorna isso
        print(f'Arquivo {nomeArquivo} criado com sucesso! \n')

def cadastrarJogo(nomeArquivo, nomeJogo, nomeGame):
    try:
        a = open(nomeArquivo, 'at') #Abrir em modo de escrita sem modificar o que tem lá dentro
    except: #Se der erro vai dar esse comando
        print('Erro ao abrir o arquivo')
    else: #Se ocorrer tudo certo vai dar esse comando. a.write() serve para escrever no arquivo e pode ser escrito da maneira que quiser
        a.write(f'{nomeJogo}; {nomeGame}\n')
    finally: #Após a abertura do arquivo, tem que fechar
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally: 
        a.close()

def abrirArquivoLeitura(nomeArquivo):
    try:
        a = open(nomeArquivo, 'r')
    except:
        print('Não foi possível abrir para leitura')
    else:
        print(f'Arquivo {nomeArquivo} aberto com sucesso\n')
        return a

def inserir_score(nomeArquivo, nomeJogador, score):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        a.write('{};{}\n'.format(nomeJogador, score))
    finally:
        a.close()