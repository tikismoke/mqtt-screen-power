# MQTT Screen Power

MQTT Client written in Python for turning HDMI screen power on and off.
Made for the Rapsberry Pi 3B+ which is using a third-party touch screen which
 does not completely switch off the screen with screensaver / power saving

## Usage

- Copy `config.template.py` to `config.py` and change the properties to
 your MQTT setup/preferences

- Install `paho-mqtt`

  ```bash
  pip install paho-mqtt
  ```

- Run

  ```bash
  python paho-mqtt
  ```

## Example use in [Home Assistant](https://www.home-assistant.io)

```yaml
switch:
  - platform: mqtt
    name: "Touch Panel"
    icon: mdi:tablet
    command_topic: "screen/rpi"
    payload_on: 'on'
    payload_off: 'off'
```

## Adding systemd service

Create /etc/systemd/system/motion-hdmi.service
Paste this code:

```
[Unit]
Description=Mqtt hdmi Service
After=multi-user.target

[Service]
Type=idle
Environment=XAUTHORITY=/home/pi/.Xauthority
ExecStart=/usr/bin/python3 /home/pi/mqtt-screen-power/main.py &
Restart=always

[Install]
WantedBy=multi-user.target

```
Then run as root or using sudo those command line:
```bash
#systemctl daemon-reload
#systemctl enable motion-hdmi.service
#systemctl start motion-hdmi.service
```
