# def is_armstrong_number(number):
#     base = list(str(number))
#     print(base)
#     sub_base = []
#     for sub in base:
#         sub_base.append(int(sub))
#     print(sub_base)
#     numbers_raised = []
#     final_sum = 0
#     for power in sub_base:
#         numbers_raised.append(power ** len(sub_base))
#     print(numbers_raised)
#     for final in numbers_raised:
#         final_sum = final_sum + final
#     print(final_sum)
#     return final_sum

# is_armstrong_number(123)

# def square_of_sum(number):
#     square_sum = 0
#     for item in range(1,number + 1)
#         square_sum = square_sum + item
#     return square_sum ** 2

# def sum_of_squares(number):
#     sum_squares = 0
#     for item in range(1,(number+1))
#         sum_squares = sum_squares + (item ** 2)
#     return sum_squares


# def difference_of_squares(number):
#     return square_of_sum(number) - sum_of_squares(number)

# def steps(number):
#     step_by_step = []
#     if number < 0:
#         raise ValueError("Only positive integers are allowed")
#     elif number % 2 == 0:
#         step_by_step.append(number/2)
#         steps(step_by_step[len(step_by_step)-1])
#     else:
#         if step_by_step[len(step_by_step)-1] == 1:
#             return len(step_by_step)
#         else:
#             step_by_step.append((number * 3) + 1)
#             steps(step_by_step[len(step_by_step)-1])

# print(steps(16))

# def steps(number):
#     if number <= 0:
#         raise ValueError("Only positive integers are allowed")
#     else:
#         step_by_step = []
#         base = number
#         while base != 1:
#             if base % 2 == 0:
#                 base = base / 2
#                 step_by_step.append(base)
#             else:
#                 base = (base * 3) + 1 
#                 step_by_step.append(base)
#         return len(step_by_step)

# print(steps(0)) 

# import random

# def private_key(p):
#     return random.randint(2,p-1)


# def public_key(p, g, private):
#     return g ** private % p


# def secret(p, public, private):
#     return public ** private % p

# print(private_key(15))
# print(public_key(1246, 6, private_key(15)))

# from collections import Counter

# arr = [6, 2, 5, 2, 7]

# count = Counter(arr)
# # print(list(count.items())[0][0])
# arr.sort()
# if arr == [2,3,4,5,6]:
#     print(arr)
# else:
#     print("que haceee")
# print(list(count.items()).sort())
# repeat_numbers = []

# for element, frequency in count.items():
#     if 1 < frequency <= 3:
#         repeat_numbers.append("element": "frequency")
        


#     print(f"El elemento {element} se repite {frequency} veces.")


# from collections import Counter
# """
# en este ejercicio se habla de un juego de cartas parecido al poker 
# en el cual hay varias formas de sumar puntos y todas las formas
# tienen que ser validadas
# """
# # Score categories.
# # Change the values as you see fit.
# YACHT = "YACHT"
# ONES = "ONES"
# TWOS = "TWOS"
# THREES = "THREES"
# FOURS = "FOURS"
# FIVES = "FIVES"
# SIXES = "SIXES"
# FULL_HOUSE = "FULL_HOUSE"
# FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
# LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
# BIG_STRAIGHT = "BIG_STRAIGHT"
# CHOICE = "CHOICE"


