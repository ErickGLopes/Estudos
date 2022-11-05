from ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mERRO: não foi possível criar o arquivo!\033[m')
    else:
        print('\033[33mArquivo criado com sucesso!\033[m')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mERRO: não foi possível ler o arquivo!\033[m')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        sleep(2)
    finally:
        a.close()


def cadastrar(aquivo, nome='desconhecido', idade=0):
    try:
        a = open(aquivo, 'at')
    except:
        print('\033[31mHouve um ERRO na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um ERRO ao escrever no arquivo!\033[m')
        else:
            print(f'\033[33mNovo registro de {nome} realizado!\033[m')
            a.close()
            sleep(1)


