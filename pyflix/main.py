import os
import time
import tracemalloc

from pyflix.archivio import SessioneUtente, salva_sessione_binaria
from pyflix.profili import Profilo, aggiungi_a_watchlist, clona_configurazione
from pyflix.streaming import analizza_eventi_lento


def demo_bug_profili():
    print("\n--- 1. DEMO BUG PROFILI ---")
    p1 = Profilo("Marco")
    p2 = Profilo("Giulia")
    p1.preferenze.append("Horror")
    print(f"Preferenze Giulia (attese ['Sci-Fi']): {p2.preferenze}")

    aggiungi_a_watchlist("Dark Stack")
    w2 = aggiungi_a_watchlist("Mr. Segfault")
    print(f"Watchlist utente 2 (attesa solo ['Mr. Segfault']): {w2}")

    base = {"piano": "4K", "dispositivi": ["TV", "Mobile"]}
    copia = clona_configurazione(base)
    copia["dispositivi"].append("Tablet")
    print(f"Dispositivi base (attesi 2): {base['dispositivi']}")


def demo_bug_streaming():
    print("\n--- 2. DEMO PERFORMANCE & MEMORIA STREAMING ---")
    percorso = "dati/eventi_small.jsonl"
    if not os.path.exists(percorso):
        print("Esegui prima: python genera_dati.py")
        return

    tracemalloc.start()
    t0 = time.perf_counter()
    titoli, _ = analizza_eventi_lento(percorso)
    dt = time.perf_counter() - t0
    _, picco = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Titoli unici: {len(titoli)} | Tempo: {dt:.4f}s | Picco RAM: {picco / 1024:.1f} KB")


def demo_bug_archivio():
    print("\n--- 3. DEMO BUG SERIALIZZAZIONE SESSIONE ---")
    os.makedirs("dati", exist_ok=True)
    sess = SessioneUtente("user_001", "dati/audit_demo.log")
    sess.traccia("PLAY Stranger Bits")
    try:
        salva_sessione_binaria(sess, "dati/sessione.pkl")
        print("Sessione salvata correttamente!")
    except Exception as e:
        print(f"CRASH durante pickle.dump: {type(e).__name__} -> {e}")
    finally:
        sess.chiudi()


if __name__ == "__main__":
    demo_bug_profili()
    demo_bug_streaming()
    demo_bug_archivio()