from models import Genero, Jogo, Base
import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

load_dotenv()
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = quote_plus(os.getenv("MYSQL_PASSWORD"))
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

#MYsql
engine = create_engine(
f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
)
Base.metadata.create_all(engine)

#SQLite
engine2 = create_engine("sqlite:///jogos_e_genero.db")
Base.metadata.create_all(engine2)

banner = r"""
  ____    _    __  __ _____ ____
 / ___|  / \  |  \/  | ____/ ___|
| |  _  / _ \ | |\/| |  _| \___ \
| |_| |/ ___ \| |  | | |___ ___) |
 \____/_/   \_\_|  |_|_____|____/

+----------------------------------+
|     O QUE VOCE DESEJA FAZER?     |
+----------------------------------+
|  1 - inserir                     |
|  2 - Listar                      |
|  3 - Excluir                     |
|  4 - Sair                        |
+----------------------------------+
"""

def escolher_banco_de_dados():
    print(r"""
Em qual banco você gostaria de salvar esses dados?

1- Mysql
2- SQLite
""")
    banco_de_dados_escolhido = input(": ").strip()
    return banco_de_dados_escolhido

def mostrar_menu():
    print(banner)


def menu():
    while True:
        mostrar_menu()
        opcao = input("Digite o que gostaria: ").strip()
        if opcao == "1":
            print("inserir")
            banco_de_dados = escolher_banco_de_dados()
            if banco_de_dados == "1":
                with Session(engine) as session:
                    # criar uma Jogo
                    j = Jogo(nome="João", 
                            desenvolvedora="joao@email.com",
                            ano_lancamento="11999999999",
                            preco= 0,
                            genero= " ")

                    # adicionar a pessoa na sessão, preparando para ser gravada
                    session.add(j)
                        
                    # confirmar a inserção no banco de dados
                    session.commit()

                print("Tabela criada (se não havia) e pessoa inserida no banco de dados")

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
