from airdrop_sniper.core.collector import collect_and_store

airdrops_scraped = [
    {"title": "Kreamer", "link": "https://airdrops.live/airdrop/kreamer/", "source": "airdrops.live"},
    {"title": "Bitscrunch", "link": "https://airdrops.live/airdrop/bitscrunch/", "source": "airdrops.live"}
]

novos = collect_and_store(airdrops_scraped)

if novos:
    print(f"🎯 We've found {len(novos)} new airdrops!")
else:
    print("😴 There's NO new airdrops.")
