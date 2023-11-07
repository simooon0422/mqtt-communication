import DataPanelGUI
import DataPanel
import time

sub_topics = ("Temperature", "Humidity", "Pressure")
# sub = DataPanel.DataPanel("mqtt.eclipseprojects.io", "Subscriber", sub_topics)
subGUI = DataPanelGUI.DataPanelGUI("mqtt.eclipseprojects.io", "Subscriber", sub_topics)

subGUI.start()

while True:
    subGUI.check_exit()
    print(subGUI.get_values())
    time.sleep(1)



