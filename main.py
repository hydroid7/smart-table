try:
    import usocket as socket
except:
    import socket

import ure
import tableController
import web
import gc

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
gc.collect()

while True:
    try:
        conn, addr = s.accept()
        # print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request)
        # print('Content = %s' % request)
        config = ure.search(r'\/tables\/led\/(\d-\d-\d)', request)
        gc.collect()
        if config is not None:
            values = config.group(1).split('-')
            values = [int(v) for v in values]
            try:
                led_values = tableController.set_table_state(values[0], values[1], values[2])
                response = web.result(led_values)
            except Exception as e:
                response = web.error(e)
                conn.send('HTTP/1.1 200 OK\n')
                conn.send('Content-Type: text/html\n')
                conn.send('Connection: close\n\n')
                conn.sendall(response)
                conn.close()
        else:
            gc.collect()
            print(gc.mem_free())
            print("Returning web page.")
            web.web_page(conn, tableController.get_table_state())
        gc.collect()
    except:
        gc.collect()
