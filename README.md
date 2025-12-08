# Proiect_echipa_Alexandra_Elisei
```import psutil
import tkinter as tk
import time
import os

def converteste_bytes(bytes_val):
    """
    Funcție ajutătoare care transformă biții (care sunt numere uriașe)
    în format citibil: GB sau MB.
    """
    factor = 1024 * 1024 * 1024  # Împărțim la 1024^3 pentru a ajunge la GB
    valoare_gb = bytes_val / factor
    return f"{valoare_gb:.2f} GB"


def start_monitorizare():
    print("Pornește monitorizarea... (Apasă CTRL+C pentru a opri)")

    try:
        while True:
            # --- 1. Curățare Ecran ---
            # Această linie șterge textul vechi din consolă ca să pară o animație
            # 'cls' e pentru Windows, 'clear' e pentru Linux/Mac
            os.system('cls' if os.name == 'nt' else 'clear')

            print("=== MONITOR RESURSE (Backend Test) ===")
            print("--------------------------------------")

            # --- 2. CPU ---
            # interval=1 înseamnă că așteaptă 1 secundă să calculeze media
            # Tot aici se face și pauza de 1 secundă a buclei!
            cpu_usage = psutil.cpu_percent(interval=int_vsl)

            print(f"procesor (CPU): {cpu_usage}%")

            # --- 3. RAM ---
            memorie = psutil.virtual_memory()
            # memorie.total = cât ram ai fizic
            # memorie.used = cât e ocupat
            # memorie.percent = procentajul
            print(f"Memorie (RAM):  {memorie.percent}% "
                  f"({converteste_bytes(memorie.used)} / {converteste_bytes(memorie.total)})")

            # --- 4. Baterie ---
            baterie = psutil.sensors_battery()

            if baterie is not None:
                # Verificăm dacă există baterie (Desktop-urile nu au)
                status_incarcare = "La priză" if baterie.power_plugged else "Pe baterie"

                # convertim secundele rămase în ore:minute (dacă e disponibil)
                timp_ramas = "Indisponibil"
                if baterie.secsleft != psutil.POWER_TIME_UNLIMITED and baterie.secsleft != psutil.POWER_TIME_UNKNOWN:
                    ore = baterie.secsleft // 3600
                    minute = (baterie.secsleft % 3600) // 60
                    timp_ramas = f"{ore}h {minute}m"

                print(f"Baterie:        {baterie.percent}% ({status_incarcare})")
                print(f"Timp rămas:     {timp_ramas}")
            else:
                print("Baterie:        Nu a fost detectată (PC Desktop?)")

    except KeyboardInterrupt:
        print("\nMonitorizare oprită de utilizator.")


#Rulăm funcția
if __name__ == "__main__":
    int_vsl=float(input())
    start_monitorizare()
```
