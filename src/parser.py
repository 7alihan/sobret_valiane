class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def siradaki(self):
        return self.tokens[self.pos]

    def tuket(self, beklenen_tip=None):
        token = self.tokens[self.pos]
        if beklenen_tip and token[0] != beklenen_tip:
            raise SyntaxError(f"Satir {token[2]}: '{beklenen_tip}' beklendi ama '{token[0]}' bulundu")
        self.pos += 1
        return token

    def parse(self):
        program = []
        while self.siradaki()[0] != 'BITIS':
            komut = self.komut_parse()
            if komut:
                program.append(komut)
        return program

    def komut_parse(self):
        token = self.siradaki()

        if token[0] == 'ANAHTAR':
            if token[1] == 'NOTA':
                return self.nota_parse()
            elif token[1] == 'TEMPO':
                return self.tempo_parse()
            elif token[1] == 'BEKLE':
                return self.bekle_parse()
            elif token[1] == 'TEKRAR':
                return self.tekrar_parse()
            elif token[1] == 'CALAR':
                self.tuket()
                return ('CALAR',)
            elif token[1] == 'DURDUR':
                self.tuket()
                return ('DURDUR',)
            elif token[1] == 'YAZAR':
                return self.yazar_parse()
            elif token[1] == 'TANIMLA':
                return self.tanimla_parse()
            elif token[1] == 'EGER':
                return self.eger_parse()
        elif token[0] == 'ISIM':
            return self.atama_parse()
        else:
            raise SyntaxError(f"Satir {token[2]}: Beklenmeyen token '{token[1]}'")

    def nota_parse(self):
        self.tuket('ANAHTAR')
        nota = self.tuket('NOTA')
        sure = self.tuket('SAYI')
        return ('NOTA', nota[1], float(sure[1]))

    def tempo_parse(self):
        self.tuket('ANAHTAR')
        deger = self.tuket('SAYI')
        return ('TEMPO', int(deger[1]))

    def bekle_parse(self):
        self.tuket('ANAHTAR')
        sure = self.tuket('SAYI')
        return ('BEKLE', float(sure[1]))

    def tekrar_parse(self):
        self.tuket('ANAHTAR')
        sayi = self.tuket('SAYI')
        self.tuket('AÇSÜSLÜ')
        govde = []
        while self.siradaki()[0] != 'KAPSÜSLÜ':
            govde.append(self.komut_parse())
        self.tuket('KAPSÜSLÜ')
        return ('TEKRAR', int(sayi[1]), govde)

    def yazar_parse(self):
        self.tuket('ANAHTAR')
        metin = self.tuket('METIN')
        return ('YAZAR', metin[1][1:-1])

    def tanimla_parse(self):
        self.tuket('ANAHTAR')
        isim = self.tuket('ISIM')
        self.tuket('ESIT')
        deger = self.tuket('SAYI')
        return ('TANIMLA', isim[1], float(deger[1]))

    def atama_parse(self):
        isim = self.tuket('ISIM')
        self.tuket('ESIT')
        deger = self.tuket('SAYI')
        return ('TANIMLA', isim[1], float(deger[1]))

    def eger_parse(self):
        self.tuket('ANAHTAR')
        sol = self.tuket('ISIM')
        op_token = self.siradaki()
        if op_token[0] in ('BÜYÜK', 'KÜÇÜK', 'ESIT'):
            op = self.tuket()[1]
        else:
            raise SyntaxError(f"Satir {op_token[2]}: Karşılaştırma operatörü beklendi")
        sag = self.tuket('SAYI')
        self.tuket('ANAHTAR')
        self.tuket('AÇSÜSLÜ')
        govde = []
        while self.siradaki()[0] != 'KAPSÜSLÜ':
            govde.append(self.komut_parse())
        self.tuket('KAPSÜSLÜ')
        return ('EGER', sol[1], op, float(sag[1]), govde)