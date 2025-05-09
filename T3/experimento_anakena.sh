#!/bin/bash

# Configuración
target_host="anakena.dcc.uchile.cl"
port=1818
client_script="./client_bw.py"
test_file="testfile"
timeouts=(0.05 0.1 0.5 1.0)  # Diferentes timeouts a probar
chunk_sizes=(128 256 512 1024)  # Distintos tamaños de chunk
results_file="resultados_anakena.txt"

# Función para obtener el tamaño de un archivo en formato legible
get_file_size() {
    ls -lh "$1" | awk '{print $5}'
}

# Función para registrar resultados
log_result() {
    echo -e "$1" | tee -a "$results_file"
}

# Inicializar archivo de resultados
echo "Resultados Tarea 3 - Localhost - $(date)" > "$results_file"
echo "Protocolo Stop-and-Wait" >> "$results_file"
echo "=================================" >> "$results_file"

echo "Preparando archivos de prueba..."
python3 create_files.py $test_file 524288 # 500 KB para anakena 524288


echo -e "\n=== INICIANDO EXPERIMENTO ===\n"

for chunk in "${chunk_sizes[@]}"; do
    for timeout in "${timeouts[@]}"; do
        log_result "\n--- Prueba con chunk: $chunk bytes, timeout: $timeout s ---"
        
        # Prueba con archivo grande
        {
            # Capturar el output y el tiempo de ejecución
            time_output=$( { time $client_script $chunk $timeout "testfile_1" "salida_large_${chunk}_${timeout}" "$target_host" $port; } 2>&1 )
            echo "$time_output"
        } | tee -a "$results_file"
        
        # Registrar tamaño del archivo recibido
        if [ -f "salida_large_${chunk}_${timeout}" ]; then
            original_size=$(stat -c%s "testfile_1")
            received_size=$(stat -c%s "salida_large_${chunk}_${timeout}")
            percentage=$((received_size * 100 / original_size))
            log_result "Tamaño original: $(get_file_size testfile_1) ($original_size bytes)"
            log_result "Tamaño recibido: $(get_file_size salida_large_${chunk}_${timeout}) ($received_size bytes)"
            log_result "Porcentaje recibido: $percentage%"
        else
            log_result "ERROR: No se generó archivo de salida"
        fi
    done
done

echo -e "\nEliminando archivos de prueba..."
rm -f testfile_* smallfile_* salida_large_* salida_small_* out_small_*

echo -e "\nResultados detallados guardados en: $results_file \n"
