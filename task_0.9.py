string = str(input("Please input string: "))

def vowel_checker():
    """
    Takes a strings and outputs the vowels from that string
    """
    vowel = [each for each in string if each in vowels]
    print(f"Vowels: {vowel}")
     
vowels = "AaEeIiOoUu"
vowel_checker()