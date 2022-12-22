#Most Similar Examples

from gensim.models import KeyedVectors
import string

print("Model Yükleniyor...")
kelimeVektoru = KeyedVectors.load_word2vec_format('trModel100', binary=True)
print(kelimeVektoru)

anahtarKelimeler = input("Kelimeleri giriniz: ")

temizlenenKelimeler = ""
for i in anahtarKelimeler:
    if i not in string.punctuation:
        temizlenenKelimeler += i

print(temizlenenKelimeler)

listeKelimeler = temizlenenKelimeler.split()

print(listeKelimeler)

for kelime in listeKelimeler:
    oneriler = (kelimeVektoru.most_similar(positive=kelime))
    print(oneriler)