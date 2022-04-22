def vowel_checker(string):

    vowels = ([v for v in 'aeiou' if v in string])
    print(f"Vowels: {vowels}")
    
vowel_checker("umuzi")