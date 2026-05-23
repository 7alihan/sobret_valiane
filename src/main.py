import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from lexer import tokenize
from parser import Parser
from evaluator import Evaluator

def dosya_calistir(dosya_yolu):
    with open(dosya_yolu, 'r', encoding='utf-8') as f:
        kod = f.read()
    
    print("=" * 40)
    print("  Sobretvaliane Yorumlayici")
    print("=" * 40)
    print(f"Dosya: {dosya_yolu}")
    print("=" * 40)
    
    tokens = tokenize(kod)
    parser = Parser(tokens)
    ast = parser.parse()
    evaluator = Evaluator()
    evaluator.calistir(ast)
    
    print("=" * 40)
    print("Tamamlandi!")
    print("=" * 40)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanim: python main.py <dosya.sbt>")
    else:
        dosya_calistir(sys.argv[1])