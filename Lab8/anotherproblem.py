#Sample input 1
# 10 12
# 71293781758123 72784
# 1 12345677654321

# Sample input 2
# 2
# 71293781685339
# 12345677654320



sträng = """10 12
71293781758123 72784
1 12345677654321"""


numbers = sträng.split("\n")
string = 0
for number in numbers:
    num = number.split()
    string = abs(int(num[1]) - int(num[0]))
    print(type(string))

