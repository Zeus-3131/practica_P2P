import socket
import threading

# Configuración del socket del Cliente P2P (Nodo 2)
direccion_nodo1 = "127.0.0.1"  # Deja la dirección IP como "127.0.0.1" para la misma máquina
puerto_nodo1 = 9090  # Puerto del Nodo 1

socket_nodo2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_nodo2.connect((direccion_nodo1, puerto_nodo1))

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
        print("Nodo 1: " + mensaje)
        if mensaje.lower() == "adios":
            break

# Iniciar hilos para enviar y recibir mensajes
thread_enviar = threading.Thread(target=enviar_mensaje)
thread_recibir = threading.Thread(target=recibir_mensaje)

thread_enviar.start()
thread_recibir.start()









