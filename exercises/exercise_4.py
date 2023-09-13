# Exercise 4: Create a function to check whether the brackets in a given string are balanced or not.

def are_brackets_balanced(s):
    # Your code here
    if len(s)%2==0:
        for i in range(int(len(s)/2)):
            if s[i] == "(":
                if s[len(s)-i-1]!=")":
                    return False
            elif s[i] == "[":
                if s[len(s)-i-1]!="]":
                    return False
            elif s[i] == "{":
                if s[len(s)-i-1]!="}":
                    return False
        return True
    return False
# Unit tests
import unittest

class TestExercise4(unittest.TestCase):

    def test_are_brackets_balanced(self):
        self.assertTrue(are_brackets_balanced("({[]})"))
        self.assertFalse(are_brackets_balanced("([)]"))
        self.assertFalse(are_brackets_balanced("{[}"))

if __name__ == '__main__':
    unittest.main()
