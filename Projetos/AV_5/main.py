import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Genero, Jogo, Base
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
|  1 - Inserir                     |
|  2 - Listar                      |
|  3 - Excluir                     |
|  4 - Trocar de banco             |
|  5 - Sair                        |
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
    engine_atual = None  # banco em uso (None = ainda não escolhido)

    while True:
        # se ainda não tem banco escolhido, pergunta
        if engine_atual is None:
            banco_de_dados_escolhido = escolher_banco_de_dados()
            if banco_de_dados_escolhido == "1":
                engine_atual = engine
            elif banco_de_dados_escolhido == "2":
                engine_atual = engine2
            else:
                print("Opcao invalida, tente de novo.")
                continue

        mostrar_menu()
        opcao = input("Digite o que gostaria: ").strip()

        if opcao == "1":
            print("inserir")
            tipo = input("1 - Genero | 2 - Jogo: ").strip()

            with Session(engine_atual) as session:
                if tipo == "1":
                    g = Genero(nome=input("Nome do genero: "),
                               jogabilidade=input("Jogabilidade: "),
                               exige_jogar_online=input("Exige jogar online? (s/n): ").strip().lower() == "s",
                               publico_alvo=input("Publico alvo: "))
                    session.add(g)
                    session.commit()
                    print("Genero inserido no banco de dados")

                elif tipo == "2":
                    # mostra os generos para o usuario escolher o id
                    for g in session.scalars(select(Genero)):
                        print(g.id, "-", g.nome)

                    genero = session.get(Genero, int(input("ID do genero do jogo: ")))
                    if genero is None:
                        print("Genero nao encontrado, cadastre o genero primeiro.")
                    else:
                        j = Jogo(nome=input("Nome do jogo: "),
                                 desenvolvedora=input("Desenvolvedora: "),
                                 ano_lancamento=int(input("Ano de lancamento: ")),
                                 preco=float(input("Preco: ")),
                                 genero=genero)
                        session.add(j)
                        session.commit()
                        print("Jogo inserido no banco de dados")
                else:
                    print("Opcao invalida.")

        elif opcao == "2":
            print("listar")
            with Session(engine_atual) as session:
                print("--- GENEROS ---")
                for g in session.scalars(select(Genero)):
                    print(g.id, g.nome, g.jogabilidade, g.exige_jogar_online, g.publico_alvo)

                print("--- JOGOS ---")
                for j in session.scalars(select(Jogo)):
                    print(j.id, j.nome, j.desenvolvedora, j.ano_lancamento, j.preco, j.genero.nome)

        elif opcao == "3":
            print("excluir")
            tipo = input("1 - Genero | 2 - Jogo: ").strip()

            with Session(engine_atual) as session:
                if tipo == "1":
                    g = session.get(Genero, int(input("ID do genero: ")))
                    if g is None:
                        print("Genero nao encontrado.")
                    elif g.jogos:
                        print("Esse genero tem jogos, exclua os jogos antes.")
                    else:
                        session.delete(g)
                        session.commit()
                        print("Genero excluido.")

                elif tipo == "2":
                    for j in session.scalars(select(Jogo)):
                        print(j.id, j.nome, j.desenvolvedora, j.ano_lancamento, j.preco, j.genero.nome)
                    j = session.get(Jogo, int(input("ID do jogo: ")))
                    if j is None:
                        print("Jogo nao encontrado.")
                    else:
                        session.delete(j)
                        session.commit()
                        print("Jogo excluido.")
                else:
                    print("Opcao invalida.")

        elif opcao == "4":
            engine_atual = None  # na proxima volta do loop pergunta o banco de novo

        elif opcao == "5":
            print("Ate mais!")
            break
        else:
            print("Opcao invalida, tente de novo.")


menu()