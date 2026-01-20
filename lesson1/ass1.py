# Before Refactoring

result = abs(3.0 * (4.0 / 3.0 - 1) - 1)

print("Mathematical Expected Result: 0")
print("Actual Computer Result: " + str(result))

if result == 0:
    print("result == 0.")
else:
    print("The result is NOT 0 need Refactoring")
