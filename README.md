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
