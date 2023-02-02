from flask import Flask
from flask import request
from flask import render_template
import math


app=Flask(__name__)

@app.route("/coordenadas")
def coordenadas():
    return render_template("Practica2.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    X1=float(request.form.get("txtX1"))
    X2=float(request.form.get("txtX2"))
    Y1=float(request.form.get("txtY1"))
    Y2=float(request.form.get("txtY2"))
    res= math.sqrt(pow(X1-Y1,2)+pow(X2-Y2,2))
    return render_template("Practica2R.html",X1=X1,X2=X2,Y1=Y1,Y2=Y2,res=res)
    


if __name__=="__main__":
    app.run(debug=True,port=3000)