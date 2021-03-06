import re

if __name__ == '__main__':
    text = "test" #get text from the user
    t = open('questionGenerators/input.txt', 'w')
    t.write(text)
    t.close()
    f = open('questionGenerators/input.txt', 'r')
    contents = f.readlines()
    f.close()
    new = ''
    i = 0
    for line in contents:
        blank = False
        lastchar=" "
        if (i < len(contents)-1):
            for num in range(len(line)-1, -1, -1):
                lastchar=line[num]
                if lastchar != "\n" and lastchar != " ":
                    break
                    
            if (contents[i+1].strip("\n") == "" and lastchar != "." and lastchar != "!"):
                blank = True
                
        if (not blank):
            if (lastchar == "."  or lastchar == "!"):
                new += line
            elif (len(line) > 10):
                new += line                    
        i+=1
    new = new.replace('\n', ' ')
    new = new[:-1];
    new = [e+'.' for e in re.split("!\s|\.\s", new) if e]
    contents = ''
    for n in new:
        if (n[-2] != "?"):
            n = n.strip(" ")
            contents += n + '\n'
    t = open('questionGenerators/input.txt', 'w')
    t.write(contents)
    t.close()