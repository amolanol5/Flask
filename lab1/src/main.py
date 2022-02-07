from cProfile import run
from cgi import test
from turtle import color
from webbrowser import get
from flask import Flask, request , render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/status', methods=['POST' , 'GET'])
def status():    
    formulario = request.args.get("name")
    return "this is my name: {}".format(formulario)


if __name__ == ("__main__"):
    app.run(host="0.0.0.0", port=8080)
    
    
    
    
    
#args = request.args
#color_seleccionado = args.get("color")
#return "El color seleccionada es el siguiente: {}".format(color_seleccionado)


#    formulario = request.form['name']