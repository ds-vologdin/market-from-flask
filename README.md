# market-form-flask
Интернет магазин на flask.

## Запуск
```
uwsgi --plugin python3  --plugin python_plugin --http-socket localhost:9090 --wsgi-file market.py -H /home/bud/coding/git/market-from-flk/env/ --callable app
```
