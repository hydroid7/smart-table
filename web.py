import gc


def web_page(conn, state):
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Last-Modified: Wed, 21 Oct 2015 07:28:00 GMT\n')
    conn.send('Connection: close\n\n')
    with open('index.html') as __index_html:
        for line in __index_html:
            conn.send(line)
            gc.collect()
        conn.close()


def result(led_values):
    return """
        <h1>Succesful set the stuff</h1>
    """


def error(err):
    return """
            <h1>Some error happended. The stacktrace is:</h1>
            <b>
        """ + repr(err) + """
            </b>
        """
