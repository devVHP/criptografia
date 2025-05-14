import chave_simetrica

chave = chave_simetrica.chave

def criptografar(texto, chave):
    texto_criptografado = ''
    for word in texto:
        texto_criptografado+=f"{chave[word]}"
    with open('Texto_Criptografado.txt', 'w', encoding="utf-8") as arquivo:
        arquivo.write(texto_criptografado)


def descriptografar(diretorio, chave):
    with open(diretorio, "r") as arquivo:
        conteudo = arquivo.read()
    texto_descriptografado = ''
    chave = {v: k for k, v in chave.items()}
    for word in conteudo:
        texto_descriptografado+=f"{chave[word]}"
    with open('Texto_Descriptografado.txt', 'w', encoding="utf-8") as arquivo:
        arquivo.write(texto_descriptografado)

def abrir_arquivo(diretorio):
    with open(diretorio, "r") as arquivo:
        conteudo = arquivo.read()
        conteudo = conteudo.upper()
    return conteudo
