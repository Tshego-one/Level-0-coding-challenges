word_1 = str(input("Please input your first string: "))
word_2 = str(input("Please input your second string: "))

def common_member():
    """
    Takes two strings and outputs the most common letters amongst the 
    two
    """
    output = [i for i in word_1 if i in word_2]
    return output

print("Common letters: ")
print(set(common_member()))