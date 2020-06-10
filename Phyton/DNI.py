strdni = "71940592-0"
strcarnetdeextranjeria = "001575294"
 
#print (strdni[9])
 
strparte1 = strdni[0:8]
 
#print (strparte1)
 
strparte2 = strdni[9]
 
#print (strparte2)
 
a = int(strdni[0]) * 3
b = int(strdni[1]) * 2
c = int(strdni[2]) * 7
d = int(strdni[3]) * 6
e = int(strdni[4]) * 5
f = int(strdni[5]) * 4
g = int(strdni[6]) * 3
h = int(strdni[7]) * 2
 
sumadigitos = a+b+c+d+e+f+g+h
divisiondigitos = sumadigitos/11
residuo = sumadigitos % 11
valor11 = 11 - residuo
#suma1 = valor11 + 1
#print (type(divisiondigitos))
serienumerica = "67890112345" 
 
print (serienumerica[valor11])