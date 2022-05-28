from random import randint
#import psutil
#import wmi

#POO en Python
#Definición de la clase
class Sensor:

    #Constructore de la clase
    def __init__(self):
        #Funciona para linux
        #self._sensor = psutil.cpu_percent()
        # Funciona para windows
        #self._wmi = wmi.WMI(namespace='root\OpenHardwareMonitor')
        pass

    def get_temp(self):
        return self._sensor['coretemp']

    #Simular la toma de algún valor de otro sensor
    def get_random_number(self):
        return randint(0, 50)


    '''def get_temp_wmi(self):
        return self._wmi.SensorType['Temperature']'''
        