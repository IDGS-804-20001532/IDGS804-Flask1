from flask import Flask
from flask import request
from flask import render_template


app=Flask(__name__)

@app.route("/operabas")
def operasbas():
    return render_template("operasbas.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    n1=request.form.get("txtNum1")
    n2=request.form.get("txtNum2")
    res= int(n1)* int(n2)
    return render_template("resultado.html",n1=n1,n2=n2,res=res)
    


if __name__=="__main__":
    app.run(debug=True,port=3000)