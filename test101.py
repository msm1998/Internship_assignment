def getDiviser(x,y):
    for i in range(x,y+1):
        if(i%7==0 and i%5!=0):
            print(i)

if __name__ == "__main__":
    getDiviser(2000,3200)   