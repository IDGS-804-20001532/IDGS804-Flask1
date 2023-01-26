from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo"

#Parametros String 
@app.route("/user/<string:user>")
def user(user):
    return "Hola "+ user

#Parametros int 
@app.route("/numero/<int:n>")
def user(n):
    return "Número {}".format(n)

#Mas de un parametro 
@app.route("/user/<int:id>/<string:username>")
def user(id, username):
    return "Id: {} nombre: {}".format(id,username)



if __name__=="__main__":
    app.run(debug=True,port=3000)