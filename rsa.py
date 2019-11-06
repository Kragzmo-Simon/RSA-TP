
from utils import *
import time

print("Code par FERY Simon et DURAFFOURG Maud")
print('Exercice RSA\n')

# message à chiffrer et déchiffrer
m = 65483

# Générer un nombre avec un certain nombre de chiffres
#print(len(str(2**2048)))
nb_digits = 200

# Générer p et q
start_time = time.time()
p = generate_prime_number(nb_digits)
end_time_p = time.time() - start_time

start_time = time.time()
q = generate_prime_number(nb_digits+2)
end_time_q = time.time() - start_time

print("p choisi : ", p)
print("Trouvé en %s seconds ---" % end_time_p, "\n")

print("q choisi : ", q)
print("Trouvé en %s seconds ---" % end_time_q, "\n")

# Calculer n
n= p*q
print("n calculé : ", n, "\n")

# Choisir un exposant de chiffrement e
# 𝑝𝑔𝑐𝑑( 𝑒 , (𝑝−1)(𝑞−1) ) = 1
e = generate_cypher_exponent(p,q)
print("e choisi : ", e, "\n")

# Choix du message à chiffrer
#print("Taper le message a crypter en minuscule : ")
message = "chainedecaractereatester"
print("Message à crypter/décrypter : ", message)

plaintext = create_plaintext(message)

print("Le message choisit donne, en chiffre : ", plaintext, "\n")

cypher = crypting_RSA(n, e, plaintext)

print("Le cypher donne : ", cypher)

start_time = time.time()
plaintextDecrypt = decrypt_RSA(p, q, e, cypher)
end_time_decrypt = time.time() - start_time

print("Le message decode donne : ", plaintextDecrypt)
print("Trouvé en %s seconds ---" % end_time_decrypt, "\n")

# Temps moyens pour cryptage et décryptage
nb_chiffres = 200
print("Temps moyen de génération des nombres premiers (", nb_chiffres, " chiffres): ")
[average_time, data] = average_time_for_generate_prime_number(nb_chiffres, 20)
print(average_time, " secondes\n")

print("Temps moyen de l'exponentiation modulaire (", nb_chiffres, "chiffres): ")
average_time = average_time_for_decryption(data)
print(average_time, " secondes\n")
