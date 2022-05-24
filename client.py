from http import client
from iiot_device import Sensor
import json
import time


# Creación de un objeto de la clase HTTPConnection
_conn = client.HTTPConnection(host='localhost', port=5000)

# Creación de un objeto de la clase Sensor
s = Sensor()

# Pa'a formar el JSON que se va al servidor
h = {'Content-type': 'application/json'}

while True:

    data = {
        'id' : 1,
        'name' : 'Temp_Sensor',
        'value' : s.get_random_number()
    }

    json_data = json.dumps(data)

    # Enviar los datos al servidor
    _conn.request('POST', '/devices', json_data, headers=h)
    _conn.close()


    print(s.get_random_number())
    #print(s.get_temp_wmi())
    time.sleep(.5)