# def score(dice, category):
#     if len(dice) == 5:
#         for item in dice:
#             if not 1 <= item <= 6:
#                 raise ValueError("the number is out of range")
#         count = Counter(dice)
#         for num, frequency in count.items():
#             print(count.items())
#             print(frequency)
#             if frequency == 5 and category == YACHT:
#                 return 50
#             elif frequency <= 5 and num == 1 and category == ONES:
#                 print("llego aqui unos")
#                 return num * frequency
#             elif frequency <= 5 and num == 2 and category == TWOS:
#                 return num * frequency
#             elif frequency <= 5 and num == 3 and category == THREES:
#                 return num * frequency
#             elif category == FOURS and frequency <= 5 and num == 4:
#                 print("llego aqui")
#                 return num * frequency
#             elif frequency <= 5 and num == 5 and category == FIVES:
#                 return num * frequency
#             elif frequency <= 5 and num == 6 and category == SIXES:
#                 return num * frequency
#             elif len(count.items()) == 2 and frequency == 3 and category == FULL_HOUSE:
#                 n1 = list(count.items())[0][0] * list(count.items())[0][1]
#                 n2 = list(count.items())[1][0] * list(count.items())[1][1]                
#                 return n1 + n2
#             elif (len(count.items()) == 2 or len(count.items()) == 1) and frequency >= 4 and category == FOUR_OF_A_KIND:
#                 if frequency == 5:
#                     return list(count.items())[0][0] * (list(count.items())[0][1] - 1)
#                 else:
#                     return list(count.items())[0][0] * list(count.items())[0][1]
            
#             dice.sort()
#             if len(count.items()) == 5 and dice == [1,2,3,4,5] and category == LITTLE_STRAIGHT:
#                 return 30
#             elif len(count.items()) == 5 and dice == [2,3,4,5,6] and category == BIG_STRAIGHT:
#                 return 30
#             elif category == CHOICE:
#                 return sum(dice)
#         return 0 
#     else:
#         return 0
    

# print(score([3, 3, 3, 3, 3], FOUR_OF_A_KIND))
# def convert(number):
#     if number % 3 == 0:
#         return "Pling"
#     elif number % 5== 0:
#         return "Plang"
#     elif number % 7 == 0:
#         return "Plong"
#     else:
#         return str(number)
    
# remainder = 1 % 3
# print(remainder) 

# print(convert(6))

# def translate(text):
#     vowel = ["a", "b", "c", "d", "e", "f"]
#     text.strip()
#     letter = text[0]
#     if letter in vowel:
#         return "".join([text, "ay"])
    
# print(translate("apple"))

# def translate(text):
#     vowel = ["a", "e","i", "o", "u", "xr", "yt"]
#     consonant = ["b", "c","d", "f", "g", "h", "j", "k", "l","m", "n", "p", "q", "r", "s", "t", "v", "x", "y", "z"]
#     text.strip()
#     letter = text[0]
#     sound_or_double = text[0] + text[1]
#     qu = text[1] + text[2]
#     if letter in vowel or sound_or_double in vowel:
#         return "".join([text, "ay"])
#     elif letter in consonant:
#         constant = ""
#         body = ""        
#         if sound_or_double == "ch" or sound_or_double == "ll":
#             constant = sound_or_double
#             body = text[2:]
#         elif qu == "qu":
#             print("llegamos aqui y esto eku:" + qu)
#             constant = letter + qu
#             body = text[3:]
#         else:
#             constant = letter
#             body = text[1:]
#         return body + constant + "ay"

# print(translate("queen"))

# def translate(text):
#     vowel = ["a", "e","i", "o", "u", "xr", "yt"]
#     consonant = ["b", "c","d", "f", "g", "h", "j", "k", "l","m", "n", "p", "q", "r", "s", "t", "v", "x", "y", "z"]
#     text.strip()
#     if " " in text:
#         new_text = text.split()
#         return new_text
#     letter = text[0]
#     sound_or_double = text[0] + text[1]
#     qu1 = ""
#     if len(text) >= 3:
#         qu1 = text[1] + text[2]
#     qu2 = text[0] + text[1]
#     if letter in vowel or sound_or_double in vowel:
#         return "".join([text, "ay"])
#     elif letter in consonant:
#         constant = ""
#         body = ""        
#         if sound_or_double == "ch" or sound_or_double == "ll" or sound_or_double == "th" :
#             indexh = text.index("h")
#             if text[indexh - 1] == "t" and text[indexh + 1] == "r":
#                 constant = sound_or_double + text[indexh + 1]
#                 body = text[3:]
#             else:
#                 constant = sound_or_double
#                 body = text[2:]
#         elif qu1 == "qu" or qu1 == "ch":
#             constant = letter + qu1
#             body = text[3:]
#         elif qu2 == "qu":
#             constant = qu2
#             body = text[2:]
#         elif letter == "y" or "y" in text:
#             index = text.index("y")
#             if text[index-1] in consonant:
#                 constant = text[:index]
#                 body = text[index:]
#             else:
#                 constant = letter
#                 body = text[1:]
#         else:
#             constant = letter
#             body = text[1:]
#         return body + constant + "ay"

