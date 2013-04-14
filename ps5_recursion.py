
# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if len(aStr) == 0:
        return ''
    else:
         return aStr[len(aStr) - 1] + reverseString(aStr[:len(aStr) - 1]) 

#
# Problem 4: Erician
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if len(x) == 0:
        return True
    if len(word) == 0:
        return False
    else:
        if x[0] == word[0]:
            return x_ian(x[1:], word[1:])
        else:
            return x_ian(x, word[1:])
    

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    import string
    wraped = ''
    def insertNewlinesRec(text, wraped, lineLength, cLength):
        if len(text) == 0:
            return wraped
        if text[0] in string.letters or text[0] == '-':
            return insertNewlinesRec(text[1:], wraped + text[0], lineLength, cLength + 1)
        else:
            if cLength + 1 >= lineLength:
                return insertNewlinesRec(text[1:], wraped + text[0] + '\n', lineLength, 0)
            else:
                if cLength == 0 and text[0] == ' ':
                    return insertNewlinesRec(text[1:], wraped, lineLength, cLength + 1)
                else:
                    return insertNewlinesRec(text[1:], wraped + text[0], lineLength, cLength + 1)
    wraped = insertNewlinesRec(text, '', lineLength, 0)
    return wraped
    
            
                
            
            
