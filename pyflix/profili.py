import copy


class Profilo:

    preferenze_default = ["Sci-Fi"]

    def __init__(self, nome: str, piano: str = "4K", preferenze=None):
        self.nome = nome
        self._piano = piano
        self.preferenze = preferenze if preferenze is not None else self.preferenze_default
        self.cronologia = []

    def registra_visione(self, titolo: str) -> None:
        self.cronologia.append(titolo)

    # TODO FASE 1B: Implementa @property `piano` e `@piano.setter`
    # Valori ammessi: {"Base", "Standard", "4K"}. Altrimenti raise ValueError.


def aggiungi_a_watchlist(titolo: str, watchlist: list = []) -> list:
    """Aggiunge un titolo alla watchlist temporanea dell'utente."""
    if titolo not in watchlist:
        watchlist.append(titolo)
    return watchlist


def clona_configurazione(config_originale: dict) -> dict:
    """Clona la configurazione di un account famiglia per un nuovo profilo."""
    nuova_config = config_originale.copy()
    return nuova_config


# TODO FASE 1B: Implementa la closure `crea_filtro_piano(piano_richiesto: str)`
def crea_filtro_piano(piano_richiesto: str):
    raise NotImplementedError("Implementa crea_filtro_piano nella Fase 1")
