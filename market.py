from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(request)
    return render_template('hello.html', user='Vasya')


@app.route('/api/add_product', methods=['POST'])
def api_add_product():
    print(request.get_json(force=True))
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)
