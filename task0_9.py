def vowel_checker(string):

    vowels = ([v for v in 'AaEeIiOoUu' if v in string.lower()])
    print(f"Vowels: {vowels}")
    
vowel_checker("Umuzi")