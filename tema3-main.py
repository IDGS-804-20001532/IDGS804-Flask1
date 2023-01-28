
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo!"

@app.route("/user/<string:user>")
def user(user):
    return "Hola".format(user)

@app.route("/edad/<int:n>")
def edad(n):
    return "Número".format(n)

@app.route("/username/<int:id>/<string:username>")
def username(id, username):
    return "Nombre: {0} Id: {1}!".format(username,id)

@app.route("/suma/<float:num1>/<float:num2>")
def suma(num1, num2):
    return "La suma de {0} y {1} es  {2}".format(num1, num2, num1 + num2)


if __name__== "__main__":
    app.run(debug = True,port=3000)