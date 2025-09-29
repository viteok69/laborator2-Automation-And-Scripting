import argparse
import requests
import json
import os
import sys
import logging
from datetime import datetime

API_BASE_URL = "http://localhost:8080"
API_KEY = "lab02cheie" 
LOG_FILE = "error.log"
DATA_DIR = "data"

def log_error(message, error_details=None):
    """Înregistrează mesajul de eroare în fișierul error.log."""
    log_path = os.path.join(os.getcwd(), LOG_FILE)
    logging.basicConfig(
        filename=log_path,
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    full_message = f"{message}"
    if error_details:
        full_message += f" Detalii: {error_details}"
    logging.error(full_message)
    print(f"\n[EROARE] {message}")
    if error_details:
        print(f"[DETALII] Vă rugăm verificați {LOG_FILE} pentru detalii complete.")
    sys.exit(1)

def save_data(data, from_currency, to_currency, date_str):
    """Salvează datele primite în format JSON într-un fișier numit după monede și dată."""
    
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        
    filename = f"{from_currency}_to_{to_currency}_{date_str}.json"
    filepath = os.path.join(DATA_DIR, filename)
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"\n[SUCCES] Datele ratei de schimb au fost salvate în: {filepath}")
    except IOError as e:
        log_error(f"Eroare la salvarea fișierului JSON în {filepath}", e)

def get_exchange_rate(from_currency, to_currency, date_str):
    """Obține rata de schimb de la serviciul API."""
    
    url = f"{API_BASE_URL}/"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    params = {
        'from': from_currency,
        'to': to_currency,
        'date': date_str,
    }
    
    post_data = {'key': API_KEY}
    
    try:
        response = requests.post(url, data=post_data, params=params, headers=headers, timeout=10)
        
        response.raise_for_status()
        
        try:
            api_response = response.json()
        except requests.JSONDecodeError:
            log_error("Răspunsul API nu este un JSON valid.", response.text)
            
        if api_response.get('error'):
            error_msg = f"Eroare API pentru {from_currency}/{to_currency} la data {date_str}: {api_response['error']}"
            log_error(error_msg, api_response)

        if api_response.get('data') is not None:
            rate = api_response['data']
            print("--------------------------------------------------")
            print(f"RATA DE SCHIMB PENTRU DATA {date_str}:")
            print(f"1 {from_currency} = {rate:.4f} {to_currency}")
            print("--------------------------------------------------")
            
            save_data(api_response, from_currency, to_currency, date_str)
            
        else:
            log_error(f"Răspuns API valid, dar lipsește câmpul 'data'.", api_response)
            
    except requests.exceptions.HTTPError as err:
        log_error(f"Eroare HTTP la accesarea API-ului (Status: {response.status_code})", err)
    except requests.exceptions.ConnectionError as err:
        log_error("Eroare de conexiune: Asigurați-vă că serviciul Docker rulează la http://localhost:8080.", err)
    except requests.exceptions.Timeout as err:
        log_error("Timp de așteptare expirat (Timeout) la cererea API.", err)
    except requests.exceptions.RequestException as err:
        log_error("O eroare necunoscută a apărut în timpul cererii API.", err)

def main():
    """Funcția principală pentru a citi argumentele și a rula logica."""
    parser = argparse.ArgumentParser(description="Obține rata de schimb valutar pentru o anumită dată.")
    parser.add_argument("from_currency", help="Moneda de bază (ex: USD)")
    parser.add_argument("to_currency", help="Moneda țintă (ex: RON)")
    parser.add_argument("date", help="Data în format YYYY-MM-DD (ex: 2025-01-01)")
    
    args = parser.parse_args()
    
    try:
        datetime.strptime(args.date, '%Y-%m-%d')
    except ValueError:
        log_error(f"Format de dată invalid: '{args.date}'. Folosiți formatul YYYY-MM-DD.")
        
    get_exchange_rate(args.from_currency.upper(), args.to_currency.upper(), args.date)

if __name__ == "__main__":
    main()

