

def dictionary(list):
    list_names={}
    for i in range(len(list)):
        list_names[list[i][0]]=[list[i]]
    return list_names
 


print(dictionary(["aya","rana","mai"]))