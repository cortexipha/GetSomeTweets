class Isim:
    def __init__(self, kelime, type, index):
        self.isim = [kelime]
        self.type = type
        self.baslangicIndex = index
        self.puan = 1

    def isimeEkle(self, kelime):
        self.isim.append(kelime)
        self.puan += 1