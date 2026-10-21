1. Sequência enumerada de comandos usada para enviar os arquivos para o repositório

1.1. Clonar o repositório já criado:


git clone https://...

1.2. Depois de realizar as atividades dentro do diretório do repositório, usar:


git add *
git commit -m "mensagem"

1.3. Para enviar os commits, usar:


git push

2. Sequência enumerada usada para baixar o programa do repositório e executar
2.1. Clonar novamente o repositório:


git clone https://...

2.2. Depois de abrir o diretório dentro do VS Code, será necessário refazer o arquivo .venv e o .env, já que esses dois não foram para o GitHub, pois estavam dentro do .gitignore.

Então, temos que usar novamente:


uv add pymysql
uv add sqlalchemy

Essas linhas restauram o ambiente virtual. Agora, para refazer o .env, apenas crie um arquivo dentro do diretório principal chamado .env e coloque as informações do banco de dados fornecido pelo professor.

2.3. Para rodar o código agora, basta usar:


uv run principal.py
