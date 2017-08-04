def pattern():
    test = int(input())
    while(test):
        count = 0
        l = int(input())
        dic = input().split(" ")
        pat = input()
        flag = 0
        listallcaps = []
        allcaps = []
        initials = {}
        for word in dic:
            for w in word:
                if(w.isupper()):
                    allcaps.append(w)
            newword = ''.join(allcaps)
            listallcaps.append(newword)
            initials[word] = newword
            allcaps[:] = []
        for key, value in initials.items():
            if value == pat:
                print(key)
                count += 1
                flag = 1
        if flag == 0:
            print("No match found")
        test -= 1
pattern()
