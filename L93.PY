#Breanna Eafon and Sarah Stephenson
def replace_substring(mainstring, substring,replacement):
    output=[]
    index=0
    while index < len(mainstring):
        if mainstring[index:index+len(substring)]== substring:
            index+=len(substring)
            output.append(replacement)
        else:
            output.append(mainstring[index])
            index+=1
    print("".join(output))
replace_substring("YELL!HelloYELL! WorldYELL!", "YELL!", "2S")
