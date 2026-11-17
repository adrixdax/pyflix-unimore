import json
import pickle
import time
from abc import ABC, abstractmethod
from functools import wraps


# TODO FASE 3: Decoratore `@misura_tempo` con `@wraps(func)` e `wrapper.ultimo_tempo`
def misura_tempo(func):
    raise NotImplementedError("Implementa misura_tempo nella Fase 3")


# TODO FASE 3: Context Manager `RegistroAudit` (__enter__, scrivi, __exit__)
class RegistroAudit:
    def __init__(self, percorso: str):
        self.percorso = percorso
        self.file = None


# BUG 4: Pickle fallisce perché `self.log_file` è un handle aperto
class SessioneUtente:
    """Rappresenta una sessione attiva con un file di traccia aperto."""

    def __init__(self, utente: str, percorso_log: str):
        self.utente = utente
        self.percorso_log = percorso_log
        self.log_file = open(percorso_log, "a", encoding="utf-8")
        self.eventi_registrati = 0

    def traccia(self, evento: str) -> None:
        self.log_file.write(f"[{self.utente}] {evento}\n")
        self.eventi_registrati += 1

    def chiudi(self) -> None:
        if self.log_file and not self.log_file.closed:
            self.log_file.close()

    # TODO FASE 3: Implementa `__getstate__` e `__setstate__` per rendere serializzabile la sessione


def salva_sessione_binaria(sessione: SessioneUtente, percorso_pkl: str) -> None:
    with open(percorso_pkl, "wb") as f:
        pickle.dump(sessione, f)


# TODO FASE 5 (Sfida Extra): Definisci `Esportatore(ABC)` con `@abstractmethod esporta(self, dati: dict, percorso: str)`
# e le due sottoclassi concrete `EsportatoreJSON` ed `EsportatorePickle`.