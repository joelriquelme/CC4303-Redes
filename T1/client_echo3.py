#!/usr/bin/python3
# Echo client program
# Version con dos threads: uno lee de stdin hacia el socket y el otro al revés
import jsockets
import sys, threading
import time

class SharedCounter:
    """Clase para manejar un contador seguro entre threads"""
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def increment(self, amount):
        with self.lock:
            self.value += amount

    def get_value(self):
        with self.lock:
            return self.value

def Rdr(s, size, total_sent, done_event):
    """Recibe datos del socket hasta que se hayan recibido todos los bytes enviados"""
    bytes_received = 0
    while not done_event.is_set() or bytes_received <= total_sent.get_value():
        try:
            data = s.recv(size)
            if not data:
                break
            bytes_received += len(data)
        except:
            break

def Sndr(s, input_file, chunk_size, done_event, total_sent):
    """Envía datos desde el archivo al socket"""
    with open(input_file, 'rb') as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            s.send(data)
            total_sent.increment(len(data))
        s.shutdown(jsockets.socket.SHUT_WR)
        done_event.set()


if len(sys.argv) != 6:
    print('Use: '+sys.argv[0]+' size IN OUT host port')
    sys.exit(1)

s = jsockets.socket_tcp_connect(sys.argv[4], sys.argv[5])
if s is None:
    print('could not open socket')
    sys.exit(1)

size = int(sys.argv[1])
input_file = sys.argv[2]

# Variables compartidas
done_event = threading.Event()
total_sent = SharedCounter()

receiver_thread = threading.Thread(target=Rdr, args=(s, size, total_sent, done_event))
sender_thread = threading.Thread(target=Sndr, args=(s, input_file, size, done_event, total_sent))

receiver_thread.start()
sender_thread.start()

# Esperar a que ambos threads terminen
sender_thread.join()
receiver_thread.join()

s.close()