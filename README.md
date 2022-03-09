# personalizar-user-django
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/LombaAnderson/personalizar-user-django/blob/main/LICENSE)

# Sobre o projeto
 O cadastro-django trata-se de desenvolvimento de uma tela para cadastro, login e logout do usuário, o login e todas as telas são responsivas e foi utilizado o Django Templates.
Foi feita a estilização simples e usado o Bootstrap para fazê-la e foi feito também nesse projeto o sistema de autenticação já existente do Django. Em seguida, foi providenciada uma rota REST para todos os usuários cadastrados e exigida autenticação do usuário para acesso das informações. Nesse projeto foi instalado o app django-crispy-forms que é responsável pela estilização da página de cadastro. As rotas para acesso às páginas accounts/signup, login e logout dão entrada a toda a parte de cadastro, login e logout do usuário do projeto cadastro-django.

## Imagem da página de cadastro
<div align="center">
<img src="https://user-images.githubusercontent.com/60937513/151632442-a036dd94-240c-4e97-8bc8-b481659836c8.png" width="700" />
</div>

# Tecnologias utilizadas

- Python
- API Django Rest
- Django
- Django-allauth
- Django-crispy-forms
- Python-decouple( responsável por escamotiar as senhas do Django. Enviei por email as senhas necessárias para acesso,mas se precisar de algo estou a disposição)

# Instruções para compilar, testar e rodar o projeto

```bash
# Clonar repositório
git clone https://github.com/LombaAnderson/cadastro-django

# Criação do ambiente de desenvolvimento do Python
-python -m venv venv

# Ativar o ambiente de desenvolvimento(venv)
-source venv/Scripts/activate

# Instalação do Django (Atenção: instalar somente após a ativação da venv)
-pip install django

# Instalação do pacote do Django Rest Framework
-pip install django djangorestframework
 
# Comando de criação do projeto
-django-admin startproject cad_usuario .

# Criação e acesso do servidor
-python manage.py runserver

# Acesso ao servidor Django
http://127.0.0.1:8000/accounts/signup/

```

# Autor

Anderson Lomba de Oliveira

Linkedin

https://www.linkedin.com/in/anderson-lomba-140279142/

Portfólio

https://www.lombanderson.epizy.com

# Agradecimentos

Agradeço ao meu Deus que é meu tudo, Ele olha sempre por mim e a minha esposa, minha companheira que amo muito e sempre torce por mim!
