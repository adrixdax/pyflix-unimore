import json
import os
import random


def genera_jsonl(percorso: str, num_righe: int) -> None:
    """Genera un dataset JSONL simulato per i test di streaming e memoria."""
    os.makedirs(os.path.dirname(percorso), exist_ok=True)
    utenti = [f"user_{i:03d}" for i in range(1, 201)]
    titoli = [
        "Stranger Bits",
        "The Witcher of RAM",
        "Breaking Bytes",
        "Black Mirroring",
        "Dark Stack",
        "House of Threads",
        "Cyberpunk: Edgerunners",
        "Mr. Segfault",
    ]
    generi = ["Sci-Fi", "Drama", "Thriller", "Cyberpunk", "Action"]

    with open(percorso, "w", encoding="utf-8") as f:
        for i in range(num_righe):
            record = {
                "id_evento": i,
                "utente": random.choice(utenti),
                "titolo": random.choice(titoli),
                "genere": random.choice(generi),
                "minuto": random.randint(1, 120),
                "bytes": random.randint(50_000, 2_000_000),
            }
            f.write(json.dumps(record) + "\n")


if __name__ == "__main__":
    print("Generazione dataset PyFlix in corso...")
    genera_jsonl("dati/eventi_small.jsonl", 5_000)
    genera_jsonl("dati/eventi_massivi.jsonl", 300_000)
    print("Fatto! Creati dati/eventi_small.jsonl e dati/eventi_massivi.jsonl.")