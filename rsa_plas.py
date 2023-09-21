#steps:
# Select 2 prime numbers, preferably large, p and q.
# Calculate n = p*q.
# Calculate phi(n) = (p-1)*(q-1)
# Choose a value of e such that 1<e<phi(n) and gcd(phi(n), e) = 1.
# Calculate d such that d = (e^-1) mod phi(n).


# want to input text like "TEST" and convert it to bearcatii


import random
# assign p and q
import math
global s

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
decimal_message_as_list = []
base27_list = []
encrypted_character_list = []
decrypted_character_list = []

raw_message = input("Input your message: ")
def convert_text_to_bearcatii(raw_message):
    raw_message_as_list = [*raw_message]
    for character in raw_message_as_list:
        decimal_value = (alphabet.index(character) + 1) # The index gets the integer, and we add 1 because bearcatii is from 1-26
        decimal_message_as_list.append(decimal_value)

    print("decimal message list: ", decimal_message_as_list)
    # base27_list = convert_decimal_message_to_base27(decimal_message_as_list)
    return decimal_message_as_list


def convert_decimal_message_to_base27(decimal_message_as_list):
    # get the index of the number. Then multiply it by 27 to the power of that index.
    sum = 0
    count = 0 # count is the power
    for number in decimal_message_as_list:
        number = int(number) # convert the list element to an int
        temp = number * (27 ** count) # 27 to the power of count
        count = count + 1
        sum = sum + temp # sum is the result of base 27
        base27_list.append(temp)
    print("base 27 list: ", base27_list)
    print("sum: ", sum)
    return base27_list

# Encrypt each of the integers in the base27_list
def encrypt(base27_list, e, phi):
    for i in base27_list : # each value i represents a character or the message
        encrypted_character = i ** (e % phi) # a message M is encrypted by taking it to the power e(mod n)
        #print("encrypted char: ", encrypted_character)
        encrypted_character_list.append(encrypted_character)
    #print("encrypted_character_list C : ", encrypted_character_list)
    return encrypted_character_list

# def decrypt(encrypted_character_list, d, n):
    # power = d % n
    # for i in encrypted_character_list:
    #     i = int(i)
    #     print("i: ", i)
    #     decrypted_char = pow(i, d)
    #     decrypted_char.fmod(decrypted_char, n)
    #     print("decrypted char: ", decrypted_char)
    #     decrypted_character_list.append(decrypted_char)
    #decrypted = power(encrypted_character_list, d ,n)

    #print("decrypted character_list P : ", decrypted_character_list)



def mod_powers(x, m):
    p, q, n, phi = compute_phi()
    #print("n's value here in mod powers is : ", n)
    if m == 1:
        pow = x
    else:
        if m % 2 == 0 :# if even
            pow = mod_powers(((x*x) % n), ((m)/2)) % n
        else:
            pow = mod_powers(((x*x) % n), ((m-1)/2)) % n
    return(pow)

def conduct_mod_powers(encrypted_character_list, d, n):
    for i in encrypted_character_list:
        x = int(i)
        m =d % n
        result = mod_powers(x, m)
        decrypted_character_list.append(result)
    print("DECRYPT RESULT: ", str(decrypted_character_list))
    return decrypted_character_list

#def convert_decrypted_results_to_text(decrypted_character_list, sum):
#for i in decrypted_character_list:




# create prime numbers q and p
def give_random_prime():
    while True:
        random_num = random.randint(10000,1000000) # According to page 41 or textbook it says that the primes should be 100 digits or longer. But for the sake of the hw I'm doing these.
        if is_prime(random_num):
            return random_num

def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def compute_phi():
    p = give_random_prime()
    q = give_random_prime()
    n = p*q
    phi = (p - 1)*(q - 1)
    #print("phi: ", phi)
    return p, q, n, phi



# We now choose a small odd integer e that is relatively prime with phi(n) and take the public key to be the pair (e,n)
def get_public_key():
    p, q, n, phi = compute_phi()
    #print("n = ", n)
    #print("phi = ", phi)
    e = int(input("Public key e: "))

    # If the user enters a number that is not relatively prime to n = pq, then have the user reenter and keep doing this until e and n are coprime, i.e., gcd(e,φ(n)) = 1.
    while (e < phi):
        if (math.gcd(e,phi) == 1):
            #print(f" e = {e} is valid")
            break
        else:
            e = int(input("Please enter a different value for e: "))
    print(f"Public key: ({e},{n})" )
    return e, phi, n


# After applying the extended gcd algorithm, d = s(mod(phi)).
# We need to do this in order to calculate d which is a component of the private key.
def calculate_euclids_extended_gcd(e, phi):
    # According to page 38 of "Algorithms: Special Topics"
    if(phi == 0):
        g = e
        s = 1
        t = 0
    else:
        remainder = e % phi
        quotient = e//phi
        g, s, t = calculate_euclids_extended_gcd(phi, remainder)
        stemp = s
        s = t
        t = (stemp - (t*quotient))
    print("s = ", s)
    #print("phi = ", phi)

    return g, s, t


def get_private_key(s, phi):
    if s > 0:
        d = s % phi
    else:
        # if s is negative, you will need to add phi to s % phi so that it yields a value between 1 and phi
        s = phi + (s % phi)
        d = s % phi
    return d



def main():
    #convert_text_to_bearcatii(raw_message)
    decimal_message_as_list = convert_text_to_bearcatii(raw_message)
    base27_list = convert_decimal_message_to_base27(decimal_message_as_list)
    e, phi, n = get_public_key()
    g, s, t = calculate_euclids_extended_gcd(e, phi)
    d = get_private_key(s, phi)
    print(f"Private key: ({d},{n})")

    #print(f"s: {s}   phi: {phi}")
    encrypted_character_list = encrypt(base27_list, e, phi)
    print("ENCRYPTED MESSAGE: ", str(encrypted_character_list))
    # decrypt(encrypted_character_list, d, n)
    conduct_mod_powers(encrypted_character_list, d, n)



if __name__ == '__main__':
    main()
