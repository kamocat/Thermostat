# Thermostat
Thermostat control via Raspberry Pi and Google Calendar

## Systemd setup
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


Based off the Google Calendar Python Quickstart

Complete the steps described in the [Google Calendar Python Quickstart](
https://developers.google.com/google-apps/calendar/quickstart/python), and in
about five minutes you'll have a simple Python command-line application that
makes requests to the Google Calendar API.

## Install

```
pip install -r requirements.txt
```

## Run

```
python quickstart.py
```
