import os
import sys

def create_file(filename, size_in_bytes):
    """Crea un archivo con el tamaño especificado en bytes."""
    with open(filename, 'wb') as f:
        f.write(os.urandom(size_in_bytes))
    print(f"Archivo '{filename}' creado con {size_in_bytes} bytes.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python create_file.py <nombre_archivo> <tamaño_en_bytes>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        size = int(sys.argv[2])
        if size <= 0:
            raise ValueError("El tamaño debe ser un número positivo.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    create_file(filename, size)