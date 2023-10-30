import devices


mqtt_broker = "mqtt.eclipseprojects.io"


sensor_t = devices.TemperatureSensor(mqtt_broker, "Temperature")
sensor_h = devices.HumiditySensor(mqtt_broker, "Humidity")
sensor_p = devices.PressureSensor(mqtt_broker, "Pressure")
sensor_t.start()
sensor_h.start()
sensor_p.start()

while True:
    pass
