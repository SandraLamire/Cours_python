# Bienvenue dans votre premier programme Python
"""Commentaire
mutlilignes
"""

# BASICS
print('Hello World !')

my_name = input("Entrer votre nom :\n")

print("Hello ", my_name)

result = int(input("Quel âge avez-vous?\n"))
if result < 18:
    print("Ici je suis dans ma condition")
    print("Vous êtes mineur")
print("Ici je ne suis plus dans ma condition")

# LOOPS
# i = 0
# while 1 < 10:
#     print(i)
#     i += 1

# Max exclus
for j in range(0, 11):
    print("j :" + str(j))

# String
hello = "Hello World !"

# Affiche Hell
print(hello[:4])
# Affiche une lettre sur 2  : HloWrd! (:: = un pas de 2)
print(hello[::2])

# String format
world = "world"
print("%s %s !" % ("Hello", world))

print("le {1} ne s'accocie pas {0} le {2}".format("avec", "Lion", "Cafard"))

word = "tombeau"
rire = "Ha" + "ha" * 3
print(f"Ce {word} sera votre {word}\n\t{rire}!")

print(f"Ce {word} sera votre {word}\n\t🤣")

# Le 0 et le 1 font référence à l'index de l'élément = affiche 01400 et 0654
print("CP = {0:05} PIN = {1:04}".format(1400, 654))

##############################################################################