# def make_word_groups(vocab_words):
#     """Transform a list containing a prefix and words into a string with the prefix followed  by the words with prefix prepended.

#     :param vocab_words: list - of vocabulary words with prefix in first index.
#     :return: str - of prefix followed by vocabulary words with
#             prefix applied.

#     This function takes a `vocab_words` list and returns a string
#     with the prefix and the words with prefix applied, separated
#      by ' :: '.

#     For example: list('en', 'close', 'joy', 'lighten'),
#     produces the following string: 'en :: enclose :: enjoy :: enlighten'.
#     """
#     new_vocab = ""
#     for index, element in enumerate(vocab_words):
#         if index == 0:
#             new_vocab += (element + " " + ":: ")
#         elif index == len(vocab_words) - 1:
#             new_vocab += (element)
#         else:
#             new_vocab += (element + " " + ":: ")

#     return new_vocabe

# def is_pangram(sentence):
#     alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     to_lower = sentence.lower()
#     close = "".join(to_lower.split())
#     without_numbers = ''.join(caracter for caracter in close if not caracter.isdigit())
#     without_special_caracter = ''.join(caracter for caracter in without_numbers if caracter.isalnum())
#     org = sorted(set(without_special_caracter))
#     if org == alphabet:
#         return True
#     else: 
#         return False
# from collections import Counter

# def is_isogram(string):
#     if len(string) == 0:
#         return True
#     else:
#         without_caracter = "".join(caracter for caracter in string if caracter.isalnum())
#         print(without_caracter)
#         to_lower = without_caracter.lower()
#         key_value = Counter(to_lower)
#         all_ok = True
#         for item, freq in key_value.items():
#             if freq != 1:
#                 all_ok = False
#         return all_ok

# def is_valid(isbn):
#     formula_items = [10,9,8,7,6,5,4,3,2,1]
#     without_caracters = "".join(caracter for caracter in isbn if caracter.isalnum())
#     if len(without_caracters) == 10:
#         isbn_vec = [caracter for caracter in without_caracters]
#         alphabet = 0
#         for item in isbn_vec:
#             if item.isalpha():
#                 alphabet += 1
#         if alphabet > 1:
#             return False
#         elif alphabet == 1:
#             if isbn_vec[-1] == "X":
#                 isbn_vec[-1] = "10"
#             else:
#                 return False
#         to_int = [int(caracter) for caracter in isbn_vec]
#         multiply = [a * b for a , b in zip(formula_items, to_int)]
#         sum = 0
#         for item in multiply:
#             sum += item
#         if sum % 11 == 0:
#             return True
#         else:
#             return False
#     else:
#         return False

def rotate(text, key):
    plain = "abcdefghijklmnopqrstuvwxyz"
    rotated = ""
    for letter in text:
        if not letter.isalnum() or letter.isspace() or letter.isnumeric():
            rotated += letter
        elif letter.isupper():
            lower_letter = letter.lower()                        
            index_letter = plain.index(lower_letter)
            subText = ""
            for _ in range(key + 1):
                subText += plain[index_letter]
                index_letter = (index_letter + 1) % len(plain)
            rotated += subText[-1].upper()
        else:
            index_letter = plain.index(letter)
            subText = ""
            for _ in range(key + 1):
                subText += plain[index_letter]
                index_letter = (index_letter + 1) % len(plain)
            rotated += subText[-1]
    return rotated   
    
print(rotate("The quick brown fox jumps over the lazy dog.", 13))