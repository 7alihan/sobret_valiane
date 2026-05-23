import time
import numpy as np
import pygame

pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)

NOTALAR = {
    # 1. Oktav
    'DO1': 130.81, 'DOdiyez1': 138.59, 'REbemol1': 138.59,
    'RE1': 146.83, 'REdiyez1': 155.56, 'MIbemol1': 155.56,
    'MI1': 164.81,
    'FA1': 174.61, 'FAdiyez1': 185.00, 'SOLbemol1': 185.00,
    'SOL1': 196.00, 'SOLdiyez1': 207.65, 'LAbemol1': 207.65,
    'LA1': 220.00, 'LAdiyez1': 233.08, 'SIbemol1': 233.08,
    'SI1': 246.94,

    # 2. Oktav (varsayılan)
    'DO': 261.63, 'DOdiyez': 277.18, 'REbemol': 277.18,
    'RE': 293.66, 'REdiyez': 311.13, 'MIbemol': 311.13,
    'MI': 329.63,
    'FA': 349.23, 'FAdiyez': 369.99, 'SOLbemol': 369.99,
    'SOL': 392.00, 'SOLdiyez': 415.30, 'LAbemol': 415.30,
    'LA': 440.00, 'LAdiyez': 466.16, 'SIbemol': 466.16,
    'SI': 493.88,

    # 3. Oktav
    'DO2': 523.25, 'DOdiyez2': 554.37, 'REbemol2': 554.37,
    'RE2': 587.33, 'REdiyez2': 622.25, 'MIbemol2': 622.25,
    'MI2': 659.25,
    'FA2': 698.46, 'FAdiyez2': 739.99, 'SOLbemol2': 739.99,
    'SOL2': 783.99, 'SOLdiyez2': 830.61, 'LAbemol2': 830.61,
    'LA2': 880.00, 'LAdiyez2': 932.33, 'SIbemol2': 932.33,
    'SI2': 987.77,

    # 4. Oktav
    'DO3': 1046.50, 'DOdiyez3': 1108.73, 'REbemol3': 1108.73,
    'RE3': 1174.66, 'REdiyez3': 1244.51, 'MIbemol3': 1244.51,
    'MI3': 1318.51,
    'FA3': 1396.91, 'FAdiyez3': 1479.98, 'SOLbemol3': 1479.98,
    'SOL3': 1567.98, 'SOLdiyez3': 1661.22, 'LAbemol3': 1661.22,
    'LA3': 1760.00, 'LAdiyez3': 1864.66, 'SIbemol3': 1864.66,
    'SI3': 1975.53,
}

def ses_uret(frekans, sure):
    ornekleme = 44100
    kareler = int(ornekleme * sure)
    t = np.linspace(0, sure, kareler, False)
    dalga = np.sin(frekans * t * 2 * np.pi) * 0.5
    fade = min(int(ornekleme * 0.01), kareler // 4)
    dalga[:fade] *= np.linspace(0, 1, fade)
    dalga[-fade:] *= np.linspace(1, 0, fade)
    ses = (dalga * 32767).astype(np.int16)
    stereo = np.column_stack([ses, ses])
    sound = pygame.sndarray.make_sound(stereo)
    sound.play()
    time.sleep(sure)

class Evaluator:
    def __init__(self):
        self.degiskenler = {}
        self.tempo = 120

    def calistir(self, program):
        for komut in program:
            self.komut_calistir(komut)

    def komut_calistir(self, komut):
        tip = komut[0]

        if tip == 'TEMPO':
            self.tempo = komut[1]
            print(f"🎵 Tempo: {self.tempo} BPM")

        elif tip == 'NOTA':
            nota_adi = komut[1]
            sure = komut[2]
            if nota_adi in NOTALAR:
                frekans = NOTALAR[nota_adi]
                gercek_sure = round((60 / self.tempo) * sure, 2)
                print(f"  ♪ {nota_adi} ({frekans}Hz) - {gercek_sure}s")
                ses_uret(frekans, gercek_sure)
            else:
                raise ValueError(f"Bilinmeyen nota: {nota_adi}")

        elif tip == 'BEKLE':
            sure = komut[1]
            gercek_sure = (60 / self.tempo) * sure
            print(f"  ⏸ Bekleniyor: {gercek_sure:.2f}s")
            time.sleep(gercek_sure)

        elif tip == 'TEKRAR':
            sayi = komut[1]
            govde = komut[2]
            print(f"🔁 {sayi} kez tekrar:")
            for i in range(sayi):
                for alt_komut in govde:
                    self.komut_calistir(alt_komut)

        elif tip == 'YAZAR':
            metin = komut[1]
            print(f"💬 {metin}")

        elif tip == 'TANIMLA':
            isim = komut[1]
            deger = komut[2]
            self.degiskenler[isim] = deger
            print(f"📌 {isim} = {deger}")

        elif tip == 'EGER':
            isim = komut[1]
            op = komut[2]
            deger = komut[3]
            govde = komut[4]
            if isim not in self.degiskenler:
                raise ValueError(f"Bilinmeyen degisken: {isim}")
            sol = self.degiskenler[isim]
            if op == '>' and sol > deger:
                for alt_komut in govde:
                    self.komut_calistir(alt_komut)
            elif op == '<' and sol < deger:
                for alt_komut in govde:
                    self.komut_calistir(alt_komut)
            elif op == '=' and sol == deger:
                for alt_komut in govde:
                    self.komut_calistir(alt_komut)

        elif tip == 'CALAR':
            print("▶ Çalınıyor...")

        elif tip == 'DURDUR':
            print("⏹ Durduruldu.")