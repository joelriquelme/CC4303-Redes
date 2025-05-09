# T1 Joel Riquelme

## Descripción

Esta tarea contiene un cliente llamado `client_echo3.py`, diseñado para enviar y recibir datos de un servidor usando TCP. También incluye un script de experimentación (`experimento.sh`) que mide la eficiencia de transferencia de datos mediante diferentes tamaños de lectura/escritura y múltiples archivos en paralelo.

## Requisitos

- Python 3
- Servidor `server_echo3.py` en ejecución ya sea en `localhost` o en `anakena.dcc.uchile.cl`

## Ejecución 
El cliente se ejecuta con el siguiente comando:
```bash
./client_echo3.py <chunk_size> <input_file> <output_file> <host> <port>
```
Ejemplo:
```bash
time ./client_echo3.py 1024 archivo_500KB.txt salida.txt localhost 1818
```

## Ejecución del Experimento
El script `experimento.sh` realiza pruebas de transferencia de archivos grandes y pequeños para medir el desempeño.

### Pasos para ejecutar el experimento:
1. Dar permisos de ejecución al script:
   ```bash
   chmod +x experimento_anakena.sh
   chmod +x experimento_local.sh
   ```
2. Ejecutar el experimento:
   ```bash
   ./experimento.sh
   ```
3. Se generarán archivos de prueba y se ejecutarán las pruebas automáticamente.

4. Al finalizar, los archivos de prueba se eliminarán.

## Notas
- Si el script muestra errores de `bad interpreter`, convertir los archivos a formato UNIX con:
  ```bash
    sed -i 's/\r$//' experimento_anakena.sh
    sed -i 's/\r$//' experimento_local.sh
    sed -i 's/\r$//' client_echo3.py
  ```

- Se realizó el experimento solamente con 20 pequeños archivos en vez de 100, ya que el tiempo de creación de archivos se alargaba mucho.

# Resultados del experimento.

## Servidor Anakena

| Tamaño de archivo | Chunk Size | Tiempo real (s) |
|-----------------|------------|-----------|
| 500 KB          | 1024       | 0.144     |
| 25 KB           | 1024       | 0.159     |
| 25 KB           | 1024       | 0.175     |
| 25 KB           | 1024       | 0.174     |
| 25 KB           | 1024       | 0.179     |
| 25 KB           | 1024       | 0.178     |
| 25 KB           | 1024       | 0.182     |
| 25 KB           | 1024       | 0.188     |
| 25 KB           | 1024       | 0.186     |
| 25 KB           | 1024       | 0.191     |
| 25 KB           | 1024       | 0.284     |
| 25 KB           | 1024       | 0.292     |
| 25 KB           | 1024       | 0.294     |
| 25 KB           | 1024       | 0.297     |
| 25 KB           | 1024       | 0.298     |
| 25 KB           | 1024       | 0.300     |
| 25 KB           | 1024       | 1.292     |
| 25 KB           | 1024       | 1.294     |
| 25 KB           | 1024       | 1.291     |
| 500 KB          | 4096       | 0.142     |
| 25 KB           | 4096       | 0.196     |
| 25 KB           | 4096       | 0.198     |
| 25 KB           | 4096       | 0.205     |
| 25 KB           | 4096       | 0.211     |
| 25 KB           | 4096       | 0.211     |
| 25 KB           | 4096       | 0.211     |
| 25 KB           | 4096       | 0.214     |
| 25 KB           | 4096       | 0.218     |
| 25 KB           | 4096       | 0.219     |
| 25 KB           | 4096       | 0.220     |
| 25 KB           | 4096       | 0.220     |
| 25 KB           | 4096       | 0.221     |
| 25 KB           | 4096       | 0.231     |
| 25 KB           | 4096       | 0.233     |
| 25 KB           | 4096       | 0.239     |
| 25 KB           | 4096       | 0.236     |
| 25 KB           | 4096       | 0.236     |
| 25 KB           | 4096       | 0.236     |
| 25 KB           | 4096       | 0.436     |
| 25 KB           | 4096       | 1.228     |
| 500 KB          | 16384      | 0.177     |
| 25 KB           | 16384      | 0.180     |
| 25 KB           | 16384      | 0.179     |
| 25 KB           | 16384      | 0.180     |
| 25 KB           | 16384      | 0.179     |
| 25 KB           | 16384      | 0.182     |
| 25 KB           | 16384      | 0.181     |
| 25 KB           | 16384      | 0.181     |
| 25 KB           | 16384      | 0.184     |
| 25 KB           | 16384      | 0.181     |
| 25 KB           | 16384      | 1.243     |
| 25 KB           | 16384      | 1.243     |
| 25 KB           | 16384      | 1.246     |
| 25 KB           | 16384      | 1.251     |
| 25 KB           | 16384      | 1.256     |
| 25 KB           | 16384      | 1.256     |
| 25 KB           | 16384      | 1.255     |
| 25 KB           | 16384      | 3.672     |
| 25 KB           | 16384      | 3.677     |
| 25 KB           | 16384      | 3.676     |
| 25 KB           | 16384      | 3.680     |
| 500 KB          | 65536      | 0.165     |
| 25 KB           | 65536      | 0.169     |
| 25 KB           | 65536      | 0.171     |
| 25 KB           | 65536      | 0.171     |
| 25 KB           | 65536      | 0.174     |
| 25 KB           | 65536      | 0.183     |
| 25 KB           | 65536      | 0.183     |
| 25 KB           | 65536      | 0.182     |
| 25 KB           | 65536      | 0.186     |
| 25 KB           | 65536      | 0.188     |
| 25 KB           | 65536      | 0.302     |
| 25 KB           | 65536      | 0.300     |
| 25 KB           | 65536      | 0.303     |
| 25 KB           | 65536      | 0.301     |
| 25 KB           | 65536      | 0.301     |
| 25 KB           | 65536      | 0.296     |
| 25 KB           | 65536      | 1.452     |
| 25 KB           | 65536      | 1.453     |
| 25 KB           | 65536      | 1.463     |
| 25 KB           | 65536      | 1.462     |
| 25 KB           | 65536      | 1.463     |

