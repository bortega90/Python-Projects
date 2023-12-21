class housePets:
    name = ''
    living_enviornment = 'indoors'
    def eat(self):
        print('I can eat')
#inherit from housePets
class Cats(housePets):
    name = 'Needles'
    diet = 'fish'
    lifestyle = 'couch potato'
    mood = 'apathetic'
    #override eat() method
    def eat(self):
        print('Cats enjoy eating {}.'.format(self.diet))

class Dogs(housePets):
    name = 'Ollie'
    diet = 'meat'
    sleep_cycle = 'diurnal'
    age = 2
    

    def eat(self):
        print('Dogs eat all kinds of {}.'.format(self.diet))
        

#create object of the subclass
if __name__ == '__main__':
    kitty = Cats()
    doggy = Dogs()
    
    doggy.eat()
    kitty.eat()

