
def numbers():
  number1 = int(input("Enter starting number: "))
  number2 = int(input("Enter ending number: "))
  numbers()
  if number2 < number1:
    print("Error: ending number must be greater than starting number")
    numbers()
number1 = int(input("Enter starting number: "))
number2 = int(input("Enter ending number: "))
answer = 0
bro = number1
while bro <= number2:
  answer += bro
  bro += 1
amount = number2-number1
result = answer/amount
print(result)
print("Helo word")
print("song.mp4")