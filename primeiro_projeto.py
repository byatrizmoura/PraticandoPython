#Cadastrar pessoas
def cadastrar(pessoas):
    cpf = input("Digite seu CPF: ")
    nome = input("Digite seu NOME: ")
    idade = int(input("Digite seu IDADE: "))
    pessoas.append((cpf,nome,idade))

def listar(pessoas):
    for pessoa in pessoas:
        cpf, nome, idade = pessoa
        print(f"Nome {nome}, possui {idade} anos de idade e é portador(a) do CPF {cpf}")

def exibir_menu():
    print(''' \n Escolha uma opção:
    1. Cadastrar pessoa
    2. Listar pessoa
    3. Sair''')

def main():
    pessoas = []
    flag = True
    while flag:  #se a tag for verdadeira
        exibir_menu()
        try:
            opcao = int(input("Digite a opção: "))
            if opcao == 1:
                cadastrar(pessoas)
            elif opcao == 2:
                listar(pessoas)
            elif opcao == 3:
                flag = False
                print("Operação finalizada!")
            else:
                print("Opção inválida!")
        except ValueError:
            print("Favor digitar somente números")
main()