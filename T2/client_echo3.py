#!/usr/bin/python3
# Echo client program
# Version con dos threads: uno lee de stdin hacia el socket y el otro al revés
import jsockets
import sys, threading
import time


def Rdr(s, output_file, size):
    """Recibe datos del socket hasta paquete vacío (EOF) o timeout"""
    with open(output_file, 'wb') as f:
        s.settimeout(3.0)  # Timeout de 3 segundos
        while True:
            try:
                data = s.recv(size)
                if not data:  # Paquete vacío = EOF
                    break
                f.write(data)
            except:
                print("Timeout occurred - measurement invalid")
                break


def Sndr(s, input_file, size):
    """Envía datos desde el archivo al socket"""
    with open(input_file, 'rb') as f:
        while True:
            data = f.read(size)
            if not data:
                break
            s.send(data)
        # Envía paquete vacío para indicar EOF
        s.send(b'')


if len(sys.argv) != 6:
    print('Use: '+sys.argv[0]+' size IN OUT host port')
    sys.exit(1)

s = jsockets.socket_udp_connect(sys.argv[4], sys.argv[5])
if s is None:
    print('could not open socket')
    sys.exit(1)

size = int(sys.argv[1])
input_file = sys.argv[2]
output_file = sys.argv[3]

# Crear threads para enviar y recibir datos
receiver_thread = threading.Thread(target=Rdr, args=(s, output_file, size))
sender_thread = threading.Thread(target=Sndr, args=(s, input_file, size))

receiver_thread.start()
sender_thread.start()

# Esperar a que ambos threads terminen
sender_thread.join()
receiver_thread.join()

s.close()