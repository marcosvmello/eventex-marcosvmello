# EVENTEX

Sistemas de Eventos do curso Welcome to the Django.

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5.
3. Ative o virtualenv.
4. Instale as dependênias.
5. Configure a instância de desenvolvimento.
6. Execute os testes.


```console
git clone git@github.com:marcosvmello/eventex-marcosvmello.git wttd
cd wttd
python -m virtualenv .wttd
source wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample.env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no Heroku
2. Envie as configurações para o Heroku
3. Defina uma SECRET_KEY para o Heroku
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:ser SERCRET_Key='python contrib/secret_gen.py'
heroku config:set DEBUG=False
# cinfigure o email
git push heroku master --force
```
