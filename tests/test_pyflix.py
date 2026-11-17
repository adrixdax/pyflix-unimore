# tests/test_pyflix.py
import tempfile
import unittest

from pyflix.profili import Profilo


class TestPyFlix(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

    def test_smoke_profilo_base(self):
        p = Profilo("Ada", piano="4K")
        self.assertEqual(p.nome, "Ada")

    # TODO FASE 4 & FASE 5: Aggiungi qui i test richiesti dalla traccia.


if __name__ == "__main__":
    unittest.main()