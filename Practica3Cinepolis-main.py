from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route("/cinepolis", methods=["GET","POST"])
def cinepolis():
    numb=(request.form.get("txtNumB"))
    if request.method=="POST":
        pagoT= (request.form.get("btnTarjeta"))
        numP= (request.form.get("txtNumPer"))
        precioB = 12
        while(int(numP)==1):
            while(int(numb)<=7 and int(numb)>0 ):
                if(int(numb)==3 or int(numb)==4 or int(numb)==5):
                    if(pagoT=="1"):
                        resultado=(int(numb)*precioB)-(float(int(numb))*(precioB)/(100*0.10))
                        resultado2=(float(resultado)/(100*0.10))           
                        resp="Se ha aplicado 10%, de descuento, ademas de 10%, de descuesto por pagar con tarjeta Cineco, por lo que el precio a pagar es de: ${}".format(str(float(resultado)-(float(resultado2))))  
                        return render_template("Practica3Cinepolis-main.html",resp=resp)
                    else:
                        resultado=(int(numb)*precioB)-(float(int(numb))*(precioB)/(100*0.10))            
                        resp=resp="Se ha aplicado 10%, de descuento, por lo que el precio a pagar es de: ${}".format(str(resultado))
                        return render_template("Practica3Cinepolis-main.html",resp=resp)
                elif(int(numb)>5):
                    if(pagoT=="1"):
                        resultado=((int(numb)*precioB)-(float(int(numb))*(precioB)*(0.15)))
                        resultado2=(float(resultado)*(0.10))           
                        resp="Se ha aplicado 15%, de descuento, ademas de 10%, de descuesto por pagar con tarjeta Cineco, por lo que el precio a pagar es de: ${}".format(str(float(resultado)-(float(resultado2))))  
                        return render_template("Practica3Cinepolis-main.html",resp=resp)
                    else:
                        resultado=(int(numb)*precioB)-(float(int(numb))*(precioB)*(0.15))            
                        resp="Se ha aplicado 15%, de descuento, por lo que el precio a pagar es de: ${}".format(str(resultado))
                        return render_template("Practica3Cinepolis-main.html",resp=resp)
                else:
                    if(pagoT=="1"):
                        resultado=(float(int(numb)*precioB))
                        resultado2=(float(resultado)/(100*0.10))
                        resp="Se ha aplicado 10%, de descuesto por pagar con tarjeta Cineco, por lo que el precio a pagar es de: ${}".format(str(float(resultado)-(float(resultado2))))  
                        return render_template("Practica3Cinepolis-main.html",resp=resp)
                    else:
                        resultado=(int(numb)*precioB)
                        resp="El precio a pagar es de: ${}".format(str(resultado))
                        return render_template("Practica3Cinepolis-main.html",resp=resp)
                resp=("No se pueden comprar mas de 7 boletos")
                return render_template("Practica3Cinepolis-main.html",resp=resp)
            resp=("Solo 1 persona puede comprar 7 boletos")
            return render_template("Practica3Cinepolis-main.html",resp=resp)
    return render_template("Practica3Cinepolis-main.html",numb=numb)

if __name__=="__main__":
    app.run(debug=True,port=3000)
