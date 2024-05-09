from pyXBDM import XBDM

xbox = XBDM('192.168.0.98')

xbox.connect()

if xbox.connected:
    xbox.disconnect()
