txt = "The rain in spain!"
x = re.findall(r"\Bain",txt)
print(x)
if x:
    print("Yes it match!")
else:
    print("NO MATCH")
