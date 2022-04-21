string = str(input("Please input string: "))

def vowel_checker():
    """
    Takes a strings and outputs the vowels from that string
    """
    vowels = ([v for v in 'aeiou' if v in string])
    print(f"Vowels: {vowels}")
    
vowel_checker()