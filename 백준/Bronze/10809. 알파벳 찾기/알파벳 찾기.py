text = input()
result= ""
for i in range(26):
    alpha = chr(i+97)
    result += str(text.find(alpha)) + " "
print(result)