def soma_primos(n):
    if n > 0:
        numero = 1
        divisor = 1
        contador = 0
        soma_n_numeros_primos = 0
        verificador = 0
        while True:
            # verifica se o numero é maior ou igual que o divisor
            if numero >= divisor:
                # verifica se o resto foi zero, se sim aumenta o contador em 1
                if numero % divisor == 0:
                    contador += 1
            # se o numero nao for maior que o divisor ele entra para verificar se o numero é primo
            else:
                # se o contador for 2 ele guarda o numero em uma lista, pois é um numero primo e reinicia o teste com o proximo numero
                if contador == 2:
                    soma_n_numeros_primos += numero
                    verificador += 1
                    numero += 1
                    contador = 0
                    divisor = 0
                    # verifica se o n foi a quantidade de vezes que um numero primo foi guardado se sim retorna a lista
                    if verificador == n:
                        return soma_n_numeros_primos
                # se o contador nao for 2 ele aumenta o valor do numero e reinicia o divisor e o contador para 0
                else:
                    numero += 1
                    divisor = 0
                    contador = 0
            # incrementa o divisor em 1
            divisor += 1