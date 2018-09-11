""" This module is python practice exercises to cover more advanced topics.
	Many of the exercises can be found at: 
        http://www.practicepython.org/exercises/
		https://www.hackerrank.com/domains/python/py-introduction
        (hackerrank will ask you to sign up, but you can just close the popup)
	You may submit them there to get feedback on your solutions, and for a
        discussion of how to do each exercise.
	Put the code for your solutions to each exercise in the appropriate function.
	DON'T change the names of the functions!
	You may change the names of the input parameters.
	Put your code that tests your functions in the if __name__ == "__main__": section
	Don't forget to regularly commit and push to github.
    Please include an __author__ comment so I can tell whose code this is.
"""

# Practice Python Exercise
# found at http://www.practicepython.org/exercises/

# 7: List Comprehensions
def even_list_elements(input_list):
    """ Use a list comprehension/generator to return a new list that has 
        only the even elements of input_list in it.
    """
    pass


# 10: List Overlap Comprehensions
def list_overlap_comp(list1, list2):
    """ Use a list comprehension/generator to return a list that contains 
        only the elements that are in common between list1 and list2.
    """ 
    pass




# More List Comprehension Practice!
# Implement the following function:

def cube_triples(input_list):
    """ Use a list comprehension/generator to return a list with the cubes
        of the numbers divisible by three in the input_list.
    """

    pass


# More practice with Dictionaries, Files, and Text!
# Implement the following functions:

def longest_sentence(text_file_name):
    """ Read from the text file, split the data into sentences,
        and return the longest sentence in the file.
    """
    pass


def longest_word(text_file_name):
    """ Read from the text file, split the data into words,
        and return the longest word in the file.
    """
    pass


def num_unique_words(text_file_name):
    """ Read from the text file, split the data into words,
        and return the number of unique words in the file.
        HINT: Use a set!
    """

    pass

def most_frequent_word(text_file_name):
    """ Read from the text file, split the data into words,
        and return a tuple with the most frequently occuring word 
        in the file and the count of the number of times it appeared.
    """

    pass


# Hackerrank Class Exercises
# found at https://www.hackerrank.com/domains/python/py-classes

#Class 2 - Find the Torsional Angle
# class Points(object):
#     def __init__(self, x, y, z):

#     def __sub__(self, no):

#     def dot(self, no):

#     def cross(self, no):
        
#     def absolute(self):
#         return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


# #Classes: Dealing with Complex Numbers
# class Complex(object):
#     def __init__(self, real, imaginary):
        
#     def __add__(self, no):

#     def __sub__(self, no):
        
#     def __mul__(self, no):

#     def __truediv__(self, no):
        
#     def mod(self):

#     def __str__(self):
#         if self.imaginary == 0:
#             result = "%.2f+0.00i" % (self.real)
#         elif self.real == 0:
#             if self.imaginary >= 0:
#                 result = "0.00+%.2fi" % (self.imaginary)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.imaginary))
#         elif self.imaginary > 0:
#             result = "%.2f+%.2fi" % (self.real, self.imaginary)
#         else:
#             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
#         return result


# Hackerrank RegEx Exercises
# found at https://www.hackerrank.com/domains/python/py-regex
# If you are unfamiliar with RegEx, look here:
# A gentle introduction about what RegEx is: 
#   https://docs.python.org/3/howto/regex.html#regex-howto
# The library reference for regex in python3: 
#    https://docs.python.org/3/library/re.html

#Validating and Parsing Email Addresses
def validate_email_addresses(address_list):
    """ Take a list of names and email addresses and return a list with
        only the valid ones. See the webpage for validity requirements.
    """
    pass



#Regex Substitution
def sub_and_or(string_list):
    """ Take a list of strings and return a list of strings with:
            ' && ' replaced by ' and '
            ' || ' replaced by ' or '
    """

    pass


#Validating Credit Card Numbers
def validate_cc_numbers(ccnumber_list):
    """ Take a list of strings and return a list with 'Valid' or 'Invalid'
        strings in the appropriate place in the list. See the webpage for 
        validity requirements.
    """
    pass



#Validating Postal Codes
def validate_postal_code(zipcode_list):
    """ Take a list of strings and return a list of 'True' or 'False' strings
        in the appropriate place in the list. See the webpage for validity
        requirements.
    """
    pass



if __name__ == "__main__":
    # put your test code here

    print('Hello')