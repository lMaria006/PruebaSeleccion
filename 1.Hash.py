import hashlib


nombre = input("Ingrese su nombre:")

hash = hashlib.sha256(nombre.encode()).hexdigest()

print(f"El hash para el '{nombre}' es: '{hash}'")