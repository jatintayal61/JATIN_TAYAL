def calculate(s: str) -> int:
    s = s.replace(" ", "")
    first = last = res = 0
    first_operation = "+"
    i = 0
    
    if s[0] == '-':
        s = '0' + s
    
    while i < len(s):
        first_char = s[i]
        if first_char.isdigit():
            while i < len(s) and s[i].isdigit():
                first = first * 10 + int(s[i])
                i += 1
            i -= 1
            if first_operation == "+":
                res += first
                last = first
            elif first_operation == "-":
                res -= first
                last = -first
            elif first_operation == "*":
                res -= last
                res += last * first
                last = last * first
            elif first_operation == "/":
                res -= last
                res += int(last/ first)
                prev = int(last / first)
            cur = 0
        elif first_char in "+-*/":
            first_operation = first_char
        i += 1
    return res

a = input("enter user_input: ")
print(calculate(a))