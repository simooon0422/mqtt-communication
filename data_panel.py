import DataPanelGUI
import DataPanel
import time

sub_topics = ("Temperature", "Humidity", "Pressure")
sub = DataPanel.DataPanel("mqtt.eclipseprojects.io", "Subscriber", sub_topics)
# subGUI = DataPanelGUI.DataPanelGUI("mqtt.eclipseprojects.io", "Subscriber", sub_topics)

sub.start()


while True:
    print(sub.get_values())
    time.sleep(1)



