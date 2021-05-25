from config_app import *
##################################
system("clear")
Write_Text_Animation(CopyRight)
##################################
print("""
to Short The URL [1]
S75XD Twitter [2]
F14Commander Twitter [3]
To EXIT [4]
""")
while True:
    Text = input(":")
    if Text == 1:
        Link = input("URL:")
        s = pyshorteners.Shortener()
        print(s.tinyurl.short(Link))
    elif Text == 2:
        webbrowser.open("https://twitter.com/S75XD")
    elif Text == 3:
        webbrowser.open("https://twitter.com/F14Commander")
    elif Text == 4:
        exit("Ok")
    else:
        print("Error")