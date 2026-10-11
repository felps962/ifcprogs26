import models
banner = r"""
  ____    _    __  __ _____ ____
 / ___|  / \  |  \/  | ____/ ___|
| |  _  / _ \ | |\/| |  _| \___ \
| |_| |/ ___ \| |  | | |___ ___) |
 \____/_/   \_\_|  |_|_____|____/
"""
opcoes = ["1 - Adicionar", "2 - Listar", "3 - Excluir", "4 - Sair"]

def mostrar_menu():
    print(banner)
    print("+" + "-" * 34 + "+")
    print("|" + "O QUE VOCE DESEJA FAZER?".center(34) + "|")
    print("+" + "-" * 34 + "+")
    for opcao in opcoes:
        print("|  " + opcao.ljust(32) + "|")
    print("+" + "-" * 34 + "+")


def menu():
    while True:
        mostrar_menu()
        opcao = input("Digite o que gostaria: ").strip()

        if opcao == "1":
            print("adicionar")
        elif opcao == "2":
            print("listar")
        elif opcao == "3":
            print("excluir")
        elif opcao == "4":
            print("Ate mais!")
            break
        else:
            print("Opcao invalida, tente de novo.")


menu()