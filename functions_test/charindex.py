



def ch_index(text,character):
    list=[]
    for y,char in enumerate(text):
        if char==character:
            list.append(y)
    return list





print(ch_index("hi iti","i"))





if __name__ == '__main__':
    pass 