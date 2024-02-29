"""m = ['a', [], 'b', ['cc', 'dd'], 'e']  # Change the empty string to an empty list
m[1].extend([1,2,3])  # Now extend can be applied to m[1]
#del m[2]
for list in m:
    for number in list:
        print(number, end="")
print(m)
m = list
print("list1 = ", m)
print("list2 = ", list)
print(len(m))
print(len(m[2]))"""
stack = [0,1,2,3,4,5,6]
print("Orignal: ", stack)
stack.append(7)
print("Stack after push: ", stack)
stack.pop()
print("Stacka fter pop(): ", stack)
last_element = len(stack) - 1
print("Value after peep: ", stack[last_element])
