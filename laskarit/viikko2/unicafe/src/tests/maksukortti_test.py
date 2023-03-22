import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")

    def test_saldo_vahenee_kun_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.00 euroa")

    def test_saldo_ei_muutu_jos_raha_ei_riita(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_ota_rahaa_palauttaa_true_kun_raha_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1000), True)

    def test_ota_rahaa_palauttaa_false_kun_raha_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)
