#Doesnt Match Example

from gensim.models import KeyedVectors

print("Model Yükleniyor...")
kelimeVektoru = KeyedVectors.load_word2vec_format('trModel100', binary=True)
print(kelimeVektoru)

def farkliBul():

    anahtarKelimeler = input("Anahtar Kelimeler: ").lower().split()

    benzerlik = (kelimeVektoru.doesnt_match(anahtarKelimeler))
    print(benzerlik)
    print("----------")
    farkliBul()

farkliBul()