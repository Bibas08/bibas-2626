
L1 = [1, 8, 7, 2, 21, 15]
L1.remove(8)
print(L1)
#wap to store 7 fiuits in a list entered by the user 
fruits = []
for i in range(7):
    fruit = input("Enter fruit {}: "(i + 1))
    fruits.append(fruit)
print("Fruits list:", fruits)


#wap to accept marks of 6 students and diplay them in sorted order
marks = []
for i in range(6):
    mark = int(input("Enter marks for student {}: "(i + 1)))
    marks.append(mark)
marks.sort()
print("Sorted marks:", marks)

#Wap to sum a list with 4 numbers.
numbers = []
for i in range(4):
    number = int(input("Enter number {}: ".format(i + 1)))
    numbers.append(number)
print("Sum of numbers:", sum(numbers))



