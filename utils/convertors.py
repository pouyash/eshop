def convert_to_group(lst,size=4):
    output = []
    for i in range(0,len(lst),size):
        output.append(lst[i:i+size])
    return output