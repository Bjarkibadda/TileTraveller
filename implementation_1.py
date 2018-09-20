# Markmið leiksins er að komast frá upphafsstað á endastað. Notandi er staddur í völundarhúsi og byrjar á staðsetningu sem við köllum herbergi 1.
#þáttakandi ferðast um eitt herbergi í einu með hverri ákvörðun, 9 herbergi eru í völundarhúsinu en mismunandi er hvert þú getur farið úr hverju herbergi.
# Notanda er gefið upplýsingar hvert hann getur farið í hverju herbergi fyrir sig.
#Þegar þáttakandi hefur er kominn í lokaherbergið hefur hann sigrað leikinn. 
#Uppröðun herbergja er eftirfarandi: 

# 3-6-9
# 2-5-8
# 1-4-7

#Upphafsstaður er herbergi nr. 1.
#Endastaður er herbergi nr. 7.

# https://github.com/Bjarkibadda/TileTraveller.git

staðsetning = 1
while staðsetning !=7 :
    if staðsetning == 1 or staðsetning == 4 :
        print("You can travel: (N)orth.")
        Direction = input("Direction: ")
        while Direction != "N" and Direction != "n":
            print("Not a valid direction!")
            Direction=input("Direction: ")       
        if Direction == "N" or Direction == "n":
            staðsetning+=1
        

    if staðsetning == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        Direction=input("Direction: ")
        while Direction !="N" and Direction !="n" and Direction !="E" and Direction !="e" and Direction !="S" and Direction !="s":
            print("Not a valid direction!")
            Direction=input("Direction: ")
        if Direction == "N" or Direction == "n":
            staðsetning+=1    
        elif Direction == "E" or Direction=="e":
            staðsetning+=3
        elif Direction =="S" or Direction=="s":
            staðsetning-=1

    if staðsetning == 3 :
        print("You can travel: (E)ast or (S)outh.")
        Direction=input("Direction: ")
        while Direction !="E" and Direction !="e" and Direction !="S" and Direction !="s":
            print("Not a valid direction!")
            Direction=input("Direction: ")
        if Direction == "E" or Direction == "e":
            staðsetning+=3
        elif Direction == "S" or Direction == "s":
            staðsetning-=1
        
    if staðsetning == 5 or staðsetning== 9:
        print("You can travel: (S)outh or (W)est.")
        Direction=input("Direction: ")
        while Direction !="S" and Direction !="s" and Direction !="W" and Direction !="w":
            print("Not a valid direction!")
            Direction=input("Direction: ")
        if Direction == "S" or Direction == "s":
            staðsetning-=1
        elif Direction == "W" or Direction == "w":
            staðsetning-=3
        
    if staðsetning == 6:
        print("You can travel: (E)ast or (W)est.")
        Direction=input("Direction: ")
        while Direction !="E" and Direction !="e" and Direction !="W" and Direction !="w":
            print("Not a valid direction!")
            Direction=input("Direction: ")
        if Direction == "E" or Direction == "e":
                staðsetning+=3
        elif Direction == "W" or Direction =="w":
                staðsetning-=3
        
    if staðsetning == 8:
        print("You can travel: (N)orth or (S)outh.")
        Direction=input("Direction: ")
        while Direction !="N" and Direction !="n" and Direction !="S" and Direction !="s":
            print("Not a valid direction!")
            Direction=input("Direction: ")
        if Direction == "N" or Direction == "n":
            staðsetning+=1
        elif Direction == "S" or Direction == "s":
            staðsetning-=1
        
print("Victory!")
