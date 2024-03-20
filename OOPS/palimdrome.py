def pali(s):
    s.lower()
    new_string=s[::-1] #reverse string
    if new_string==s:
        print("string is palimdrome")
    
    else:
        print("string is not palimdorme")


pali("level")


