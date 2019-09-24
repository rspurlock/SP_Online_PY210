#second set of warmup exercises

#string_times
def string_times(str, n):
    return str*n

print(string_times('Hi',2))
print(string_times('Hi',3))
print(string_times('Hi',1))
print('-' * 25)

#front_times
def front_times(str, n):
    return str[:3] * n

print(front_times('Chocolate', 2))
print(front_times('Chocolate', 3))
print(front_times('Abc', 3))
print('-' * 25)

#string_bits
def string_bits(str):
    return str[::2]

print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))
print('-'*25)

#string_splosion
def string_splosion(str):
    result = ''
    for i in range(len(str)):
        chars = str[:i]
        result += chars
    return result + str

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))
print('-' * 25)

#last2
def last2(str):
    last2 = str[-2:]
    
    count = 0
    for i in range(len(str)-2):
        sub = str[i:i+2]
        #print(sub)
        if sub == last2:
            #print(sub)
            count += 1
           
    return count


print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))
print('-' * 25)

#array_count9
def array_count9(nums):
    return nums.count(9)

assert array_count9([1, 2, 9]) == 1
assert array_count9([1, 9, 9]) == 2
assert array_count9([1, 9, 9, 3, 9]) == 3
print("array_count9 tests passed")

#array_front9
def array_front9(nums):
    return 9 in nums[:4]

assert array_front9([1, 2, 9, 3, 4]) == True
assert array_front9([1, 2, 3, 4, 9]) == False
assert array_front9([1, 2, 3, 4, 5]) == False
assert array_front9([1,2,3]) == False
print("array_front9 tests passed")

