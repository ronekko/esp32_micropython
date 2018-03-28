import network
import ujson

import exception


def connect_to_access_point(wifi_config_filename='wifi_config.json'):
    try:
        with open(wifi_config_filename) as f:
            json = f.read()
    except OSError:
        raise exception.FileNotFoundError(wifi_config_filename)

    config = ujson.loads(json)
    ssid = config['ssid']
    password = config['key']

    station = network.WLAN(network.STA_IF)

    if station.isconnected():
        print('connection already exists')
        return station.ifconfig()

    station.active(True)
    station.connect(ssid, password)

    while not station.isconnected():
        pass

    print('established a new connection')
    return station.ifconfig()
