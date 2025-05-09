# T2 Joel Riquelme

## Descripción

Esta tarea contiene un cliente llamado `client_echo3.py`, diseñado para enviar y recibir datos de un servidor usando TCP. También incluye un script de experimentación (`experimento_local.sh` y `experimento_anakena.sh`) que mide la eficiencia de transferencia de datos mediante diferentes tamaños de lectura/escritura y múltiples archivos en paralelo.

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
time ./client_echo3.py 1024 archivo_500KB salida localhost 1818
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
   ./experimento_local.sh
   ./experimento_anakena.sh
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

- Se realizó el experimento solamente con 50 pequeños archivos en vez de 100, ya que con más de 50 empezaba a tener errore.

## Resultados

Los resulados de la experimentación se encuentran en los archivos `resultados_local.txt` y `resultados_anakena.txt`. Estos archivos contienen las métricas de tiempo y eficiencia de transferencia para diferentes configuraciones de chunk size y número de archivos.

## Preguntas

### P1

**Si el archivo de salida es más pequeño que el de entrada, ¿es correcto medir el ancho de banda disponible como tamaño recibido/tiempo?**

Sí, es correcto medir el ancho de banda disponible como tamaño recibido/tiempo, ya que el tamaño recibido representa la cantidad de datos que efectivamente se han transferido y el tiempo es el intervalo en el cual se realizó la transferencia. 

### P2

**Si el archivo de salida es más pequeño que el de entrada, ¿es correcto medir el ancho de banda disponible como tamaño enviado/tiempo?**

No, es incorrecto medir el ancho de banda disponible como tamaño enviado/tiempo, ya que el tamaño enviado no refleja la cantidad de datos que realmente se han transferido y puede incluir datos que no fueron recibidos correctamente como paquetes perdidos o errores de transmisión.

### P3

**Una medición que termina por timeout, ¿podría usarse de alguna forma para medir el ancho de banda disponible?**

No, una medición que termina por timeout no puede usarse para medir el ancho de banda disponible, ya que un timeout indica que la transferencia no se completó correctamente y no se puede determinar la cantidad de datos transferidos ni el tiempo real de transferencia. El tiempo puede variar totalmente si se configura un timeout muy alto o muy bajo, lo que afectaría la medición del ancho de banda. Además, el timeout puede ser causado por problemas de red o congestión, lo que hace que la medición no sea representativa del ancho de banda real disponible.

## Comparación de resultados con T1

Los resultados de la T2 son en general más lentos, lo cual no tiene mucho sentido si tomamos en cuenta que TCP es más lento que UDP. Sin embargo estos resultados no pueden ser comparados directamente, ya que en la T1 se utilizó un PC distinto y otras conexiones a red. 

Para la primera tarea los experimentos se corrieron en un Notebook y en la red del DCC, por lo que en ese aspecto tiene sentido que sean menores los tiempos en anakena. En cuanto a los resultados en local, una posible explicación puede ser el sistema operativo o la terminal ocupada. Los setups para la T1 y T2 son totalmente distintos.