# IW02: Creating a Python Script to Interact with an API

> Realizat de studentul: Badia Victor \
> Grupa: I2301
> \
> Verificat de Mihail Croitor

## 1. Instalarea Dependențelor
Scriptul Python se bazează pe biblioteca requests pentru a efectua apeluri HTTP.

A. Sincronizarea Cheii API
Înainte de a rula, verificam că valoarea cheii API este identică în cele două fișiere:

Fișierul .env (pentru Docker): Am setat cheia API_KEY=lab02cheie.
Fișierul lab02/currency_exchange_rate.py (pentru Python): Variabila API_KEY trebuie să aibă aceeași valoare API_KEY = "lab02cheie").

B. Instalarea Bibliotecii requests
Am rulat următoarea comandă în terminal (din directorul rădăcină). Utilizarea py -m pip rezolvă majoritatea problemelor legate de PATH.

```bash
py -m pip install requests
```

C. Pornirea Serviciului Local (Docker)
Controlam că serviciul de schimb valutar rulează pe portul 8080 înainte de orice rulare a scriptului.

```bash
docker-compose up --build -d
```

## 2. Cum se Rulează Scriptul
Scriptul se execută din directorul rădăcină al proiectului și necesită trei argumente obligatorii: <MONEDA_DE_BAZĂ>, <MONEDA_ȚINTĂ> și <DATA>.
Intervalul de date valid pentru serviciu este 2025-01-01 până la 2025-09-15.

Sintaxa Comenzii
Utilizam py la începutul comenzii (sau calea completă la python.exe, dacă py nu funcționează):

```bash
py lab02/currency_exchange_rate.py <MONEDA_DE_BAZĂ> <MONEDA_ȚINTĂ> <YYYY-MM-DD>
```

## 3. Structura și Logica Scriptului
Scriptul lab02/currency_exchange_rate.py este modularizat în funcții pentru a separa responsabilitățile:
1. main(): Punct de Intrare: Configurează argparse pentru a citi cele 3 argumente de intrare din linia de comandă și validează formatul datei.
2. get_exchange_rate(): Interacțiune API: Construiește cererea HTTP către http://localhost:8080. Trimite cheia API prin metoda POST și monedele/data prin parametri GET.
3. Gestionarea Erorilor: Utilizează blocuri try...except pentru a prinde erorile de rețea (ConnectionError, Timeout) și erorile returnate de API (câmpul "error" din JSON). Orice eroare este pasată către funcția de logare.
4. log_error(): Logare și Ieșire: Înregistrează detaliile complete ale erorii (inclusiv excepțiile Python) în fișierul error.log și oprește execuția programului (sys.exit(1)).
5. save_data(): Salvarea Datelor: După un răspuns de succes, creează directorul data (dacă nu există) și scrie răspunsul JSON primit de la API într-un fișier numit în funcție de monede și dată.
