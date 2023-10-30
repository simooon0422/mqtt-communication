import DataPanel

sub_topics = ("Temperature", "Humidity", "Pressure")
sub = DataPanel.DataPanel("mqtt.eclipseprojects.io", "Subscriber", sub_topics, True)
sub.start()


while True:
    pass



