import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):

    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        kortti = Maksukortti(1000)
        vastaus = str(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")

    def test_rahan_ottaminen_toimii(self):
        self.maksukortti = Maksukortti(1000)
        self.maksukortti.ota_rahaa(650)
        self.maksukortti.ota_rahaa(650)
        if str(self.maksukortti) == "Kortilla on rahaa 4.50 euroa":
            return True
        else:
            return False