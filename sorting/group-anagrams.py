"""

Given a list of strings that contains anagrams, write a function to print pairs of those anagrams.

Input#
A list of strings. Remember that spaces count as characters. So, " abc" and “cab” are technically not anagrams, since " abc" has spaces which “cab” does not.

Output#
A list of lists where all pairs of anagrams grouped together

Sample input#
input = [
    'tom marvolo riddle ',
    'abc',
    'def',
    'cab',
    'fed',
    'brag',
    'clint eastwood ',
    'i am lord voldemort',
    'elvis',
    'grab',
    'old west action',
    'lives'
  ]
Sample output#
result = [['abc', 'cab'], ['clint eastwood ', 'old west action'], ['def', 'fed'], ['elvis', 'lives']]

Sorting one word takes O(klogk)
 time in the average case using quick sort (where k
 is the length of the longest word in the given list), so, sorting n
 words would take O(n*klogk)
. The rest of the operations use hashing which is all in constant time and therefore, doesn’t count.


"""
def anagrams(lst):
    dictionary = {}
    for string in lst:
        key = ''.join(sorted(string))
        if key in dictionary.keys():
            dictionary[key].append(string)
        else:
            dictionary[key] = []
            dictionary[key].append(string)
    result = []
    for key, value in dictionary.items():
        if len(value) >= 2:
            result.append(value)
    return result

# Driver to test above code
if __name__ == '__main__':

    lst = ['tom marvolo riddle ', 'abc', 'def', 'cab', 'fed', 'clint eastwood ', 'i am lord voldemort', 'elvis', 'old west action', 'lives']
    print (anagrams(lst))
