def vowel_finder(string):

    vowels = ([v for v in 'AaEeIiOoUu' if v in string.lower()])
    print(f"Vowels: {vowels}")
    
vowel_finder("Umuzi")