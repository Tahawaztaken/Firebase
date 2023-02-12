from flask import Flask, request
import firebase

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def post_Data():
    timestamp = request.args.get("timestamp")
    sensorName = request.args.get("sensorName")
    temperature = request.args.get("temperature")
    light = request.args.get("light")
    doorstatus = request.args.get("doorstatus")
    firebase.push_Data(timestamp, sensorName, temperature, light, doorstatus)

    return "OK"


@app.route('/api/dooropencount')
def get_doorcount():
    doorcount = firebase.door_Count()
    return {"doors_open": doorcount}

@app.route('/api/bysensor/<sensorName>')
def get_sensorInfo(sensorName):
    sensorList = firebase.sensor_info(sensorName)
    return str(sensorList)


@app.route('/api/maxLight')
def get_max_light():
    return firebase.max_Light()

if __name__ == '__main__':
    app.run(debug=True)