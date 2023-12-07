n = "Bewin Felix a"
lst = n.split(' ')
count = 0

for i in lst:
    if len(i) < 5:
        print(i)
        count +=1

print("total words: ",len(lst))
print("words with length less than 5: ",count)
