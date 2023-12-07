conv = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero"
}
num = [1,2,3,4,5,6,7,8,9,0]
test_str ="Bewin 1 2"


for ele in test_str:
    if ele.isdigit():
        test_str = test_str.replace(ele, conv[ele])
print(test_str)
        