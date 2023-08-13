from flask import Flask, Blueprint, render_template
from api.api import api
import requests, json

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')

@app.route("/")
def homePage():
    data = requests.get('http://127.0.0.1:5000/api/data')
    data = json.loads(data.text)
    return render_template('dataTable.html', cursor=data)


if __name__ == '__main__':
    app.run(debug=True)