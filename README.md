# Thermostat
Thermostat control via Raspberry Pi and Google Calendar

## Hardare
- Raspberry Pi
- Pi-compatible LCD display. (It should plug into the GPIO headers)
- Temperature sensor (I used an attiny26 to read a thermistor and send the value over serial)
- 3.3v Relay to switch the heater controls

## Install
```
pip install -r requirements.txt
```

## Run
We can't run Pygame over SSH, so instead we run it as a systemd service.
```
sudo cp thermostat.service /etc/systemd/system/
sudo sysmemctl daemon-reload
sudo systemctl enable thermostat
sudo systemctl start thermostat
```
To reload the service for testing changes, try
```
sudo systemctl restart thermostat
```

