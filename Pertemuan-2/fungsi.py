def greeting(hour = 7):
    if hour < 12 :
        return "Selamat Pagi !!"
    elif hour < 18 :
        return "Selamat Sore !!"
    else :
        return "Selamat Malam !!"

print(greeting(7))
print(greeting(13))
print(greeting(20))
print(greeting())