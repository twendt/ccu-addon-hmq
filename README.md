# ccu-addon-hmq

[hmq](https://github.com/fhmq/hmq) als Addon für die
[Homematic CCU3](https://www.eq-3.de/produkte/homematic/zentralen-und-gateways/smart-home-zentrale-ccu3.html) und 
[RaspberryMatic](https://github.com/jens-maus/RaspberryMatic)

Unter [Releases](https://github.com/twendt/ccu-addon-hmq/releases) steht die Datei 
`hmq-<version>.tar.gz` zum Download zur Verfügung, diese kann über das CCU WebUI als Zusatzsoftware installiert
werden.

Auf der CCU3 sind anschließend noch die notwendigen Ports freizugeben. Die Freigabe erfolgt unter Einstellungen > Systemsteuerung > Firewall konfigurieren. Dort trägt man im Feld "Port-Freigabe" z.B. "1883" ein. 

Neustart via `/etc/config/rc.d/hmq restart`.

Per default lauscht hmq auf den Ports 1883/mqtt.


## Credits

hmq Project (https://github.com/fhmq/hmq)

Thanks to hobbyquakers [ccu-addon-mosquitto](https://github.com/hobbyquaker/ccu-addon-mosquitto). The repo was used as a base for this repo.
