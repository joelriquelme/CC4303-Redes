#!/bin/bash

# Configuración
target_host="anakena.dcc.uchile.cl"  # Cambiar a anakena.dcc.uchile.cl si es necesario
port=1818  # Puerto del servidor
client_script="./client_echo3.py"  # Cliente a usar
test_file="testfile"  # Base del nombre de archivos
chunk_sizes=(1024 4096 16384 65536)  # Distintos tamaños de lectura/escritura

echo "Preparando archivos de prueba..."
python3 create_files.py "$test_file" 2621440 # 50 MB para localhost
python3 create_files.py "smallfile" 25600 20  # 20 archivos de 2.5 MB (total ~50 MB)

echo -e "\n=== INICIANDO EXPERIMENTOS ===\n"

for chunk in "${chunk_sizes[@]}"; do
    echo -e "\n Prueba con archivo grande y chunk size = $chunk bytes"
    time $client_script $chunk "testfile_1" "salida_large_$chunk.txt" "$target_host" $port

echo -e "\n Prueba con 20 archivos pequeños en paralelo y chunk size = $chunk bytes"
    for i in {1..20}; do
        (time $client_script $chunk "smallfile_$i" "salida_small_${chunk}_$i.txt" "$target_host" $port) &
    done
    wait  # Esperar a que terminen todas las transferencias

done

echo -e "\n Eliminando archivos de prueba..."
rm -f "testfile_1" smallfile_* salida_large_* salida_small_* out_small_*

echo -e "\n Experimentos finalizados."
