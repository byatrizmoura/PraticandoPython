#Pegando as informações informadas pelo usuário e transformando em uma lista
def cadastrar(pessoas):
    cpf = input("Digite seu CPF: ")
    nome = input("Digite seu NOME: ")
    idade = int(input("Digite seu IDADE: "))
    pessoas.append((cpf,nome,idade))
    
#Definindo modo de apresentação dos dados quando solicitado a listagem
def listar(pessoas):
    for pessoa in pessoas:
        cpf, nome, idade = pessoa
        print(f"Nome {nome}, possui {idade} anos de idade e é portador(a) do CPF {cpf}")
        
#opções apresentadas no menu
def exibir_menu():
    print(''' \n Escolha uma opção:
    1. Cadastrar pessoa
    2. Listar pessoa
    3. Sair''')

#Funções executadas no menu, incluindo mensagem de erro e finalização
def main():
    pessoas = []
    flag = True
    while flag:  
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
