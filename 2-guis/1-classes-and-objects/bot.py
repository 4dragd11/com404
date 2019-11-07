class Bot:

    # constructor
    def __init__(self, name, age=0, energy=100, shield=100):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield
         
    # methods
    def display_name(self):
        print("My name is", self.name)
    def display_age(self):
        print("My age is", self.age)
    def display_energy(self):
        print("My energy is", self.energy)
    def display_shield(self):
        print("My shield is", self.shield)


    

# create some bots
beep = Bot("Beep")            
beep.display_name()
beep.display_age()
beep.display_energy()
beep.display_shield()

