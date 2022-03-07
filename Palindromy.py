def func(name):
    word = ""
    for i in name:
        word = i + word
    return word
def palin(str):
    if str == func(str):
        return True
    return False     
a = "kajak"
print(palin(a))
