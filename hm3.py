def check_brackets(expression):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return f"Несиметрично: знайдено '{char}', але немає відповідної відкриваючої дужки"
            top = stack[-1]
            if top == brackets[char]:
                stack.pop()
            else:
                return f"Несиметрично: знайдено '{char}', але остання відкрита дужка — '{top}'"

    if stack:
        return "Несиметрично: не всі дужки закриті"
    return "Симетрично"


examples = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",  #Симетрично
    "( 23 ( 2 - 3);",            #Несиметрично
    "( 11 }",                    #Несиметрично
    "((()))",                    #Симетрично
    "{[(])}",                    #Несиметрично
    "[({})]",                    #Симетрично
]

for expr in examples:
    result = check_brackets(expr)
    print(f"{expr}: {result}")


