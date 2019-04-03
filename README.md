# Twitter_proj

O Twitter_proj é um projeto criado para efetuar buscas de mensagens no twitter a partir de uma hashtag previamente cadastrada.

Pré-requisitos:
1 - Python 3.7.2;
2 - Você deve possuir uma conta no twitter e habilitar a função desenvolvedor;
3 - Além disso, é necessário criar um novo aplicativo no twitter para receber as credenciais.

Utilização:
1 - Clone o repositório;
2 - Vá até a pasta raíz do projeto e crie um ambiente virtual executando o seguinte comando no terminal:
	  python -m venv C:\Users\admin\Documents\Prog\Python\Django\Twitter_proj\venv
3 - Ative o ambiente acessando, via terminal, a pasta Script dentro do diretório virtual e rodando o comando:
    activate
4 - Volte a pasta raiz do projeto e instale os requisitos do sistema com o comando:
  	pip install -r requirements.txt
5 - Acesse a pasta twitter e crie as tabelas o banco de dados:
	  python manage.py migrate
6 - Crie seu super usuário para possuir acesso a guia de administração do projeto:
	  python manage.py createsuperuser
7 - O layout da guia de administração foi sobrescrevido, por isso é necessário apagar os arquivos de layout padrão base.html, base-site.html e login.html.
  	Para isto acesse a partir do diretório raiz do projeto, a pasta \venv\Lib\site-packages\django\contrib\admin\templates\admin
	 e apague de seu conteúdo os arquivos base.html, base-site.html e login.html
8 - Acesse o arquivo settings.py complete os seguintes campos as credenciais da sua aplicação no twitter:
    consummer_key
    consummer_secret
    acess_key
    acess_secret
9 - Volte a pasta Twitter_proj/twitter e rode sua aplicação:
	  python manage.py runserver
10 - A tela inicial da aplicação exibe as mensagens buscadas no twitter a partir das hashtags cadastradas. Para cadastrar hashtags, acesse a guia Admin, faça acesso com o usuário criado no item 6, e em Hashtags faça o cadastro das hashtags que deseja acompanhar.
