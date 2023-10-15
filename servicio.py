import psutil, time, threading, webbrowser

url = 'https://www.youtube.com/' # Definimos URL
ruta_chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
bandera = False

def timer(): # REALIZA LA ACCION DE RESPALDO CADA 30 SEGUNDOS #
        global bandera
        while True: # Accion a repetir
            for proc in psutil.process_iter():
                if proc.name() == 'chrome.exe':
                    bandera = True

            if bandera == False: # El proceso NO está en ejecución
                 webbrowser.get(ruta_chrome).open(url) # Ejecutamos el proceso
                 bandera = True
            else:
                    print("En ejecución.")
            time.sleep(1) # Repetimos procedimiento cada 30 segundos

# Creamos el hilo
t = threading.Thread(target = timer)
t.start()