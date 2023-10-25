import socket
import threading

# Configuración del socket del Cliente P2P (Nodo 1)
direccion_nodo2 = "127.0.0.1"  # Deja la dirección IP como "127.0.0.1" para la misma máquina
puerto_nodo2 = 9091  # Puerto diferente al del Nodo 1

socket_nodo1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_nodo1.bind(("0.0.0.0", 9090))
socket_nodo1.listen()

print("Esperando conexión del Nodo 2...")
socket_nodo2, addr = socket_nodo1.accept()
print("Conectado con el Nodo 2", addr)

# Función para enviar mensajes a otro nodo
def enviar_mensaje():
    while True:
        mensaje = input("Tú: ")
        socket_nodo2.send(mensaje.encode())
        if mensaje.lower() == "adios":
            break

# Función para recibir mensajes de otro nodo
def recibir_mensaje():
    while True:
        mensaje = socket_nodo2.recv(4096).decode()
        print("Nodo 2: " + mensaje)
        if mensaje.lower() == "adios":
            break

# Iniciar hilos para enviar y recibir mensajes
thread_enviar = threading.Thread(target=enviar_mensaje)
thread_recibir = threading.Thread(target=recibir_mensaje)

thread_enviar.start()
thread_recibir.start()






