from flask import Flask
from flask import request
from flask import render_template
from datetime import date


app=Flask(__name__)

def calcularEdad(fecha):
    hoy = date.today()
    edad = hoy.year - fecha.year -((hoy.month, hoy.day) < (fecha.month, fecha.day))
    return edad

@app.route("/datos")
def datos():
    return render_template("Practica4RSignoZodiacal.html")

@app.route("/datosF", methods=["GET","POST"])
def datosF():
    nombre=(request.form.get("txtNombre"))
    ap=(request.form.get("txtAp"))
    am=(request.form.get("txtAm"))
    dia=(request.form.get("txtD"))
    mes=(request.form.get("txtM"))
    ano=(request.form.get("txtAn"))
    btnP=(request.form.get("btnP"))
    btnP2=(request.form.get("btnP2"))
    btnP3=(request.form.get("btnP3"))
    btnP4=(request.form.get("btnP4"))
    btnP5=(request.form.get("btnP5"))

    nombreC=str(nombre+" "+ap+" "+am)

    if(btnP=="4"):
        p=2
    else:
        p=0

    if(btnP2=="1"):
        p2=2
    else:
        p2=0
    
    if(btnP3=="10"):
        p3=2
    else:
        p3=0
    
    if(btnP4=="2"):
        p4=2
    else:
        p4=0

    if(btnP5=="9"):
        p5=2
    else:
        p5=0
    m=mes[1]
    a=(calcularEdad(date(int(ano),int(m),int(dia))))


    
    r=p+p2+p3+p4+p5

    if(ano=="1924" or ano=="1936" or ano=="1948" or ano=="1960" or ano=="1972" or ano=="1984" or ano=="1996" or ano=="2008" or ano=="2020"):
        s=str("Es Rata")
    elif(ano=="1925" or ano=="1937" or ano=="1949" or ano=="1961" or ano=="1973" or ano=="1985" or ano=="1997" or ano=="2009" or ano=="2021"):
        s=str("Es Buey")
    elif(ano=="1926" or ano=="1938" or ano=="1950" or ano=="1962" or ano=="1974" or ano=="1986" or ano=="1998" or ano=="2010" or ano=="2022"):
        s=str("Es Tigre")
    elif(ano=="1927" or ano=="1939" or ano=="1951" or ano=="1963" or ano=="1975" or ano=="1987" or ano=="1999" or ano=="2011" or ano=="2023"):
        s=str("Es Conejo")
    elif(ano=="1928" or ano=="1940" or ano=="1952" or ano=="1964" or ano=="1976" or ano=="1988" or ano=="2000" or ano=="2012" or ano=="2024"):
        s=str("Es Dragon")
    elif(ano=="1929" or ano=="1941" or ano=="1953" or ano=="1965" or ano=="1977" or ano=="1989" or ano=="2001" or ano=="2013" or ano=="2025"):
        s=str("Es Serpiente")
    elif(ano=="1930" or ano=="1942" or ano=="1954" or ano=="1966" or ano=="1978" or ano=="1990" or ano=="2002" or ano=="2014" or ano=="2026"):
        s=str("Es Caballo")
    elif(ano=="1931" or ano=="1943" or ano=="1955" or ano=="1967" or ano=="1979" or ano=="1991" or ano=="2003" or ano=="2015" or ano=="2027"):
        s=str("Es Cabra")
    elif(ano=="1932" or ano=="1944" or ano=="1956" or ano=="1968" or ano=="1980" or ano=="1992" or ano=="2004" or ano=="2016" or ano=="2028"):
        s=str("Es Mono")
    elif(ano=="1933" or ano=="1945" or ano=="1957" or ano=="1969" or ano=="1981" or ano=="1993" or ano=="2005" or ano=="2017" or ano=="2029"):
        s=str("Es Gallo")
    elif(ano=="1934" or ano=="1946" or ano=="1958" or ano=="1970" or ano=="1982" or ano=="1994" or ano=="2006" or ano=="2018" or ano=="2030"):
        s=str("Es Perro")
    elif(ano=="1935" or ano=="1947" or ano=="1959" or ano=="1971" or ano=="1983" or ano=="1995" or ano=="2007" or ano=="2019" or ano=="2031"):
        s=str("Es Cerdo")

    return render_template("Practica4R2SignoZodiacal.html",nombreC=nombreC, nombre=nombre, ap=ap, am=am,r=r,a=a,s=s)


if __name__=="__main__":
    app.run(debug=True,port=3000)

