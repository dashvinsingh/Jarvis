#DO MATH
import math
import operator
import functools
from os import *
import random

ans_voice = ['The answer is: ', 'It is: ', "It is simply: "]
ans_ran = random.choice(ans_voice)

def extract_numbers(text):
    lst = text.split()
    new = []
    for item in lst:
        if (item.lstrip('-').isnumeric()):
            new.append(float(item))
    return new

def return_answer(ans):
    print('Computing...')
    system('say Computing...')
    if ans >= 0:
        print('{0} {1}'.format(ans_ran, ans))
        system('say  {0} {1}'.format(ans_ran, ans))
    else:
        print('{0} {1}'.format(ans_ran, ans))
        system('say {0} negative {1}'.format(ans_ran, abs(ans)))



def addition(text):
    ans = sum(extract_numbers(text))
    return_answer(ans)

def subtraction(text):
    lst = extract_numbers(text)
    ans = functools.reduce(operator.sub,lst)
    return_answer(ans)


def multiplication(text):
    lst = extract_numbers(text)
    ans = functools.reduce(operator.mul, new, 1)
    return_answer(ans)

def division(text):
    lst = extract_numbers(text)
    if any(word in text for word in ['divided by', 'divide by', 'is divisible by ']):
        return_answer(lst[0]/lst[1])
    elif any(word in text for word in ['divides']):
        return_answer(lst[1]/lst[0])

def power(text):
    lst = extract_numbers(text)
    if any(word in text for word in ['squared']):
        return_answer(math.pow(lst[0], 2))
    elif any(word in text for word in ['cubed']):
        return_answer(math.pow(lst[0], 3))
    else:
        if len(lst) == 2:
            return_answer(math.pow(lst[0], lst[1]))
        else:
            return('Invalid power command. More than 2 digits.')

def sqrt(text):
    lst = extract_numbers(text)
    if len(lst) == 2:
        print("{0} {1} and {2}".format(ans_ran, math.sqrt(lst[0]), math.sqrt(lst[1])))
        system("say {0} {1} and {2}".format(ans_ran, math.sqrt(lst[0]), math.sqrt(lst[1])))
    else:
        return_answer(math.sqrt(lst[0]))

def sin(text):
    lst = extract_numbers(text)
    return_answer(round(math.sin(math.radians(lst[0])), 3))
def cos(text):
    lst = extract_numbers(text)
    return_answer(round(math.cos(math.radians(lst[0])), 3))

def tan(text):
    lst = extract_numbers(text)
    return_answer(round(math.tan(math.radians(lst[0])), 3))
    
    
