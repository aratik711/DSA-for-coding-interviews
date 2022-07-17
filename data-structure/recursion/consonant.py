vowels = "aeiou"

def iterative_count_consonants(str):
    count = 0
    for i in range(len(str)):
        if str[i].lower() not in vowels and str[i].isalpha():
            count += 1
    return count

def recursive_count_consonants(str):
    if str == "":
        return 0
    if str[0].lower() not in vowels and str[0].isalpha():
        return 1 + recursive_count_consonants(str[1:])
    else:
        return recursive_count_consonants(str[1:])

input_str = "abc de"
print(input_str)
print(iterative_count_consonants(input_str))
input_str = "LuCiDPrograMMiNG"
print(input_str)
print(recursive_count_consonants(input_str))
