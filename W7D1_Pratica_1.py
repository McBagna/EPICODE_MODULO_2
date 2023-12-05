def lunghezza_delle_parole(myListFunction):
    myReturnList = []
    for word in myListFunction:
        myReturnList.append(len(word))
    return myReturnList
        

if __name__ == "__main__":
    myListA = ["riga","colonna","python","import","socket","matematica","operazioni"]
    myListB = []
    myListB = lunghezza_delle_parole(myListA)
    print(myListB)
