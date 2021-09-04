# First Problem
st01 = 'Print only the words that start with s in this sentence'


def starts_with_s(name):
    # Use a breakpoint in the code line below to debug your script.
    st_split = name.split()
    print(st_split)
    for word in st_split:
        if word[0] == 's':
            print(word)
        else:
            print('No')


# Second Problem
# Use range() to print all the even numbers from 0 to 10.

def print_even():
    list_10 = range(0, 11, 1)
    for num in list_10:
        if num % 2 == 0:
            print(num)


# Third Problem
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

div_by_3 = [x for x in range(1, 50, 1) if x % 3 == 0]

# Fourth Problem
# Go through the string below and if the length of a word is even print "even!"

st02 = 'Print every word in this sentence that has an even number of letters'


def even_words(string):
    split_list = string.split()
    help(split_list)
    for word in split_list:
        if len(word) % 2 == 0:
            print(f'{word} -- This word is even')
        else:
            print(f'{word} -- This word is ODD')


# Fifth Problem
# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz"
# instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three
# and five print "FizzBuzz".


def fizz(limit):
    x = 1
    while x <= limit:
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)
        x += 1


# Sixth Problem
# Use List Comprehension to create a list of the first letters of every word in the string below:
st03 = 'Create a list of the first letters of every word in this string'


def first_letter(string):
    split_phrase = string.split()
    split_list = [x[0] for x in split_phrase]
    print(split_list)


if __name__ == '__main__':
    starts_with_s(st01)
    print_even()
    print(div_by_3)
    even_words(st02)
    fizz(100)
    first_letter(st03)
