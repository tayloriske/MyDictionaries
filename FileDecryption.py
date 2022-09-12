decode = {'!':'A','@':'B','#':'C','$':'D','%':'E','^':'F','&':'G','*':'H','(':'I',')':'J','-':'K','_':'L','+':'M','=':'N','`':'O','~':'P','{':'Q','[':'R','}':'S',']':'T',':':'U',';':'V','"':'W','<':'X','>':'Y','0':'Z','1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','a':'j','b':'k','c':'l','d':'m','e':'n','f':'o','g':'p','h':'q','i':'r','j':'s','k':'t','l':'u','m':'v','n':'w','o':'x','p':'y','q':'z'}

afile = open("encrypted.txt", "r")
fileread = afile.read()
afile.close()

items= decode.items()

for character in fileread:
    if character not in decode.values() or character == "." or character == "," or character == "!":
        print(character)
    else:
        for x,y in items:
            if character == y and character != ".":
                print(x, end="")
