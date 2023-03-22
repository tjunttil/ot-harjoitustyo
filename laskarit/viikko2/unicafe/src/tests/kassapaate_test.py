import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_luotu_kassapaate_sisaltaa_oikean_rahamaaran(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luodun_kassapaatteen_myytyjen_lounaiden_maara_oikea(self):
        self.assertEqual((self.kassapaate.edulliset, self.kassapaate.maukkaat), (0,0))

    def test_edullinen_kateisosto_kasvattaa_kassaa_kun_raha_riittaa(self): 
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullinen_kateisosto_palauttaa_oikean_summan_kun_raha_riittaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

    def test_edullinen_kateisosto_kasvattaa_myytyjen_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_kateisosto_kasvattaa_kassaa_kun_raha_riittaa(self): 
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukkaasti_kateisosto_palauttaa_oikean_summan_kun_raha_riittaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_maukas_kateisosto_kasvattaa_myytyjen_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kassa_ei_muutu_kun_raha_ei_riita_edulliseen(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myydyt_ei_muutu_kun_raha_ei_riita_edulliseen(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kaikki_rahat_palautetaan_kun_raha_ei_riita(self):
        edullinen = self.kassapaate.syo_edullisesti_kateisella(200)
        maukas = self.kassapaate.syo_maukkaasti_kateisella(350)

        self.assertEqual((edullinen,maukas), (200,350))

    def test_kassa_ei_muutu_kun_raha_ei_riita_maukkaaseen(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myydyt_ei_muutu_kun_raha_ei_riita_maukkaaseen(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_edullinen_korttiosto_onnistuu_kun_saldo_riittava(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual((self.maksukortti.saldo, tulos), (760, True))

    def test_edullinen_korttiosto_kasvattaa_myytyja(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_korttiosto_onnistuu_kun_saldo_riittava(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual((self.maksukortti.saldo, tulos), (600, True))

    def test_maukas_korttiosto_kasvattaa_myytyja(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_mikaan_ei_muutu_ja_palautetaan_false_kun_saldo_ei_riita_edulliseen(self):
        maksukortti = Maksukortti(200)
        tulos = self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual((maksukortti.saldo, self.kassapaate.edulliset, tulos), (200, 0, False))

    def test_mikaan_ei_muutu_ja_palautetaan_false_kun_saldo_ei_riita_maukkaaseen(self):
        maksukortti = Maksukortti(300)
        tulos = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual((maksukortti.saldo, self.kassapaate.maukkaat, tulos), (300, 0, False))
    
    def test_kassa_ei_muutu_korttiostoissa(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        kassa1 = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        kassa2 = self.kassapaate.kassassa_rahaa
        self.k



   
