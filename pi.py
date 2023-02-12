import requests,random, time
from datetime import datetime



sensorsList = ["Room", "Living Room", "Bathroom"]
doorList = ["open", "closed"]

def send_data():
    requests.post(f"http://127.0.0.1:5000/api/data?timestamp={timestamp}&sensorName={sensorName}&temperature={temperature}&light={light}&doorstatus={doorstatus}")

while True:
    timestamp = datetime.now().strftime("%H:%M:%S")
    sensorName = sensorsList[random.randint(0,2)]
    temperature = random.random() * 40
    light = random.randint(10, 20)
    doorstatus = doorList[random.randint(0,1)]
    print(timestamp, sensorName, temperature, light, doorstatus)
    send_data()
    time.sleep(4)