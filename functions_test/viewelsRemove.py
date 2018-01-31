



def remove_vow(text):
    vow=["a","e","o","u","i","A","O","I","E","U"]
    res=""
    for i in text:
        if i not in vow:
            res+=i
    print(res)

  




remove_vow("mobile")

if __name__ == '__main__':
    pass