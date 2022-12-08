#Most Similar Example

from gensim.models import KeyedVectors

kelimeVektoru = KeyedVectors.load_word2vec_format('trModel100', binary=True)

def benzerKelimeler():

    anahtarKelime = input("Anahtar Kelime: ").lower()
    print("Anahtar Kelime : "+ str(anahtarKelime))
    oneriler = (kelimeVektoru.most_similar(positive=anahtarKelime))
    print(oneriler)

benzerKelimeler()