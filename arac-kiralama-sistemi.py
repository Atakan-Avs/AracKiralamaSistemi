class Arac:
    def __init__(self, marka, model, yakit_turu, kiralama_ucreti):
        self.marka = marka
        self.model = model
        self.yakit_turu = yakit_turu
        self.kiralama_ucreti = kiralama_ucreti

    def kiralama_bilgisi(self):
        print(f"Marka: {self.marka} | Model: {self.model} | Yakıt türü: {self.yakit_turu} | Kiralama ücreti: {self.kiralama_ucreti} TL")

class Araba(Arac):
    def __init__(self, marka, model, yakit_turu, kiralama_ucreti, kapi_sayisi):
        super().__init__(marka, model, yakit_turu, kiralama_ucreti)
        self.kapi_sayisi = kapi_sayisi

    def kiralama_bilgisi(self):
        super().kiralama_bilgisi()
        print(f"Kapı sayısı: {self.kapi_sayisi}")

class Motosiklet(Arac):
    def __init__(self, marka, model, yakit_turu, kiralama_ucreti, kask_zorunlulugu):
        super().__init__(marka, model, yakit_turu, kiralama_ucreti)
        self.kask_zorunlulugu = kask_zorunlulugu

    def kiralama_bilgisi(self):
        super().kiralama_bilgisi()
        print(f"Kask zorunluluğu: {self.kask_zorunlulugu}")

class Kamyonet(Arac):
    def __init__(self, marka, model, yakit_turu, kiralama_ucreti, yuk_kapasitesi):
        super().__init__(marka, model, yakit_turu, kiralama_ucreti)
        self.yuk_kapasitesi = yuk_kapasitesi

    def kiralama_bilgisi(self):
        super().kiralama_bilgisi()
        print(f"Yük kapasitesi: {self.yuk_kapasitesi}")


def kiralama_hesapla(arac_turu, gun_sayisi):
    if arac_turu == "araba":
        arac = Araba("Audi", "A5", "Benzin", 1900, 4)
    elif arac_turu == "motosiklet":
        arac = Motosiklet("Yamaha", "R6", "Benzin", 980, "Evet")
    elif arac_turu == "kamyonet":
        arac = Kamyonet("Ford", "ABC", "LPG", 1450, "2000 kg")
    else:
        print("Geçersiz araç seçimi yaptınız")
        

    arac.kiralama_bilgisi()


    toplam_ucret = arac.kiralama_ucreti * gun_sayisi
    print(f"Toplam kiralama ücreti ({gun_sayisi} gün): {toplam_ucret} TL")


arac_turu = input("Hangi aracı kiralamak istersiniz? (araba, motosiklet, kamyonet): ").lower()
gun_sayisi = int(input("Kaç gün kiralamak istersiniz? "))

kiralama_hesapla(arac_turu, gun_sayisi)
