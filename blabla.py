def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

def greetUser():
    userInput = input("Enter your name")
    return f"Hello, {userInput}"\

print(greetUser()
      )
