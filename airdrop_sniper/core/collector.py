# collector.py
import json
import os

DATA_FILE = 'data/airdrops.json'


def load_existing_airdrops():
    """Carrega os airdrops salvos em disco."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_airdrops(airdrops):
    """Salva a lista atualizada de airdrops."""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(airdrops, f, indent=2, ensure_ascii=False)


def is_new_airdrop(airdrop, existing_airdrops):
    """Verifica se o airdrop já existe."""
    return not any(existing['link'] == airdrop['link'] for existing in existing_airdrops)


def collect_and_store(new_airdrops):
    """
    Recebe uma lista de dicionários com airdrops novos do scraper
    e adiciona apenas os que ainda não existem no arquivo.
    """
    existing = load_existing_airdrops()
    added = []

    for airdrop in new_airdrops:
        if is_new_airdrop(airdrop, existing):
            existing.append(airdrop)
            added.append(airdrop)

    if added:
        save_airdrops(existing)

    return added  # Retorna os que foram de fato adicionados


# Exemplo de uso direto:
if __name__ == "__main__":
    exemplo = [
        {"title": "Nova Gema", "link": "https://airdrops.live/airdrop/nova-gema/", "source": "airdrops.live"}
    ]
    novos = collect_and_store(exemplo)
    print(f"{len(novos)} airdrops novos adicionados.")
