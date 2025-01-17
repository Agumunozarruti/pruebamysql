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

@app.route('/send-data', methods=['POST'])
def send_data():
    # Obtener datos del ESP32
    try:
        data = request.json
        value = data.get("valor")
        value = "{:.2f}".format(value)

   
        with db.cursor() as cursor:
            sql = "INSERT INTO readings (value) VALUES (%s, %s)"
            cursor.execute(sql, (value))
        db.commit()
        return jsonify({"message": "Data inserted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
