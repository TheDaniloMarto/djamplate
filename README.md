<h1 align="center">DJAMPLATE</h1>

<p align="center">Um projeto Django pré-configurado para realizar o deploy no Heroku.</p>


Criei esse projeto com a intenção de agilizar o meu início de desenvolvimento com Django do qual consistem em fazer o deploy no Heroku.     


## Recursos

- python 3.10.5
- django 4.0.5
- poetry 1.1.13
- Princípio dos 12 fatores configurado com python-decouple
- coleta de arquivos estáticos com whitenoise
- Postgres configurado com docker
- pytest
- pre-commit

## Como usar

Clone o projeto

```
git clone https://github.com/TheDaniloMarto/djamplate < seu projeto >
```

Recriei o diretório .git
```
cd < seu projeto >
rm -rf .git
git init
git add .
git commit -m "ft: Initial commit"
```

Criei um app no Heroku

Configure as seguintes variáveis de ambiente no Heroku

- SECRET_KEY
- DEBUG
- ALLOWED_HOSTS
- DATABASE_URL

Instale o buildpak para o heroku poder gerar um build com poetry

Vincule o app do Heroku com o seu repositório remoto

Eu gravei um [vídeo](https://www.youtube.com/watch?v=_2rt1074v1w) para o youtube criando esse repositório.
