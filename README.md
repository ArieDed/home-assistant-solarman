Original forked from [KodeCR](https://github.com/KodeCR/home-assistant-solarman), I updated it to work witht the latest home assistant version and to make the setup documentation more clear.

# Home Assistant custom component for SolarMAN (IGEN Tech) solar inverter logger
Uses a local push connection by setting up a server listing for packages from the logger, parsing the data, and updating the relevant sensors.

Tested with a Trannergy solar inverter, but probably works with any inverter using a SolarMAN (IGEN Tech) logger.

## Setup
Clone or download the repo, and copy the "solarman" folder in "custom_components" to the "custom_components" folder in home assistant.

After that, the folder structure should look as follows:

```
custom_components
├── solarman  
│   ├── __init__.py  
│   ├── config_flow.py  
│   ├── const.py
│   ├── manifest.json
│   ├── sensor.py
│   ├── strings.json
├── {other components}
```

Restart home assistant and go to Settings -> Devices & Services. add a new integration and search for solarMAN logger. 

![Addon settings](https://github.com/user-attachments/assets/55887779-efa6-4d75-a618-0c9abde5335b)

For "Host" you use the local IP address of your home assistant server, for example `192.168.1.100` and for the port any port that is still open on your home assistant server, for example `8899`. After that, click submit and you are done within home assistant. Now all is left is to point one of the remote server connections on the Solarman local page to your home assistant server. 

Find the IP address of your solarman logger and go there in a webbrowser. login with username `admin` and password `admin`. Next, go to tab "Advanced" -> "Remote Server". In one of the server entries fill in the IP address of your home assistant server and the port you have chosen when setting up the addon. Save and restart and after a little while the entities created by the addon in home assistant will receive data.

## Acknowlegements
Thanks to @rhmswink for figuring out how to parse the incoming data, as found here: https://github.com/rhmswink/omnik_monitor and to @KodeCR for making the initial code for the home assistant addon.
