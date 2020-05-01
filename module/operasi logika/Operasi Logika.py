#Operasi Logika Python & Prolog
#and(A,B):- A,B.
#or(A,_):- A, !.
#or(_,B):- B, !.
#xor(A,B):- A\=B.
#equal(A,B):- A==B.

andi = 'True'
ganteng = 'True'
mapirs = 'False'
jelek = 'False'

print(andi and ganteng)
print(andi and jelek)
print(mapirs and ganteng)
print(mapirs and jelek)
print('-===================-')
print(andi or ganteng)
print(andi or jelek)
print(mapirs or ganteng)
print(mapirs or jelek)
