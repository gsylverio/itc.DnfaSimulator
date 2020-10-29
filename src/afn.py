#Individual: 10687861

def testaCadeia(passo, estadoCorrente, transicoes, cadeia, aceitos):
    if (passo >= len(cadeia)):
        if str(estadoCorrente) in aceitos:
            return True
        else:
            if 0 in transicoes[estadoCorrente]:
                p1 = transicoes[estadoCorrente][0]
                for p in p1:
                    if (testaCadeia(passo, p, transicoes, cadeia, aceitos)):
                        return True

            return False
    proximo = int(cadeia[passo])

    if proximo in transicoes[estadoCorrente]:
        possibilidades = transicoes[estadoCorrente][proximo]
        for possibilidade in possibilidades:
            if (testaCadeia(passo + 1, int(possibilidade), transicoes, cadeia, aceitos)):
                return True

    if 0 in transicoes[estadoCorrente]:
        p1 = transicoes[estadoCorrente][0]
        for p in p1:
            if proximo in transicoes[p] or 0 in transicoes[p]:
                if (testaCadeia(passo, p, transicoes, cadeia, aceitos)):
                    return True

entrada = open("entrada.txt", "r").readlines()
nAutomatos = int(entrada[0])
linhaAtual = 1
resp = ""
for i in range(0, nAutomatos):
    #Define especificações
    especificacoes = dict()
    especificacoes = {
                        "nAutomato": i,
                        "nEstados": int(entrada[linhaAtual].split(' ')[0]),
                        "nSimbolos": int(entrada[linhaAtual].split(' ')[1]),
                        "nTransicoes": int(entrada[linhaAtual].split(' ')[2]),
                        "estadoInicial": int(entrada[linhaAtual].split(' ')[3]),
                        "nEstadosAceitos": int(entrada[linhaAtual].split(' ')[4]),
                        "estadosAceitos": entrada[linhaAtual + 1].replace('\n','').split(' ')
                     }
    linhaAtual+= 2

    transicoes = {key: {} for key in range(0,especificacoes['nEstados'])}
    for i in range(0, especificacoes['nTransicoes']):
        estadoCorrente = int(entrada[linhaAtual].split(' ')[0])
        simbolo = int(entrada[linhaAtual].split(' ')[1])
        estadoNovo = int(entrada[linhaAtual].split(' ')[2])

        if simbolo not in transicoes[estadoCorrente]:
            transicoes[estadoCorrente][simbolo] = [estadoNovo]
        else:
            transicoes[estadoCorrente][simbolo].append(estadoNovo)
        linhaAtual+= 1

    especificacoes['nTestes'] = int(entrada[linhaAtual])
    linhaAtual+= 1
    for i in range(0, especificacoes['nTestes']):
        cadeia = entrada[linhaAtual].replace('\n','').split(' ')
        estado = especificacoes['estadoInicial']
        if(testaCadeia(0, estado, transicoes, cadeia, especificacoes['estadosAceitos'])):
            resp+= "1 "
        else:
            resp+="0 "
        linhaAtual+= 1
    resp+="\n"
saida = open(r"saida.txt","w+") 
saida.write(resp)
saida.close()


        






    
    
