from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route('/form1', methods=['GET', 'POST'])
def form1():
    resultado = None
    if request.method == 'POST':
        dato1 = request.form.get("dato1")
        dato2 = request.form.get("dato2")
        dato3 = request.form.get("dato3")
        asistencia = request.form.get("asistencia")
        
        if all([dato1, dato2, dato3, asistencia]) and all(x.isdigit() for x in [dato1, dato2, dato3, asistencia]):
            resultado = procesar_dato1(int(dato1), int(dato2), int(dato3), int(asistencia))
        else:
            resultado = 'Ingrese un número válido'
    return render_template('form1.html', resultado=resultado)

@app.route('/form2', methods=['GET', 'POST'])
def form2():
    resultado = None
    if request.method == 'POST':
        dato4 = request.form.get('dato4')
        dato5 = request.form.get('dato5')
        dato6 = request.form.get('dato6')

        if dato4 and dato5 and dato6:
            resultado = procesar_dato2(dato4, dato5, dato6)
        else:
            resultado = 'Ingrese nombres válidos en los tres campos.'
            
    return render_template('form2.html', resultado=resultado)





def procesar_dato1(dato1,dato2,dato3,asistencia):
    
    promedio = dato1 + dato2 + dato3
    
    promedio= promedio / 3

    if asistencia > 75:
        if promedio > 40:
            return f'El Resultado es: {promedio}. Felicidades, Aprobaste por asistencia y por tus notas!!'
        else:
                return f'Lamentablemente reprobaste solo por tus bajas notas'
    else:
        if asistencia < 75:
            if promedio < 40:
                return f'El Resultado es: {promedio}. Reprobaste por tu asistencia y notas bajas'
            else:
                return f'El Resultado es: {promedio}. Reprobaste por tu asistencia'
        else:
            return f'El Resultado es: {promedio}. Reprobaste por tu asistencia'
def procesar_dato2(dato4, dato5, dato6):
    nombre_mas_largo = max([dato4, dato5, dato6], key=len)
    cantidad_caracteres = len(nombre_mas_largo)
    return f'El nombre más largo es "{nombre_mas_largo}" con {cantidad_caracteres} caracteres.'


if __name__ == '__main__':
    app.run()
