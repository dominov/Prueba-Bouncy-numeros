def verificarNumero(numero):
    aumento = dimin = False
    i=0
    for digito in numero:
        if (i > 0):
            if digito > numero[i - 1]:
                aumento = True
            elif digito < numero[i - 1]:
                dimin = True
            
            if aumento and  dimin:
                return "="
            
        i +=1
      


n = 0
bouncy = porcentaje = 0
while porcentaje<99:
    n+=1
    simbolo = verificarNumero(str(n))

    if simbolo == "=":
        bouncy+=1
    
    porcentaje =  100 * bouncy / n
   # print(n,simbolo,porcentaje)
    

print("Para {} El porcentaje {}".format(n, porcentaje))
