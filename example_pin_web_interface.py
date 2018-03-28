import socket
import machine


def run_led_server(pin_id=26, tcp_port=80):
    html = """<html>
<head> <title>LED</title> </head>
<center>
<h2>MicroPythonは多分いいぞ...!!</h2>
<form>
LED {pin_id}番ポート
<button name="LED" value="ON_{pin_id}" type="submit">ON</button>
<button name="LED" value="OFF_{pin_id}" type="submit">OFF</button><br><br>
</form>
</center>
</html>
""".format(pin_id=pin_id)

    led = machine.Pin(pin_id, machine.Pin.OUT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', tcp_port))
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        req = conn.recv(1024)
        req = str(req, 'utf-8')
        print('request:', req)

        query = req.split(' ')[1]
        print(query)
        is_led_on = req.find('GET /?LED=ON_{}'.format(pin_id)) == 0
        is_led_off = req.find('GET /?LED=OFF_{}'.format(pin_id)) == 0
        print('is_led_on:', is_led_on)
        print('is_led_off:', is_led_off)
        if is_led_on:
            led.value(1)
            print('entered led_on')
        if is_led_off:
            led.value(0)
            print('entered led_off')
        response = html
        conn.send(response)
        conn.close()
