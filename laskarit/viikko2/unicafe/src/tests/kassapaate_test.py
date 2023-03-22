import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_luotu_kassapaate_sisaltaa_oikean_rahamaaran(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luodun_kassapaatteen_myytyjen_lounaiden_maara_oikea(self):
        self.assertEqual((self.kassapaate.edulliset, self.kassapaate.maukkaat), (0,0))

    def test_edullinen_kateisosto_kasvattaa_kassaa_kun_raha_riittaa(self):
        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100250)

    def test_edullinen_kateisosto_antaa_oikean_
