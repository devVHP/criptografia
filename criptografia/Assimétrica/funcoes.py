from chave_publica import chave_publica

chave = chave_publica

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
    for word in conteudo:
        texto_descriptografado+=f"{chave[word]}"
    with open('Texto_Descriptografado.txt', 'w', encoding="utf-8") as arquivo:
        arquivo.write(texto_descriptografado)

def abrir_arquivo(diretorio):
    with open(diretorio, "r") as arquivo:
        conteudo = arquivo.read()
        conteudo = conteudo.upper()
    return conteudo
