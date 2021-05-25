from config_app import *
##################################
system("clear")
Write_Text_Animation(CopyRight)
##################################
URl = input("Enter You Url:")
s = pyshorteners.Shortener()
print(s.tinyurl.short(URl))
##################################
