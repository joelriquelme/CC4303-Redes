import os
import sys

def create_file(filename, size_in_bytes):
    """Crea un archivo con el tamaño especificado en bytes."""
    with open(filename, 'wb') as f:
        f.write(os.urandom(size_in_bytes))

def create_multiple_files(base_filename, size_in_bytes, count):
    """Crea múltiples archivos con nombres secuenciales."""
    for i in range(count):
        filename = f"{base_filename}_{i+1}"
        create_file(filename, size_in_bytes)

if __name__ == "__main__":
    if len(sys.argv) not in [3, 4]:
        print("Uso: python create_file.py <nombre_base_archivo> <tamaño_en_bytes> [cantidad]")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        size = int(sys.argv[2])
        if size <= 0:
            raise ValueError("El tamaño debe ser un número positivo.")
        count = int(sys.argv[3]) if len(sys.argv) == 4 else 1
        if count <= 0:
            raise ValueError("La cantidad debe ser un número positivo.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    create_multiple_files(filename, size, count)