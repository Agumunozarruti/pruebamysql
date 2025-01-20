from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Configuración de MySQL
db = pymysql.connect(
    host="bmqqy9bjero3zbgiec1g-mysql.services.clever-cloud.com",  # Cambia a la IP de tu servidor MySQL si está en otro equipo
    user="u3cjnh3pnr3eiqfy",       # Usuario de MySQL
    password="RptvmV1gWizVZhFGGBvX",  # Contraseña de MySQL
    database="bmqqy9bjero3zbgiec1g"
)

@app.route('/insertar', methods=['POST'])
def send_data():
    try:
        # Obtener datos del ESP32
        data = request.json
        print("Datos recibidos:", data)  # Depuración
        
        temp = float(data['temperatura'])  # Convertir el valor recibido a flotante
        hum = float(data['humedad'])  # Convertir el valor recibido a flotante

        pre = float(data['presion'])  # Convertir el valor recibido a flotante

        
        
        # Insertar en la base de datos
        with db.cursor() as cursor:
            sql = "INSERT INTO mediciones_amp (temperatura, humedad, presion) VALUES (%s, %s ,%s)"
            cursor.execute(sql, (temp, hum, pre))  # Nota la coma para pasar un tuple
        db.commit()
        
        print("Guardado")
        return jsonify({"message": "Data inserted successfully!"}), 200
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
