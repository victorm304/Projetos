import hashlib

def sha256(bytes):
    algoritmo = hashlib.sha256()
    algoritmo.update(bytes)
    return algoritmo.digest()

def verificar_integridade(b1, b2):
    return b1 == b2

with open("thorium-browser_121.0.6167.204_AVX.deb", "rb") as arq1, open("thorium", "rb") as arq2:
    arq1Bytes = [x for x in arq1.read()]
    arq2Bytes = [y for y in arq2.read()]

    print(sha256(bytes(arq1Bytes)), sha256(bytes(arq2Bytes)))