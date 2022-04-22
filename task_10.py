def common_member(word_1, word_2):

    output = [i for i in word_1 if i in word_2]
    return output

print("Common letters: ")
print(set(common_member("Omphile", "Ompheletse")))