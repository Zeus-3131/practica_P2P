# practica_P2P
# Práctica de Comunicación P2P (Peer-to-Peer)

En esta práctica, implementamos una comunicación P2P básica entre dos nodos que se ejecutan en la misma máquina. Cada nodo actúa tanto como servidor como cliente, lo que permite una comunicación bidireccional entre ellos. 

## Nodo 1 (Cliente P2P - Parte 1)

### Configuración del Socket del Nodo 1

El primer fragmento de código representa el Nodo 1, que actúa como servidor en el puerto 9090 y espera una conexión del Nodo 2.

- `direccion_nodo2`: La dirección IP del Nodo 2 se establece en "127.0.0.1", que se refiere a la máquina local.
- `puerto_nodo2`: Se utiliza un puerto diferente al puerto del Nodo 2, en este caso, 9091.

### Creación y Configuración del Socket

```python
socket_nodo1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_nodo1.bind(("0.0.0.0", 9090))
socket_nodo1.listen()
