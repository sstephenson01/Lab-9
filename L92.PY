#Breanna Eafon and Sarah Stephenson
def remove_substring(mainstring, substring):
    output=[]
    index=0
    while index < len(mainstring):
        if mainstring[index:index+len(substring)]== substring:
            index+=len(substring)
        else:
            output.append(mainstring[index])
            index+=1
    print("".join(output))
remove_substring("YELL!HelloYELL! WorldYELL!", "YELL!")
