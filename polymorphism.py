class housePets:
    name = ''
    living_enviornment = 'indoors'
    def eat(self):
        print('I can eat')
#inherit from housePets
class Cats(housePets):
    name = 'Needles'
    diet = 'fish'
    #override eat() method
    def eat(self):
        print('Cats like to eat {}'.format(self.diet)) 

#create object of the subclass
kitty = Cats()

kitty.eat()
