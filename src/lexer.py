import re

# Token tipleri
TOKEN_TIPLER = [
    ('SAYI',     r'\d+(\.\d+)?'),
    ('METIN',    r'"[^"]*"'),
    ('NOTA',     r'(DO|RE|MI|FA|SOL|LA|SI)(diyez|bemol)?[1-7]?'),
    ('ANAHTAR',  r'TEMPO|NOTA|BEKLE|TEKRAR|CALAR|DURDUR|YAZAR|TANIMLA|EGER|ISE|DEGILSE|BITIR'),
    ('ISIM',     r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('ESIT',     r'='),
    ('ARTI',     r'\+'),
    ('EKSI',     r'-'),
    ('ÇARP',     r'\*'),
    ('BOL',      r'/'),
    ('BÜYÜK',    r'>'),
    ('KÜÇÜK',    r'<'),
    ('AÇPARANTEZ', r'\('),
    ('KAPPARANTEZ', r'\)'),
    ('AÇSÜSLÜ',  r'\{'),
    ('KAPSÜSLÜ', r'\}'),
    ('ATLA',     r'[ \t\n]+'),
    ('BILINMIYOR', r'.'),
]

def tokenize(kod):
    tokens = []
    pos = 0
    satir = 1

    while pos < len(kod):
        eslesti = False
        for tip, pattern in TOKEN_TIPLER:
            regex = re.compile(pattern)
            m = regex.match(kod, pos)
            if m:
                deger = m.group(0)
                if tip == 'ATLA':
                    satir += deger.count('\n')
                elif tip != 'BILINMIYOR':
                    tokens.append((tip, deger, satir))
                elif tip == 'BILINMIYOR':
                    raise SyntaxError(f"Satir {satir}: Bilinmeyen karakter '{deger}'")
                pos = m.end()
                eslesti = True
                break
        if not eslesti:
            raise SyntaxError(f"Satir {satir}: Okunamayan karakter")

    tokens.append(('BITIS', '', satir))
    return tokens