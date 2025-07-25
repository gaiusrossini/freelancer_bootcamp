# collector.py
import json
import os

DATA_FILE = 'data/airdrops.json'


def load_existing_airdrops():
    """Load the airdrops in a list."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_airdrops(airdrops):
    """Save the updated airdrop list."""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(airdrops, f, indent=2, ensure_ascii=False)


def is_new_airdrop(airdrop, existing_airdrops):
    """Verify if the airdrop is new."""
    return not any(existing['link'] == airdrop['link'] for existing in existing_airdrops)


def collect_and_store(new_airdrops):

    """Get a list of dictionaries and add only new ones in an archive."""

    existing = load_existing_airdrops()
    added = []

    for airdrop in new_airdrops:
        if is_new_airdrop(airdrop, existing):
            existing.append(airdrop)
            added.append(airdrop)

    if added:
        save_airdrops(existing)

    return added  # Returns the ones that have been added


# Exemple of direct use:
if __name__ == "__main__":
    exemplo = [
        {"title": "New Gem", "link": "https://airdrops.live/airdrop/nova-gema/", "source": "airdrops.live"}
    ]
    new = collect_and_store(exemplo)
    print(f"{len(new)} new airdrops added.")
