
from utils import *

print("Code par FERY Simon et DURAFFOURG Maud")
print('Exercice RSA')


# Générer un nombre avec un certain nombre de chiffres
#print(len(str(2**2048)))
nb_digits = 200

# Générer p et q
p = generate_prime_number(nb_digits)
q = generate_prime_number(nb_digits)
print("p choisi : ", p, "\n")
print("q choisi : ", q, "\n")

# Calculer n
n= p*q
print("n calculé : ", n, "\n")


# Choisir un exposant de chiffrement e
e = 0




