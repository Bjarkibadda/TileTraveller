

def position(staðsetning,direction):
    if direction == "N" or direction =="n":
        staðsetning +=1
    elif direction == "S" or direction =="s":
        staðsetning -=1
    elif direction == "E" or direction == "e":
        staðsetning +=3
    elif direction == "W" or direction == "w":
        staðsetning -=3
    print(staðsetning)
    return staðsetning

def leiðbeiningar(staðsetning):
    if staðsetning == 1 or staðsetning == 4:
        print("You can travel (N)orth")
    elif staðsetning == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif staðsetning == 3 :
        print("You can travel: (E)ast or (S)outh.")
    elif staðsetning == 5 or staðsetning== 9:
        print("You can travel: (S)outh or (W)est.")
    elif staðsetning == 6:
        print("You can travel: (E)ast or (W)est.")
    elif staðsetning == 8:
        print("You can travel: (N)orth or (S)outh.")

        
staðsetning=1

while staðsetning != 7:
    leiðbeiningar(staðsetning)
    direction = input("Direction: ")
    staðsetning = position(staðsetning,direction) 
    #leiðbeiningar(staðsetning)
    
    
