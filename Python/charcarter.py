import re
txt = "The rain in spain!"
#x = re.findall("\ATHE",txt)
#x = re.findall(r"ain\b",txt)
#x = re.findall("\d",txt)
#x = re.findall("\D",txt)
#x = re.findall("\s",txt)
#x = re.findall("\w", txt)
#x = re.findall("\W", txt)
x = re.findall("Spain\Z", txt)

print(x)
if x:
    print("Yes,at least one match!")
else:
    print("NO MATCH")

pattern = r"[a-zA-Z]+ \d+"
matches = re.findall(pattern, "LXI 2013, VXI 2015, VDI 2014, MARUTI SUZUKI CARS I N INDIA")
for match in matches:
    print(match, end=" ")

import re
string = "she sells sea shell on the sea shore"
pattern = "sea"
repl = "ocean"
new_string = re.sub(pattern, repl, string, 2)
print(new_string)

var = "Good"
def show():
    global var1
    var1 = "Morning"
    print("The function var is: ", var)
show()
print("Outside funciton var is: ", var1)
print("Var is: ", var)

