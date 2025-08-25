import os
from flask import Flask, render_template, request, send_file, jsonify, make_response
from dotenv import load_dotenv
from modules import get_employees, get_projects,get_records, get_report, write_report

#Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("CLOCKIFY_API_KEY")
WORKSPACE_ID = os.getenv("CLOCKIFY_WORKSPACE_ID")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar-reporte', methods=['POST'])
def generar_repote():

    #Obtiene las fechas del formulario
    data = request.get_json()
    fecha_inicio = data.get('fechaInicio')
    fecha_fin = data.get('fechaFin')

    #Consulta la base de datos de colaboradores
    try:
        empleados = get_employees()
        #Convierte el email en minuscula
        empleados = [{**empleado, 'Email': empleado['Email'].lower()} for empleado in empleados]
    except RuntimeError as e:
        return jsonify({'error': str(e)}), 500
    
    #Consulta los proyectos de Clockify
    try:
        proyectos = get_projects()
    except RuntimeError as e:
        return jsonify({'error': str(e)}), 500
    
    #Consulta los registros de tiempo
    try:
        registros = get_records(fecha_inicio, fecha_fin)
    except RuntimeError as e:
        return jsonify({'error': str(e)}), 500
    
    #Genera el prorrateo
    try:
        reporte = get_report(empleados,proyectos, registros,fecha_inicio, fecha_fin)
    except RuntimeError as e:
        return jsonify({'error': str(e)}), 500
    
    #Asigna el nombre del archivo
    if fecha_inicio.split('-')[1] == "01":
        prorrateo_nombre = "PRORRATEO_ENE"
    elif fecha_inicio.split('-')[1] == "02":
        prorrateo_nombre = "PRORRATEO_FEB"
    elif fecha_inicio.split('-')[1] == "03":
        prorrateo_nombre = "PRORRATEO_MAR"
    elif fecha_inicio.split('-')[1] == "04":
        prorrateo_nombre = "PRORRATEO_ABR"
    elif fecha_inicio.split('-')[1] == "05":
        prorrateo_nombre = "PRORRATEO_MAY"
    elif fecha_inicio.split('-')[1] == "06":
        prorrateo_nombre = "PRORRATEO_JUN"
    elif fecha_inicio.split('-')[1] == "07":
        prorrateo_nombre = "PRORRATEO_JUL"
    elif fecha_inicio.split('-')[1] == "08":
        prorrateo_nombre = "PRORRATEO_AGO"
    elif fecha_inicio.split('-')[1] == "09":
        prorrateo_nombre = "PRORRATEO_SEP"
    elif fecha_inicio.split('-')[1] == "10":
        prorrateo_nombre = "PRORRATEO_OCT"
    elif fecha_inicio.split('-')[1] == "11":
        prorrateo_nombre = "PRORRATEO_NOV"
    elif fecha_inicio.split('-')[1] == "12":
        prorrateo_nombre = "PRORRATEO_DIC"

    reporte["Nombre Prorrateo"] = [prorrateo_nombre] * len(reporte["Id colaborador"])

    #Escribe el archivo XLSX
    try:
        output, nombre_archivo = write_report(reporte)
    except RuntimeError as e:
        return jsonify({'error': str(e)}), 500

    return send_file(
        output,
        as_attachment=True,
        download_name="PEDELTA_PRORRATEO_CLOCKIFY.xlsx",
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

if __name__ == '__main__':
    app.run(debug=True)
