import DataPanelGUI

sub_topics = ("Temperature", "Humidity", "Pressure")
sub = DataPanelGUI.DataPanelGUI("mqtt.eclipseprojects.io", "Subscriber", sub_topics)
sub.start()


while True:
    sub.check_exit()



