mqtt_host = "IP_OR_DOMAIN"
mqtt_port = 1883
mqtt_topic = "screen/rpi"
mqtt_username = "USERNAME"
mqtt_password = "PASSWORD"
#On raspberry pi
power_on_command = "vcgencmd display_power 1"
power_off_command = "vcgencmd display_power 0"
#On other hdmi linux device:
#power_on_command = "xset -display :0 dpms force on"
#power_off_command = "xset -display :0 dpms force off"
