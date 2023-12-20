from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_yksinkertainen import TekoalyYksinkertainen
from tekoaly_parannettu import TekoalyParannettu

class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()

        while True:
            ekan_siirto = self._ensimmaisen_siirto()

            if not self._onko_ok_siirto(ekan_siirto):
                break

            tokan_siirto = self._toisen_siirto(ekan_siirto)
            
            if not self._onko_ok_siirto(tokan_siirto):
                break
            
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)
        
        print("Kiitos")
        print(tuomari)
    
    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")
    
    def _toisen_siirto(self, ensimmaisen_siirto):
        return "k"
    
    def _onko_ok_siirto(self, siirto):
        return siirto in ["k", "p", "s"]

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto):
        return input("Toisen pelaajan siirto: ")

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self, tekoaly: Tekoaly):
        self._tekoaly = tekoaly
    
    def _toisen_siirto(self, ensimmaisen_siirto):
        valinta = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {valinta}")
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)
        return valinta

def luo_peli(tyyppi):
    if tyyppi == "a":
        return KPSPelaajaVsPelaaja()
    if tyyppi == "b":
        return KPSTekoaly(TekoalyYksinkertainen())
    if tyyppi == "c":
        return KPSTekoaly(TekoalyParannettu(10))
