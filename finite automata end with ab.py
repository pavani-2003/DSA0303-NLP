
def ends_with_ab(input_string):
    return input_string.endswith("ab")

# Test the function
input_string1 = "ab"
input_string2 = "aabb"
input_string3 = "aab"
input_string4 = "ba"
input_string5 = "abab"

print(f'"{input_string1}" ends with "ab": {ends_with_ab(input_string1)}')
print(f'"{input_string2}" ends with "ab": {ends_with_ab(input_string2)}')
print(f'"{input_string3}" ends with "ab": {ends_with_ab(input_string3)}')
print(f'"{input_string4}" ends with "ab": {ends_with_ab(input_string4)}')
print(f'"{input_string5}" ends with "ab": {ends_with_ab(input_string5)}')

