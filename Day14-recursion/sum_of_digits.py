num =123456
def sum_digits(num):
    if num == 0:
        return 0
    return num%10 + sum_digits(num//10)
sum1 = sum_digits(num)
# print(sum1)

def power_of_num(num, power):
    if power == 0:
        return 1
    return num*power_of_num(num, power-1)

# print(power_of_num(2,4))

def decimal_to_binary(num):
    if num == 0 or num<1:
        return 0
    return num%2 + 10*decimal_to_binary(int(num/2))

# print(decimal_to_binary(4))

def factorial(num):
    if num == 0:
        return 1
    return num*factorial(num-1)
# print(factorial(5))

def productofarray(arr):
    if arr == []:
        return 1
    return arr.pop()*productofarray(arr)
# print(productofarray([1,2,3,4,5]))

def recursive_range(num):
    if num == 0:
        return 0
    
    return num + recursive_range(num-1)
# print(recursive_range(10))

def fib(num):
    if num < 2:
        return num
    return fib(num-1) + fib(num-2)
# print(fib(4))

def reverse(str1):
    if str1 == "":
        return ""
    return str1[-1] + reverse(str1[:-1])
# print(reverse("Suyash"))

def ispalindrome(name):
    if len(name) == 0:
        return True
    if name[0] != name[len(name)-1]:
        return False
    return ispalindrome(name[1:-1])
# print(ispalindrome("tacocat"))

# def someRecursive(arr, callback):
#     if arr == []:
#         return False
#     if not arr.pop().callback:
#         return False
#     return someRecursive(arr, callback)
# arr = [2,4,5,6,8]   
# print(someRecursive(arr, isodd()))

def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True
 
def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
# print(someRecursive([2,4,6,7,8], isOdd()))

def flatten(arr):
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else: 
            resultArr.append(custItem)
    return resultArr 
# print(flatten([1,2,3,[4,5],[7,[8,[9,0]]]]))

def capitalize(list_of_stings):
    result_arr = []
    if len(list_of_stings) == 0:
        return result_arr   
    result_arr.append(list_of_stings[0].capitalize())
    return result_arr +  capitalize(list_of_stings[1:])
# print(capitalize(['car', 'taco', 'banana']))

def nestedEvenSum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key]%2==0:
            sum+=obj[key]
    return sum
# print(nestedEvenSum({"outer": 2,"obj": {"inner": 2,"otherObj": {"superInner": 2,"notANumber": True,"alsoNotANumber": "yup"}}}))

def capitalizeWords(words):
    resultArr = []
    if len(words) == 0:
        return resultArr
    resultArr.append(words[0].upper())
    return resultArr + capitalizeWords(words[1:])
# print(capitalizeWords(['i', 'am', 'learning', 'recursion']))

def collectStrings(obj):
    resultArr = []
    for key in obj:
        if type(obj[key]) is str:
            resultArr.append(obj[key])
        if type(obj[key]) is dict:
            resultArr = resultArr + collectStrings(obj[key])
    return resultArr
print(collectStrings({
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}))