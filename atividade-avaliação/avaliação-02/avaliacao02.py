# variaveis
maior_palavra_da_frase = 0
palavra = ''
qtd_char_palavra = []
saida_solicitada = ''
# Gravando em uma lista a frase digitada pelo usuario e colocando '0' caso nao for digitado nada
frase_usuario = input('Digite uma frase: ').split() or '0'

while True:
    # termina o programa caso o usuario digitar '0' ou nada como padrao visto na linha 7
    if frase_usuario[0] == '0':
        break
    elif len(frase_usuario) >= 1 and len(frase_usuario) <= 100:
        for x in frase_usuario:
            # guarda a qtd de caracteres por palavra da lista 'frase_usuario' na lista 'qtd_char_palavra'
            qtd_char_palavra.append(str(len(x)))
            # verifica se a palavra atual da lista frase_usuario é maior, se sim guarda a palavra na variavel 'maior_palavra_da_frase.
            if len(x) >= maior_palavra_da_frase:
                maior_palavra_da_frase = len(x)
                # guarda a maior palavra em 'palavra'
                palavra = x
            # adiciona '-' entre a lista 'qtd_char_palavra' e guarda na string 'saida_solicitada'
            saida_solicitada = '-'.join(qtd_char_palavra)
        # saida
        print(saida_solicitada)
        print('A maior palavra na frase digitada pelo usuario foi: ', palavra)
        print()
        break


