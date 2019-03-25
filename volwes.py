try:
    ch=input()
    v=['a','e','i','o','u','A','E','I','O','U']
    co=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','w','x','y','z','Z','Y','X','W','T','S','R','Q','P','N','M','L','K','J','H','G','F','D','C','B']
    if ch in v:
        print("Vowel")
    elif ch in co:
        print("Consonant")
    else:
        print("invalid")
except:
    print("inalid")
