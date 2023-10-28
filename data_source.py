import time
import devices


t_sens = devices.TemperatureSensor("mqtt.eclipseprojects.io", "Temperature")

t_sens.start()
time.sleep(5)
t_sens.stop()


while True:
    pass
