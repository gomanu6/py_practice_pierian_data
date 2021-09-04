# *args and **kwargs

# *args
# returns tuple of arguments

def add_all(*args):
    print(args)
    return sum(args)


# *kwargs
# returns dictionary of keyword: value arguments

def kw_func(**kwargs):
    if 'fruit' in kwargs:
        print('The fruit is ' + kwargs['fruit'])
    print(kwargs)


# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd

def lesser_evens(a, b):
    if (a % 2 == 0 and b % 2 == 0):
        print(min(a, b))
    else:
        print(max(a, b))

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(string):
    split_string = string.lower().split()
    print((split_string))
    if len(split_string) > 2 or len(split_string) < 2:
        print('Incorrect No of Arguments')
    else:
        print(split_string[0][0] == split_string[1][0])


# MASTER YODA: Given a sentence, return a sentence with the words reversed

def yoda(sent):
    split_sent = sent.split()
    rev_sent = split_sent[::-1]
    rev_str = " ".join(rev_sent)
    print(rev_str)


# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def is_next(check_list, check_int):
    the_list = check_list
    the_int = check_int
    for i in range(len(the_list)):
        if the_list[i] == the_int:
            if the_list[i] == the_list[i-1]:
                print(f'The number {the_int} is at position {i-1} and {i}')


# Lambda Expressions

filter(lambda num: num %2 == 0, [1,2,3,4])
map(lambda num: num ** 2, [1,2,3,4])





if __name__ == '__main__':
    answer = add_all(20, 30, 40, 10)
    print(answer)
    kw_func(fruit='apple', veg='cabbage')
    lesser_evens(2, 4)
    lesser_evens(2, 5)
    animal_crackers('hop hole')
    animal_crackers('new maze')
    yoda("this is awesome, how")
    is_next([1,2,3, 3, 4, 4], 4)
