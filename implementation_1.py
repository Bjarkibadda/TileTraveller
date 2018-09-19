# Markmið leiksins er að komast frá upphafsstað á endastað. Notandi er staddur í völundarhúsi og byrjar á staðsetningu sem við köllum herbergi 1, 1.
#þáttakandi ferðast um eitt herbergi í einu með hverri ákvörðun, 9 herbergi eru í völundarhúsinu. Notanda er gefið upplýsingar hvert hann getur farið í hverju herbergi fyrir sig.
#Þegar þáttakandi hefur er kominn í lokaherbergið hefur hann sigrað leikinn

# https://github.com/Bjarkibadda/TileTraveller.git

staðsetning = 1

while staðsetning !=7 :  
    if staðsetning == 1 or staðsetning == 4 :
        inntak=input("You can travel: (N)orth.: ")
    elif staðsetning == 2:
        inntak=input("You can travel: (N)orth or (E)east or (S)outh.")
    elif staðsetning == 3 or staðsetning == 9:
        inntak=input("You can travel: (E)east or (S)outh.")
    elif staðsetning == 6:
        inntak=input("You can travel: (E)east or (W)est.: ")
    elif staðsetning == 5:
        inntak=input("You can travel: (S)outh or (W)est.: ")
    elif staðsetning == 8:
        inntak=input("You can travel: (N)orth or (S)outh.: ")

    
    if inntak == "N" or inntak == "n":
        if staðsetning == 1 or staðsetning == 2 or staðsetning == 4 or staðsetning == 8:
            staðsetning +=1

    if inntak == "S" or inntak =="s":
        if staðsetning == 2 or staðsetning == 3 or staðsetning == 5 or staðsetning == 8 or staðsetning == 9:
            staðsetning -=1

    if inntak == "W" or inntak == "w":
        if staðsetning == 5 or staðsetning == 6 or staðsetning == 9:
            staðsetning -=3

    if inntak == "E" or inntak== "e" :
        if staðsetning ==2 or staðsetning ==3 or staðsetning ==6:
            staðsetning +=3

print("Victory!")
