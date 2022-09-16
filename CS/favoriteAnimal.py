class snakeSpecies:
    def __init__(self, s, p, leng,col):
        self.length = leng
        self.species = s
        self.poisonous = p
        self.color = col

    def setSpecies(self,s):
        self.species = s

    def getSpecies(self):
        return self.species

    def setPoisonous(self,p):
        self.poisonous = p

    def getPoisonous(self):
        return self.poisonous

    def setLength(self,leng):
        self.length = leng

    def getLength(self):
        return self.length

    def setColor(self,col):
        self.color = col

    def getColor(self):
        return self.color

def main():
    #print("Hello World")

    print("Hey welcome to the zoo here are some snakes...")
    
    snake1 = snakeSpecies("Rattle Snake", "yes, it is poisonous", "It is 1.5m", "It is brownish")
    s = snake1.getSpecies()        
    print(s)
    p = snake1.getPoisonous()
    print(p)
    leng = snake1.getLength()
    print(leng)
    print(snake1.getColor())
    snake2=snakeSpecies("Milk Snake","No, it is not poisonous","It is 70cm","It is redish")
    
    print(snake2.getSpecies())
    print(snake2.getPoisonous())
    print(snake2.getLength())
    print(snake2.getColor())
    

if __name__ == "__main__":
    main()
