codes = {'A':'!','B':'@','C':'#','D':'$','E':'%','F':'^','G':'&','H':'*','I':'(','J':')','K':'-','L':'_','M':'+','N':'=','O':'`','P':'~','Q':'{','R':'[','S':'}','T':']','U':':','V':';','W':'"','X':'<','Y':'>','Z':'0','a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'a','k':'b','l':'c','m':'d','n':'e','o':'f','p':'g','q':'h','r':'i','s':'j','t':'k','u':'l','v':'m','w':'n','x':'o','y':'p','z':'q'}

afile = open("info_security-1.txt", "r")
readfile = afile.read()
afile.close()

efile = open("encrypted.txt", "w")

for character in readfile:
    if character in codes:
        efile.write(codes[character])
    else:
        efile.write(character)

efile.close()
efile = open("info_security-1.txt", "r")
fileread = efile.read()
efile.close()
items = codes.items()

for character in fileread:
    if character not in codes.values() or character == "." or character == "," or character == "!":
        print(character)
    else:
        for x,y in items:
            if character == y and character != ".":
                print(x, end= "")
