import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)


    def test_luotu_rahamaara_oikea(self):
        if self.kassapaate.kassassa_rahaa == 100000 and self.kassapaate.edulliset == 0 and self.kassapaate.maukkaat == 0:
            return True
        else:
            return False
        
    def test_kateisosto_toimii(self):
        self.kassapaate.syo_edullisesti_kateisella(400)
        self.kassapaate.syo_maukkaasti_kateisella(240)
        self.kassapaate.syo_edullisesti_kateisella(1)
        self.kassapaate.syo_maukkaasti_kateisella(1)
        if self.kassapaate.edulliset == 1 and self.kassapaate.maukkaat == 1 and self.kassapaate.kassassa_rahaa == self.kassapaate.kassassa_rahaa == 100640:
            return True
        else:
            return False
    
    def test_korttiosto_toimii(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        if self.kassapaate.edulliset == 1 and self.kassapaate.maukkaat == 1 and str(self.maksukortti) == "Kortilla on rahaa 4.50 euroa":
            return True
    
    def test_lataus_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,100)
        if str(self.maksukortti) == "Kortilla on rahaa 11.00 euroa" and self.kassapaate.kassassa_rahaa == 100100:
            return True
        else:
            return False