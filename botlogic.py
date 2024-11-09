import random
element = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
contraseña =""
ask =int(input ("de cuantos caracteres va a ser tu contraseña"))
for i in range(ask):
    contraseña += random.choice(element)
print (contraseña)
