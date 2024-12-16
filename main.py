total_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def user_inputs():
    user_letter = input("What letter are you? ")
    user_letter_first = input("What is the first letter of the range? ")
    user_letter_second = input("What is the final letter of the range? ")
    return user_letter, user_letter_first, user_letter_second

def check_letter(user_letter, user_letter_first, user_letter_second):
    in_range = True
    for user_letter in total_letters:
        if user_letter_first <= user_letter <= user_letter_second:
            in_range = False
            print("Your letter is in this range")
            break
    return in_range


