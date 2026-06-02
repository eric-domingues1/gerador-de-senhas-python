import string
import random

def gerar_senha(tamanho):
    while tamanho < 4:
        print('Senha muito pequena, tente novamente.')
        tamanho = int(input('Insira mais de 4 caracteres para gerar sua senha : '))

    senha = [random.choice(string.ascii_letters),
                 random.choice(string.digits),
                 random.choice(string.punctuation) ]
        
    possibilidades="".join (random.choices(string.ascii_letters + string.digits + string.punctuation, k=tamanho -3))

    senha.extend(possibilidades)

    random.shuffle(senha)

    return "".join(senha)
    
tamanho = int (input('Digite o tamanho da senha :'))
print(gerar_senha(tamanho))