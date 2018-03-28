import wifi

wifi_config_filename = 'wifi_config.json'

print('Enter boot.py')

print('Connect to wifi access point...')
addresses = wifi.connect_to_access_point(wifi_config_filename)
print('Done.')

if addresses:
    print('Wifi connection is established.')
    print('Open http://{}/ in your browser.'.format(addresses[0]))

print('Exit boot.py')
