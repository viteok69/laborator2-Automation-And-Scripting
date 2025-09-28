# IW02: Creating a Python Script to Interact with an API

> Realizat de studentul: Badia Victor \
> Grupa: I2301
> \
> Verificat de Mihail Croitor

## 1. Instalarea Dependențelor
Scriptul Python se bazează pe biblioteca requests pentru a efectua apeluri HTTP.

A. Sincronizarea Cheii API
Înainte de a rula, asigurați-vă că valoarea cheii API este identică în cele două fișiere:

Fișierul .env (pentru Docker): Setați cheia (de exemplu, API_KEY=lab02cheie).
Fișierul lab02/currency_exchange_rate.py (pentru Python): Variabila API_KEY trebuie să aibă aceeași valoare (de exemplu, API_KEY = "lab02cheie").

B. Instalarea Bibliotecii requests
Rulați următoarea comandă în terminal (din directorul rădăcină). Utilizarea py -m pip rezolvă majoritatea problemelor legate de PATH.

```bash
py -m pip install requests
```

C. Pornirea Serviciului Local (Docker)
Asigurați-vă că serviciul de schimb valutar rulează pe portul 8080 înainte de orice rulare a scriptului.

```bash
docker-compose up --build -d
```

## 2. Cum se Rulează Scriptul
Scriptul se execută din directorul rădăcină al proiectului și necesită trei argumente obligatorii: <MONEDA_DE_BAZĂ>, <MONEDA_ȚINTĂ> și <DATA>.
Intervalul de date valid pentru serviciu este 2025-01-01 până la 2025-09-15.

Sintaxa Comenzii
Utilizați py la începutul comenzii (sau calea completă la python.exe, dacă py nu funcționează):

```bash
py lab02/currency_exchange_rate.py <MONEDA_DE_BAZĂ> <MONEDA_ȚINTĂ> <YYYY-MM-DD>
```

##3. Structura și Logica Scriptului
Scriptul lab02/currency_exchange_rate.py este modularizat în funcții pentru a separa responsabilitățile:
1. main(): Punct de Intrare: Configurează argparse pentru a citi cele 3 argumente de intrare din linia de comandă și validează formatul datei.
