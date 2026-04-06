import json
import os
from datetime import datetime

LOG_FILE = "/home/ubuntu/skills/instagram-prospector/prospect_log.json"

def log_interaction(username, action, niche):
    """
    Registra uma interação com um perfil do Instagram para evitar duplicidade.
    """
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Verifica se já existe interação recente (últimos 30 dias)
    for entry in data:
        if entry['username'] == username and entry['action'] == action:
            print(f"Aviso: Interação '{action}' já realizada com {username} em {entry['date']}.")
            return False

    new_entry = {
        "username": username,
        "action": action,
        "niche": niche,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data.append(new_entry)

    with open(LOG_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"Sucesso: Interação '{action}' com {username} registrada.")
    return True

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 3:
        log_interaction(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Uso: python3 log_prospect.py <username> <action> <niche>")