## Servidor Local

| Tamaño de archivo | Chunk Size | Tiempo real (s) |
|-----------------|------------|-----------|
| 500 MB          | 1024       | 47.723    |
| 25 MB           | 1024       | 8.909     |
| 25 MB           | 1024       | 8.933     |
| 25 MB           | 1024       | 9.594     |
| 25 MB           | 1024       | 9.703     |
| 25 MB           | 1024       | 9.718     |
| 25 MB           | 1024       | 9.730     |
| 25 MB           | 1024       | 9.810     |
| 25 MB           | 1024       | 9.833     |
| 25 MB           | 1024       | 9.834     |
| 25 MB           | 1024       | 9.873     |
| 25 MB           | 1024       | 9.879     |
| 25 MB           | 1024       | 9.912     |
| 25 MB           | 1024       | 9.994     |
| 25 MB           | 1024       | 10.026    |
| 25 MB           | 1024       | 10.097    |
| 25 MB           | 1024       | 10.109    |
| 25 MB           | 1024       | 10.113    |
| 25 MB           | 1024       | 10.114    |
| 25 MB           | 1024       | 10.122    |
| 25 MB           | 1024       | 10.125    |
| 500 MB          | 4096       | 47.256    |
| 25 MB           | 4096       | 10.727    |
| 25 MB           | 4096       | 10.734    |
| 25 MB           | 4096       | 10.735    |
| 25 MB           | 4096       | 10.746    |
| 25 MB           | 4096       | 10.763    |
| 25 MB           | 4096       | 10.762    |
| 25 MB           | 4096       | 10.766    |
| 25 MB           | 4096       | 10.767    |
| 25 MB           | 4096       | 10.781    |
| 25 MB           | 4096       | 10.779    |
| 25 MB           | 4096       | 10.781    |
| 25 MB           | 4096       | 10.786    |
| 25 MB           | 4096       | 10.790    |
| 25 MB           | 4096       | 10.795    |
| 25 MB           | 4096       | 10.792    |
| 25 MB           | 4096       | 10.793    |
| 25 MB           | 4096       | 10.798    |
| 25 MB           | 4096       | 10.797    |
| 25 MB           | 4096       | 11.073    |
| 25 MB           | 4096       | 11.080    |
| 500 MB          | 16384      | 12.743    |
| 25 MB           | 16384      | 2.744     |
| 25 MB           | 16384      | 3.020     |
| 25 MB           | 16384      | 3.125     |
| 25 MB           | 16384      | 3.130     |
| 25 MB           | 16384      | 3.131     |
| 25 MB           | 16384      | 3.131     |
| 25 MB           | 16384      | 3.135     |
| 25 MB           | 16384      | 3.134     |
| 25 MB           | 16384      | 3.136     |
| 25 MB           | 16384      | 3.153     |
| 25 MB           | 16384      | 3.152     |
| 25 MB           | 16384      | 3.151     |
| 25 MB           | 16384      | 3.152     |
| 25 MB           | 16384      | 3.156     |
| 25 MB           | 16384      | 3.153     |
| 25 MB           | 16384      | 3.157     |
| 25 MB           | 16384      | 3.155     |
| 25 MB           | 16384      | 3.156     |
| 25 MB           | 16384      | 3.157     |
| 25 MB           | 16384      | 3.161     |
| 500 MB          | 65536      | 5.754     |
| 25 MB           | 65536      | 2.184     |
| 25 MB           | 65536      | 2.207     |
| 25 MB           | 65536      | 2.208     |
| 25 MB           | 65536      | 2.207     |
| 25 MB           | 65536      | 2.212     |
| 25 MB           | 65536      | 2.211     |
| 25 MB           | 65536      | 2.211     |
| 25 MB           | 65536      | 2.212     |
| 25 MB           | 65536      | 2.213     |
| 25 MB           | 65536      | 2.212     |
| 25 MB           | 65536      | 2.214     |
| 25 MB           | 65536      | 2.215     |
| 25 MB           | 65536      | 2.216     |
| 25 MB           | 65536      | 2.219     |
| 25 MB           | 65536      | 2.227     |
| 25 MB           | 65536      | 2.231     |
| 25 MB           | 65536      | 2.230     |
| 25 MB           | 65536      | 2.239     |
| 25 MB           | 65536      | 2.240     |
| 25 MB           | 65536      | 2.372     |

