
from utils import *

print("Code par FERY Simon et DURAFFOURG Maud")
print('Exercice RSA')


# message à chiffrer et déchiffrer
m = 65483

# Générer un nombre avec un certain nombre de chiffres
#print(len(str(2**2048)))
nb_digits = 2

# Générer p et q
p = generate_prime_number(nb_digits)
q = generate_prime_number(nb_digits)
# TODO : verifier distinction entre p et q
print("p choisi : ", p, "\n")
print("q choisi : ", q, "\n")

# Calculer n
n= p*q
print("n calculé : ", n, "\n")


# Choisir un exposant de chiffrement e
e = 9007
print(is_Prime(e))


def crypting_RSA(n, e, plaintext):
	"""
	m the message to crypt as a list of two digit int
	n the mod (int)
	e the exposant (int)
	"""
	cypher = [ (m ** e) % n  for m in plaintext]
	return cypher

def decrypt_RSA(p, q, e, cypher):
	d = modinv(e , (p-1)*(q-1))
	plaintext = [(c**d)% (p*q) for c in cypher]
	return plaintext

print(modinv(7467,11 200))



