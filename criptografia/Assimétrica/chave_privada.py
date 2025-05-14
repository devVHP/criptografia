from chave_publica import chave_publica
# Chave privada (decodificação = inversão da chave pública)

chave_privada = {v: k for k, v in chave_publica.items()}
