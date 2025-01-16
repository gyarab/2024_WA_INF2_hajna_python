def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

def test_fibonacci(n):
    try:
        result = fibonacci(n)
        print(f"Fibonacci({n}) = {result}")
        return result
    except ValueError as e:
        print(e)
        return None

def is_prime(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be an integer")
    if n == 1:
        return False
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both a and b must be integers")
    if a < 1 or b < 1:
        raise ValueError("Both a and b must be positive integers")
    
    start, end = min(a, b), max(a, b)
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def split_into_threes(text):
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    return [text[i:i+3] for i in range(0, len(text), 3)]

def caesar_encode(text):
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    
    for char in text:
        if not (char.isascii() and (char.isalpha() or char == '.' or char == ' ')):
            raise ValueError("text must only contain English letters a-z, A-Z, dot, and space")
    
    encoded_text = []
    for char in text:
        if char.isalpha():
            shift = 3
            if char.islower():
                encoded_text.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            else:
                encoded_text.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        else:
            encoded_text.append(char)
    
    return ''.join(encoded_text)

def caesar_decode(code):
    if not isinstance(code, str):
        raise ValueError("code must be a string")
    
    for char in code:
        if not (char.isascii() and (char.isalpha() or char == '.' or char == ' ')):
            raise ValueError("code must only contain English letters a-z, A-Z, dot, and space")
    
    decoded_text = []
    for char in code:
        if char.isalpha():
            shift = 3
            if char.islower():
                decoded_text.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
            else:
                decoded_text.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
        else:
            decoded_text.append(char)
    
    return ''.join(decoded_text)

MORSE_CODE_DICT = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

def morse(text):
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    
    text = text.lower()
    morse_text = []
    
    for char in text:
        if char in 'áäčďéěíňóöřšťúůüýž':
            char = 'a' if char in 'áä' else 'c' if char == 'č' else 'd' if char == 'ď' else 'e' if char in 'éě' else 'i' if char == 'í' else 'n' if char == 'ň' else 'o' if char in 'óö' else 'r' if char == 'ř' else 's' if char == 'š' else 't' if char == 'ť' else 'u' if char in 'úůü' else 'y' if char == 'ý' else 'z'
        if char in MORSE_CODE_DICT:
            morse_text.append(MORSE_CODE_DICT[char])
        elif char == ' ':
            morse_text.append('/')
    
    return ' '.join(morse_text)

if __name__ == "__main__":
    print(morse("Hana"))
    test_fibonacci(10)
    test_fibonacci(-1)
    test_fibonacci(0)
    test_fibonacci(1)
    test_fibonacci(5)
    try:
        print(is_prime(11))
        print(is_prime(4))
        print(is_prime(1))
        print(is_prime(-1))
        print(is_prime(0.9))
    except ValueError as e:
        print(e)
    try:
        print(primes_in_range(10, 20))
        print(primes_in_range(20, 10))
        print(primes_in_range(1, 10))
        print(primes_in_range(10, -5))
    except ValueError as e:
        print(e)
    try:
        print(split_into_threes("abcdefghij"))
        print(split_into_threes("abcdefghi"))
        print(split_into_threes("ab"))
        print(split_into_threes(123))
    except ValueError as e:
        print(e)
    try:
        print(caesar_encode("Hello World."))
        print(caesar_encode("áž"))
    except ValueError as e:
        print(e)
    try:
        print(morse(123))
        print(morse("Hello World"))
        print(morse("Příliš žluťoučký kůň úpěl ďábelské ódy 123"))
    except ValueError as e:
        print(e)