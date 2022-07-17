def isVowel(character):
    vowels = "aeiou"
    if character.lower() in vowels:
        return 1
    else:
        return 0

def countVowels(string, n):
    if n == 1:
        return isVowel(string[0])
    return countVowels(string, n-1) + isVowel(string[n-1])

# Driver code
string = "Educative"
print(countVowels(string, len(string)))
