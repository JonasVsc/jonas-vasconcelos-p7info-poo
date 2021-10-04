def printDecimal(x):
    return x

def printOctal(x):
    return oct(x)

def printHexadecimal(x):
    return hex(x)

def printBinario(x):
    return bin(x)

def imprimirTabela():
    x = 0
    print('''
Decimal Octal Hexadecimal Binario
------- ----- ----------- -------''')
    while x < 256:
        print('{0}       {1}   {2}         {3}'.format(printDecimal(x), printOctal(x), printHexadecimal(x), printBinario(x)))
        x += 1

imprimirTabela()
