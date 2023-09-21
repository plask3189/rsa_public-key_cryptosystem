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

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
decimal_message_as_list = []
base27_list = []

raw_message = input("Input your message: ")
def convert_text_to_bearcatii(raw_message):
    raw_message_as_list = [*raw_message]
    for character in raw_message_as_list:
        decimal_value = (alphabet.index(character) + 1) # The index gets the integer, and we add 1 because bearcatii is from 1-26
        decimal_message_as_list.append(decimal_value)

    print(decimal_message_as_list)
    convert_decimal_message_to_base27(decimal_message_as_list)


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
    print(base27_list)
    print("sum: ", sum)

#convert base27 back to letter
#def convert_base27_nums_back_to_letters(sum):
#    sum % 27


# create prime numbers q and p
def give_random_prime():
    while True:
        random_num = random.randint(100000000,10000000000000) # According to page 41 or textbook it says that the primes should be 100 digits or longer. But for the sake of the hw I'm doing these.
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
    print("n = ", n)
    print("phi = ", phi)
    e = int(input("Public key e: "))

    # If the user enters a number that is not relatively prime to n = pq, then have the user reenter and keep doing this until e and n are coprime, i.e., gcd(e,φ(n)) = 1.
    while (e < phi):
        if (math.gcd(e,phi) == 1):
            #print(f" e = {e} is valid")
            break
        else:
            e = int(input("Please enter a different value for e: "))
    print(f"Public key: ({e},{n})" )
    calculate_euclids_extended_gcd(e, phi)
    d = s % phi
    print(f"Private key: ({d},{n})")

#  the secret key is then chosen to be the pair (d,n) where d is the multiplicative inverse of e mod phi(n).

# After applying the extended gcd algorithm, d = s(mod(phi))
def calculate_euclids_extended_gcd(e, phi):
    # According to page 38 of "Algorithms: Special Topics"
    if(phi == 0):
        g = e
        s = 1
        t = 0
    else:
        remainder = e % phi
        quotient = e//b
        calculate_euclids_extended_gcd(phi, remainder)
        stemp = s
        s = t
        t = (stemp - (t*quotient))
    return g, s, t





def main():
    convert_text_to_bearcatii(raw_message)

    get_public_key()

if __name__ == '__main__':
    main()
