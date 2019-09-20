
def valor_moedas(vlr):
    
    vlr2=float(vlr.replace(',','.'))
    val1= "{:.2f}".format(vlr2)
    val=float(val1)
    moedas = [1,0.50,0.20,0.10,0.05, 0.01]
    
    result = ''
    nMoedas = []
    
    for i in moedas:
        nMoedas.append(val/i)
        val %= i
   
    for i in range(len(moedas)):
        
        result += ("Moedas de {} :{} ".format(moedas[i], int(nMoedas[i]),))
    return result


