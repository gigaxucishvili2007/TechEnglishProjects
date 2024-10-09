# # CLASSWORK:
# create a function named swap that will change first and third element in a list. for example----    fruits["apple","orange","grape"] will return   fruits["grape","orange","apple'

# დავწეროთ ფუნქცია სახელად swap, რომელიც ცვლის სიის პირველ და მესამე ელემენტს.
# მაგალითად, თუ გვაქვს სია fruits["ვაშლი", "ფორთოხალი", "ყურძენი"], ფუნქციის გამოძახების შემდეგ მივიღებთ fruits["ყურძენი", "ფორთოხალი", "ვაშლი"].


def swap(arg):
    num = arg[0]
    arg[0] = arg[2]
    arg[2] = num
    return arg
print(swap(['apple' , 'melon' , 'cherry']))

# def swap(arguments): # - argument list = ["ucha"-0,"giga"-1,"mole"-2,"luka"-3,"goa"]
#     string = arguments[0] # ucha
#     arguments[0] = arguments[1] # ["giga","giga"]
#     arguments[1] = string       # ["giga","ucha"]
# print(swap(["ucha","giga"]))
# ["giga","ucha"]

