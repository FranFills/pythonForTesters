import unittest
"""
Write a Python program that checks if a string is a palindrome, Then optionally write a unit test to check your
program's correctness
"""


def palindrome(words):

    if words == words[::-1]:
        return 'The string is a palindrome'
    else:
        return 'The string is not a palindrome'


#words = input('Enter word').lower()

print(palindrome('madam'))

def palindrom1(word):
    rev_str = ''
    word = word.lower()

    for st in word:
        rev_str = (st + rev_str)
    print(rev_str)

    if rev_str == word:
        print('This word is a palindrome')
    else:
        print('This is not a palindrome')


palindrom1('Madam')
palindrom1('automate')


"""class check_palindrome(unittest.TestCase):

    def test_calculate_power(self):
        self.assertEqual(palindrom1(words), word)"""
