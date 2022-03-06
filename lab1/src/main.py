from cProfile import run
from cgi import test
from distutils.log import debug
from turtle import color
from webbrowser import get
from flask import Flask, request , render_template

app = Flask(__name__)

@app.route("/")
def index():
    varmola  = "this is a text from main page"
    return render_template('index.html', varmola = varmola)



@app.route('/status', methods=['POST' , 'GET'])
def status():    
    if request.method == 'POST':
        valorrecibido = request.form['nombre']
        return valorrecibido
    else:
        return "this not is a post method is insecure"
        # return "this is my name: {}".format(formulario)



if __name__ == ("__main__"):
    app.run(host="0.0.0.0", debug= True, port=8080)
    
    
    
    
    
#args = request.args
#color_seleccionado = args.get("color")
#return "El color seleccionada es el siguiente: {}".format(color_seleccionado)
#    formulario = request.form['name']