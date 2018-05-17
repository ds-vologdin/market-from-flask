# market-form-flask
Интернет магазин на flask.

## Запуск

Можно работать через uwsgi
```
uwsgi --plugin python3  --plugin python_plugin --http-socket localhost:9090 --wsgi-file market.py -H /home/bud/coding/git/market-from-flk/env/ --callable app
```

А можно для отладки пользоваться встроенным во flask http-сервером
```
python market.py
```

# Добавление товара
```
curl --header "Content-Type: application/json"   --request POST   --data '{"name":"xyz","category":"xyz"}'   http://localhost:5000/api/add_product
```
