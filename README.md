```markdown
# Sobretvaliane

Sobretvaliane, müzik ve ritim üretmeye odaklanmış, özgün bir programlama dilidir. Kendi sözdizimi ile nota, tempo ve ritim komutları yazarak bilgisayardan gerçek sesler üretebilirsiniz. Dosya uzantısı `.sbt` dir.

## Özellikler
- `NOTA` komutu ile gerçek ses frekansları çalar (DO, RE, MI, FA, SOL, LA, SI ve tüm diyez/bemolleri)
- `TEMPO` ile BPM ayarlanır
- `TEKRAR` ile döngü oluşturulur
- `TANIMLA` ile değişken tanımlanır
- `EGER` ile koşullu ifade yazılır
- `BEKLE` ile bekleme süresi eklenir
- `YAZAR` ile ekrana mesaj yazdırılır

## Kurulum
```python
python -m pip install pygame numpy
```

## Kullanım
```python
python src/main.py examples/ornek1.sbt
```

## Örnek Kod
```
TEMPO 120
YAZAR "Merhaba, Sobretvaliane!"
NOTA LA 1
NOTA SOL 0.5
NOTA MI 0.5
TEKRAR 2 {
    NOTA DO 0.5
    NOTA RE 0.5
    NOTA MI 1
}
```

## Gramer (BNF)
```
<program>    ::= <komut>*
<komut>      ::= <nota> | <tempo> | <bekle> | <tekrar> | <yazar> | <tanimla> | <eger>
<nota>       ::= "NOTA" <nota_adi> <sayi>
<tempo>      ::= "TEMPO" <sayi>
<bekle>      ::= "BEKLE" <sayi>
<tekrar>     ::= "TEKRAR" <sayi> "{" <komut>* "}"
<yazar>      ::= "YAZAR" <metin>
<tanimla>    ::= "TANIMLA" <isim> "=" <sayi>
<eger>       ::= "EGER" <isim> <op> <sayi> "ISE" "{" <komut>* "}"
<nota_adi>   ::= "DO" | "RE" | "MI" | "FA" | "SOL" | "LA" | "SI" | diyez/bemol varyantları
<op>         ::= ">" | "<" | "="
```

## Proje Yapısı
```
sobretvaliane/
├── src/
│   ├── lexer.py       → Kaynak kodu tokenlara böler
│   ├── parser.py      → Tokenları AST ye çevirir
│   ├── evaluator.py   → AST yi çalıştırır, sesi üretir
│   └── main.py        → Ana giriş noktası
├── examples/
│   ├── ornek1.sbt     → Star Shopping - Lil Peep
│   ├── ornek2.sbt     → Sen Gülünce Güller Açar
│   └── ornek3.sbt     → Shape of My Heart - Sting
├── README.md
└── ai_prompts.md
```

## Geliştirici
7alihan — BIL206 Programlama Dillerinin Prensipleri Dönem Ödevi
```

