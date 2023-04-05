import json
import hashlib

class Ejecuciones:
    def imprimir_parametros(self, id, nombre, contrasena):
        # Encriptar la contraseña con SHA-256
        hash_contrasena = hashlib.sha256(contrasena.encode('utf-8')).hexdigest()
        
        # Crear un diccionario con los parámetros recibidos y la contraseña encriptada
        usuario = {
            "id": id,
            "nombre": nombre,
            "contrasena": hash_contrasena
        }
        
        # Abrir el archivo "usuario.txt" en modo append
        with open("usuario.txt", "a") as f:
            # Convertir el diccionario a formato JSON y escribirlo en el archivo
            json.dump(usuario, f)
            f.write("\n")
        
        # Imprimir los parámetros en la consola
        print("id:", id)
        print("nombre:", nombre)
        print("contrasena:", "*" * len(contrasena))
        
    def imprimir_usuarios(self):
        # Abrir el archivo "usuario.txt" en modo lectura
        with open("usuario.txt", "r") as f:
            # Leer cada línea del archivo y cargarla como un diccionario JSON
            for linea in f:
                usuario = json.loads(linea)
                # Desencriptar la contraseña y mostrarla en la consola
                contrasena = hashlib.sha256(usuario["contrasena"].encode('utf-8')).hexdigest()
                print("id:", usuario["id"])
                print("nombre:", usuario["nombre"])
                print("contrasena:", "*" * len(contrasena))
                print()




