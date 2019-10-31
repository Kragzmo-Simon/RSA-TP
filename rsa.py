
from utils import *
import time

print("Code par FERY Simon et DURAFFOURG Maud")
print('Exercice RSA')



# message à chiffrer et déchiffrer
m = 65483

# Générer un nombre avec un certain nombre de chiffres
#print(len(str(2**2048)))
nb_digits = 200

# Générer p et q
start_time = time.time()
p = generate_prime_number(nb_digits)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
q = generate_prime_number(nb_digits)
print("--- %s seconds ---" % (time.time() - start_time))

# TODO : verifier distinction entre p et q
print("p choisi : ", p, "\n")
print("q choisi : ", q, "\n")

# Calculer n
n= p*q
print("n calculé : ", n, "\n")


# Choisir un exposant de chiffrement e
# 𝑝𝑔𝑐𝑑( 𝑒 , (𝑝−1)(𝑞−1) ) = 1
e = 9007
print(is_Prime(e))




