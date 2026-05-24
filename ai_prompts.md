# AI Kullanım Raporu - Sobretvaliane

## Claude (claude.ai) - 24 Mayıs 2026

### Proje Planlaması
**Prompt:** Programlama dili tasarımı için fikir ürettim, müzik/ritim üretici dil yapısı tasarladım.
**Kullanım:** Dilin genel yapısı, komut seti ve proje planlaması için yardım aldım.

### Lexer Geliştirme
**Prompt:** Sobretvaliane dili için lexer (sözcüksel analizci) yazılmasında yardım aldım.
**Kullanım:** Token tiplerinin belirlenmesi ve regex tabanlı tokenizer kodunun yazılması.

### Parser Geliştirme
**Prompt:** Token listesini AST'ye çeviren recursive descent parser geliştirilmesinde yardım aldım.
**Kullanım:** Parser sınıfının ve komut parse fonksiyonlarının yazılması.

### Evaluator Geliştirme
**Prompt:** AST'yi çalıştıran, pygame ile ses üreten evaluator geliştirilmesinde yardım aldım.
**Kullanım:** Ses üretme fonksiyonu, nota frekansları ve komut çalıştırma mantığının yazılması.

### Hata Giderme
**Prompt:** Pygame stereo ses hatası, Python 3.14 uyumsuzluğu gibi hataların çözümünde yardım aldım.
**Kullanım:** Hata mesajlarını analiz edip çözüm ürettim.

### Nota Ekleme
**Prompt:** Tüm oktavlar için diyez ve bemol notaların frekanslarının eklenmesi.
**Kullanım:** NOTALAR sözlüğüne 4 oktav boyunca tüm notaların eklenmesi.