try:
    import usocket as socket
except:
    import socket

import network

import esp

esp.osdebug(None)

import gc

gc.collect()

ssid = 'SmartTable'
password = '0000'

station = network.WLAN(network.AP_IF)
station.active(True)
station.config(essid=ssid, password=password)
#
# while station.isconnected() == False:
#   pass
#
print('Wlan Station successful')
print(station.ifconfig())


gc.collect()
