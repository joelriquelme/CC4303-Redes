#!/usr/bin/python3
# Echo client program
# Cliente UDP con protocolo Stop-and-Wait para medición de performance
import jsockets
import sys, threading
from threading import Condition
import time

class ProtocolState:
    def __init__(self):
        self.condition = Condition()
        self.last_seq_received = -1
        self.timeout = None
        self.packets_sent = 0
        self.errors = 0


def Rdr(s, output_file, size, state):
    """Thread receptor que maneja el protocolo Stop-and-Wait"""
    with open(output_file, 'wb') as f:
        s.settimeout(3.0)  # Timeout de seguridad
        while True:
            try:
                data = s.recv(size)
                if not data:  # Esto no debería ocurrir con nuestro protocolo
                    break
                
                if len(data) < 3:  # Paquete inválido (debe tener al menos seqnum)
                    continue
                
                seqnum = int(data[:3].decode())
                payload = data[3:]
                
                with state.condition:
                    state.last_seq_received = seqnum
                    state.condition.notify()
                
                if not payload:  # EOF (solo seqnum)
                    break
                
                f.write(payload)
            except Exception as e:
                break


def Sndr(s, input_file, size, state):
    """Thread emisor que implementa Stop-and-Wait"""
    seqnum = 0 
    with open(input_file, 'rb') as f:
        while True:
            data = f.read(size)
            packet = f"{seqnum:03d}".encode() + (data if data else b'')

            retransmit = False
            while True:
                s.send(packet)
                if not retransmit:
                    state.packets_sent += 1
                else:
                    state.errors += 1
                
                with state.condition:
                    if state.condition.wait_for(
                        lambda: state.last_seq_received == seqnum, 
                        timeout=state.timeout
                    ):
                        break
                    else:
                        retransmit = True
            
            if not data:  # EOF enviado y confirmado
                break
            
            seqnum = (seqnum + 1) % 1000  # Secuencia 000-999


if len(sys.argv) != 7:
    print('Use: '+sys.argv[0]+' size timeout IN OUT host port')
    sys.exit(1)

if float(sys.argv[2]) > 3.0:
    print('Timeout too long, must be <= 3 seconds')
    sys.exit(1)

s = jsockets.socket_udp_connect(sys.argv[5], sys.argv[6])
if s is None:
    print('could not open socket')
    sys.exit(1)

size = int(sys.argv[1])
timeout = float(sys.argv[2])
input_file = sys.argv[3]
output_file = sys.argv[4]

state = ProtocolState()
state.timeout = timeout

# Crear threads para enviar y recibir datos
receiver_thread = threading.Thread(target=Rdr, args=(s, output_file, size+3, state))
sender_thread = threading.Thread(target=Sndr, args=(s, input_file, size, state))

receiver_thread.start()
sender_thread.start()

# Esperar a que ambos threads terminen
sender_thread.join()
receiver_thread.join()

s.close()

file_size = 0

try:
    file_size = len(open(input_file, 'rb').read())
except:
    pass

if state.packets_sent > 0:
    print(f"sent {state.packets_sent} packets, lost {state.errors}, {state.errors/state.packets_sent*100:.6f}%")