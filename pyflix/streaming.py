import json
import os
from collections import deque


# Versione lenta/eager da confrontare nei benchmark
def analizza_eventi_lento(percorso_file: str) -> tuple[list[str], dict[str, int]]:
    with open(percorso_file, "r", encoding="utf-8") as f:
        righe = f.readlines()

    titoli_unici = []
    byte_per_utente = {}

    for riga in righe:
        dato = json.loads(riga)
        titolo = dato["titolo"]
        utente = dato["utente"]
        byte_scaricati = dato["bytes"]

        if titolo not in titoli_unici:
            titoli_unici.append(titolo)

        if utente not in byte_per_utente:
            byte_per_utente[utente] = 0
        byte_per_utente[utente] += byte_scaricati

    return titoli_unici, byte_per_utente


# TODO FASE 2: Generatore lazy che legge riga per riga e produce tuple immutabili
# Formato tupla: (utente, titolo, genere, minuto, bytes)
def stream_eventi(percorso_file: str):
    raise NotImplementedError("Implementa stream_eventi nella Fase 2")


# TODO FASE 2: Aggregazione veloce con set, dict, deque(maxlen=5) e scrittura atomica (.tmp + os.replace)
# Ritorno atteso: {"titoli_unici": set, "byte_per_utente": dict, "ultimi_5": list}
def genera_report_veloce(percorso_input: str, percorso_output: str) -> dict:
    raise NotImplementedError("Implementa genera_report_veloce nella Fase 2")