import firebase_admin
from firebase_admin import credentials, db as database

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://fir-course-ed2d0-default-rtdb.firebaseio.com/"
})

ref = database.reference("/data")


def push_Data(timestamp, sensor_name, temperature, light, doorstatus):
    data = {
        "time": timestamp,
        "name": sensor_name,
        "temperature": round(float(temperature), 2),
        "light": int(light),
        "doorstatus": doorstatus
    }
    ref.push(data)
    print("Successfully posted data")


def door_Count():
    data = ref.get()
    doorcount = 0
    for key, value in data.items():
        if value['doorstatus'] == 'open':
            doorcount += 1
    return doorcount

def sensor_info(sensorName):
    data = ref.get()
    sensor_info = []
    for key, value in data.items():
        if value['name'] == sensorName:
            sensor_info.append({"name": value["name"], "time": value["time"], "temperature": value["temperature"], "light": value["light"], "doorstatus": value["doorstatus"]})
    return sensor_info

def max_Light():
    query = ref.order_by_child("light").limit_to_last(1).get()
    return query
# push_Data("12:34:23", "bedroom", 23.4, 14, "open")


