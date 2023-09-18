# Zbiór kamer
class Kamera:
    def __init__(self, nazwa, wym_matr1, wym_matr2, wym_pix, ogniskowa, cykl, waga):
        self.nazwa = nazwa
        self.wym_matr1 = wym_matr1
        self.wym_matr2 = wym_matr2
        self.wym_pix = wym_pix
        self.ogniskowa = ogniskowa
        self.cykl = cykl
        self.waga = waga


# Zbiór samoltów
class Samolot:
    def __init__(self, nazwa, predkosc_min, predkosc_max, pulap, czas_lotu):
        self.nazwa = nazwa
        self.predkosc_min = predkosc_min
        self.predkosc_max = predkosc_max
        self.pulap = pulap
        self.czas_lotu = czas_lotu


kam1 = Kamera("Z/I DMC II 250", 16768, 14016, 5.6, 112, 2.3, 66)
kam2 = Kamera("Leica DMC III", 25728, 14592, 3.9, 92, 1.9, 63)
kam3 = Kamera("UltraCam Falcon M2 70",17310, 11310, 6, 70, 1.35, 61)
kam4 = Kamera("UltraCam Eagle M3", 26460, 17004, 4, 80, 1.5, 61)
kam5 = Kamera("DMC IIe 230", 15552, 14144, 5.6, 92, 1.7, 66)

sam1 = Samolot("Cessna 402", 132, 428, 8200, 5)
sam2 = Samolot("Cessna T206H NAV III", 100, 280, 4785, 5)
sam3 = Samolot("Vulcan Air P68 Obeserver 2", 135, 275, 6100, 6)
sam4 = Samolot("Tencam MMA", 120, 267, 4572, 6)

kamery = [kam1, kam2, kam3, kam4,kam5]
samoloty = [sam1, sam2, sam3, sam4]