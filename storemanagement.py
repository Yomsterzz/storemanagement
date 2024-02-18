textbooks = {

  "math": 13,
  "science": 11,
  "history": 32,
  "english": 12,
  "french": 8,
  "chemistry": 18,
  "physics": 21
  
}

textbooks["physics"] = 20

print(textbooks)

textbooks["spanish"] = 9
textbooks["biology"] = 20

print(textbooks)

inpbook = input("Name a book you want the price of: ")

if inpbook in textbooks:
  print(textbooks[inpbook])
else:
  print("Book does not exist.")

print(textbooks)