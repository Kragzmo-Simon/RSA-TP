import random
from fractions import gcd
import time
 
def is_Prime(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
 
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
 
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(10):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True  

def generate_prime_number(number_of_digits):
    """
    Generate randoms number until it finds a prime number (uses the Miller-Rabin test).
    """
    while True:
        random_number = random.randrange(10**(number_of_digits-1), 10**number_of_digits)
        if is_Prime(random_number):
            return random_number

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def generate_cypher_exponent(p,q):
    pq = (p-1)*(q-1)
    while True:
        random_number = random.randrange(10**3,10**5)
        if gcd(random_number,pq) == 1:
            return random_number

def crypting_RSA(n, e, plaintext):
	"""
	plaintext the message to crypt as a list of int
	n the mod (int)
	e the exposant (int)
	"""
	cypher = [ pow(m, e, n ) for m in plaintext]
	return cypher

def decrypt_RSA(p, q, e, cypher):
	"""
	cypher the message to decrypt
	p, q, e an int 
	"""
	d = modinv(e , (p-1)*(q-1))
	plaintext = [ pow(c, d, (p*q) ) for c in cypher]
	return plaintext

def create_plaintext(message):
	plaintext = [ord(char)-ord("a")+1 for char in message]
	plaintext = ["0"+str(char) if char < 10 else str(char) for char in plaintext ]
	plaintext = "".join(plaintext)
	plaintext = [int(plaintext)]
	return plaintext

