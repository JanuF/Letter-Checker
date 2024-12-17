total_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def user_inputs():
    user_letter = input("What letter are you? ")
    user_letter_first = input("What is the first letter of the range? ")
    user_letter_second = input("What is the final letter of the range? ")
    return user_letter, user_letter_first, user_letter_second

def index_letter(user_letter, user_letter_first, user_letter_second):
    index_letter = total_letters.index(user_letter)
    index_letter_first = total_letters.index(user_letter_first)
    index_letter_second = total_letters.index(user_letter_second)
    return index_letter, index_letter_first, index_letter_second


def index_checker(index_letter, index_letter_first, index_letter_second):
    inside_range = False
    if index_letter_first > index_letter_second and index_letter_second <= index_letter <= index_letter_first:
        inside_range = True
        return inside_range
    elif index_letter_second > index_letter_first and index_letter_first <= index_letter <= index_letter_second:
        inside_range = True
        return inside_range
    else:
        return inside_range


user_letter, user_letter_first, user_letter_second = user_inputs()
index_letter, index_letter_first, index_letter_second = index_letter(user_letter, user_letter_first, user_letter_second)
inside_range = index_checker(index_letter, index_letter_first, index_letter_second)

if inside_range == True:
    print(user_letter, "is in the range of", user_letter_first, "and", user_letter_second)
else:
    print(user_letter, "is not in the range of", user_letter_first, "and", user_letter_second)

