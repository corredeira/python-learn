nova = ["casa", "nova", "hello"]
x , y , z = nova
print(x)
print(y)
print(z)

w = 1
a = "nova"

print(w,a)



def funcNew():
    global b
    b = "oldfunction"
    

funcNew()
print("now " + b)