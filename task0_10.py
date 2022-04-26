def common_member(word_1, word_2):

    output = [i for i in word_1.lower() if i in word_2.lower()]
    return output

print("Common letters:",', '.join(set(common_member("house","computers"))))