
from utils import *
import time

print("Code par FERY Simon et DURAFFOURG Maud")
print('Exercice RSA')

# message à chiffrer et déchiffrer
m = 65483

# Générer un nombre avec un certain nombre de chiffres
#print(len(str(2**2048)))
nb_digits = 20

# Générer p et q
start_time = time.time()
p = generate_prime_number(nb_digits)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
q = generate_prime_number(nb_digits+2)
print("--- %s seconds ---" % (time.time() - start_time))

# TODO : verifier distinction entre p et q
print("p choisi : ", p, "\n")
print("q choisi : ", q, "\n")

# Calculer n
n= p*q
print("n calculé : ", n, "\n")

# Choisir un exposant de chiffrement e
# 𝑝𝑔𝑐𝑑( 𝑒 , (𝑝−1)(𝑞−1) ) = 1
e = generate_cypher_exponent(p,q)
print("e choisi : ", e, "\n")
print("Taper le message a crypter en minuscule : ")
message = input();

plaintext = create_plaintext(message)

print("Le message choisit donne, en chiffre : ", plaintext, "\n")

cypher = crypting_RSA(n, e, plaintext)

print("Le cypher donne : ", cypher, "\n")

plaintextDecrypt = decrypt_RSA(p, q, e, cypher)

print("Le message decode donne : ", plaintextDecrypt, "\n")