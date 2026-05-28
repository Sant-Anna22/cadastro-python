import os

lista = []
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

    
def cadastro():
    nome = input('Digite o nome: ').title()
    if not nome:
        limpar()
        print('Você deixou campos em branco.', '\n' * 2)
        return
    elif nome.isdigit():
        limpar()
        print('Nome não pode ser um número.')
        return
    
    try:
        idade = int(input('Digite a idade: '))
    except ValueError:
        limpar()
        print('Sua idade tem que ser um número válido.')
        return
    
    profissao = input('Digite a profissao: ').title()
    if not profissao:
        limpar()
        print('Você deixou campos em branco.', '\n' * 2)
        return
    
    lista.append({
        'nome': nome,
        'idade': idade,
        'profissao': profissao
    })

def listagem():
    if not lista:
        print('Sua lista está vazia. Cadastre alguém!')
        return
    for i, d in enumerate(lista):
        print(f"{i} - {d['nome']} | {d['idade']} Anos | {d['profissao']}")
    print('')

def apagar():
    if not lista:
        print('Sua lista está vazia.')
        return
    try:
        escolha = int(input('Digite o índice que deseja apagar: '))
        decisao = input('Tem certeza? [s/n] ').lower()
        decisoes_possiveis = {'s', 'n'}
        if decisao in decisoes_possiveis:
            if decisao == 's':
                limpar()
                print('Cadastro apagado.', '\n' * 2)
                del lista[escolha]
            elif decisao == 'n':
                limpar()
                return
        else:
            limpar()
            print('Escolha uma opção válida')
            return
    except ValueError:
        print('O índice tem que ser um número váldo.')
    except IndexError:
        print('Esse índice não está na sua lista.')

while True:
    opcao = input('Escolha uma opção:\n'
                  '\n'
                  '[c]adastrar\n'
                  '[l]istar \n'
                  '[a]pagar\n'
                  '[s]air\n'
                  '\n'
                  '--> '
                  ).lower()
    opcoes_possiveis = "clas"
    if not opcao:
        limpar()
        print('Você não pode deixar este campo em branco.', '\n' * 2)
        continue
    elif opcao == 'c':
        limpar()
        cadastro()
        continue
    elif opcao == 'l':
        limpar()
        listagem()
        continue
    elif opcao == 's':
        limpar()
        print('Você saiu')
        break
    elif opcao == 'a':
        limpar()
        apagar()
    elif opcao not in opcoes_possiveis:
        limpar()
        print('Escolha uma opção válida')
        continue