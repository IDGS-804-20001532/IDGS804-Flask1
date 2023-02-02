
from flask import Flask
from flask import request

app=Flask(__name__)

@app.route("/suma", methods=["GET","POST"])
def suma():
    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        resultado=request.form.get("resultado")
        if(resultado=="suma"):
            return "<h1> La suma es: {} </h1>".format(str(int(num1)+int(num2)))
        elif(resultado=="resta"):
            return "<h1> La resta es: {} </h1>".format(str(int(num1)-int(num2)))
        elif(resultado=="multiplicacion"):
            return "<h1> La multiplicacion es: {} </h1>".format(str(int(num1)*int(num2)))
        elif(resultado=="division"):
            return "<h1> La division es: {} </h1>".format(str(int(num1)/int(num2)))
    else: 
        return '''
            <form action = '/suma' method="POST">
                <label>Suma: </label>
                <input type="radio" id="suma" name="resultado" value="suma">
                <label>Resta: </label>
                <input type="radio" id="resta" name="resultado" value="resta">
                <label>Multiplicacón: </label>
                <input type="radio" id="multiplicacion" name="resultado" value="multiplicacion">
                <label>División: </label>
                <input type="radio" id="division" name="resultado" value="division"><br>
                <label>N1: </label>
                <input type="text" name="num1"/></br></br>
                <label>N2: </label>
                <input type="text" name="num2"/></br></br>
                <input type="submit" value="Calcular"/></br></br> 
            </form>
        '''

if __name__=="__main__":
    app.run(debug=True,port=3000)