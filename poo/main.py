from poo.class_cat import Cat

grosminet = Cat("Sylvestre", "noir")
tom = Cat("Tom", "gris")
print("Je suis", grosminet.getName(), "un chat", grosminet.getColor())
print(grosminet)

grosminet.chasser()
# Cat.chasser()         => impossible car chasser() est une méthode d'instance
grosminet.dormir()
Cat.dormir()
grosminet.miauler()
Cat.miauler()

print(Cat.type)
print(grosminet.type)
print(tom.type)
Cat.type = "Drôle de canaris jaune"
print(Cat.type)
print(grosminet.type)
print(tom.type)



