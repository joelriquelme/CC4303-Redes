#!/bin/bash

# Configuración
target_host="localhost"
port=1818  # Puerto del servidor
client_script="./client_echo3.py"  # Cliente a usar
test_file="testfile"  # Base del nombre de archivos
chunk_sizes=(1024 4096 16384 32768)  # Distintos tamaños de lectura/escritura
results_file="resultados_experimento_local.txt"  # Archivo para guardar resultados

# Función para obtener el tamaño de un archivo en formato legible
get_file_size() {
    ls -lh "$1" | awk '{print $5}'
}

# Función para registrar resultados
log_result() {
    echo -e "$1" | tee -a "$results_file"
}

# Inicializar archivo de resultados
echo "Resultados del Experimento - $(date)" > "$results_file"
echo "=================================" >> "$results_file"

echo "Preparando archivos de prueba..."
python3 create_files.py "$test_file" 524288000 # 500 MB para localhost
python3 create_files.py "smallfile" 10485760 50  # 50 archivos de 10 MB (total ~500 MB)

echo -e "\n=== INICIANDO EXPERIMENTOS ===\n"

for chunk in "${chunk_sizes[@]}"; do
    log_result "\n--- Prueba con chunk size = $chunk bytes ---"
    
    # Prueba con archivo grande
    log_result "\n[Archivo grande]"
    time $client_script $chunk "testfile_1" "salida_large_$chunk" "$target_host" $port
    
    # Registrar tamaño del archivo recibido
    if [ -f "salida_large_$chunk" ]; then
        original_size=$(stat -c%s "testfile_1")
        received_size=$(stat -c%s "salida_large_$chunk")
        percentage=$((received_size * 100 / original_size))
        log_result "Tamaño original: $(get_file_size testfile_1) ($original_size bytes)"
        log_result "Tamaño recibido: $(get_file_size salida_large_$chunk) ($received_size bytes)"
        log_result "Porcentaje recibido: $percentage%"
    else
        log_result "ERROR: No se generó archivo de salida"
    fi

    # Prueba con 50 archivos pequeños en paralelo
    log_result "\n[50 archivos pequeños]"
    total_received=0
    total_expected=0
    
    for i in {1..50}; do
        (time $client_script $chunk "smallfile_$i" "salida_small_${chunk}_$i" "$target_host" $port) &
    done
    wait  # Esperar a que terminen todas las transferencias

    # Calcular estadísticas de los archivos pequeños
    for i in {1..50}; do
        if [ -f "salida_small_${chunk}_$i" ]; then
            original_size=$(stat -c%s "smallfile_$i")
            received_size=$(stat -c%s "salida_small_${chunk}_$i")
            total_expected=$((total_expected + original_size))
            total_received=$((total_received + received_size))
        fi
    done

    if [ $total_expected -gt 0 ]; then
        percentage=$((total_received * 100 / total_expected))
        log_result "Total esperado: $((total_expected/1024/1024)) MB ($total_expected bytes)"
        log_result "Total recibido: $((total_received/1024/1024)) MB ($total_received bytes)"
        log_result "Porcentaje total recibido: $percentage%"
    else
        log_result "ERROR: No se recibió ningún archivo pequeño"
    fi
done

echo -e "\n Eliminando archivos de prueba..."
rm -f "testfile_1" smallfile_* salida_large_* salida_small_* out_small_*

echo -e "\n=== RESUMEN FINAL ==="
cat "$results_file"
echo -e "\nResultados detallados guardados en: $results_file"
echo -e "\nExperimentación finalizada."
