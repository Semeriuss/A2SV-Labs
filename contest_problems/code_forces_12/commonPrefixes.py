def commonPrefixes(relations):
    
    ret = []
    ptr = ord('a')
    for i, relation in enumerate(relations):
        # print("index before  ", i, "  ", ret)
        if ptr == ord('z') + 1:
            ptr = ord('a')
        if relation == 0 and i == 0:
            ret.append([chr(ptr)])
            ptr += 1
            ret.append([chr(ptr)])
            ptr += 1
        
        elif relation == 0:
            ret.append([chr(ptr)])
            ptr += 1

        elif i == 0: #not ret:
            new_str1 = []
            new_ptr = ord('a')
            for i in range(relation):
                new_ptr = ord('a')if new_ptr > ord('z') else new_ptr 
                new_str1.append(chr(new_ptr))
                new_ptr += 1
            ret.append(new_str1)
            new_str2 = []
            new_ptr = ord('a')
            for i in range(relation):
                new_ptr = ord('a') if new_ptr > ord('z') else new_ptr
                new_str2.append(chr(new_ptr))
                new_ptr += 1
            # ptr += relation
            ret.append(new_str2)
            # print(ret)
            ptr = ord(ret[-1][-1]) + 1
        
        else:
            if len(ret[-1]) >= relation:
                new_str = []
                new_ptr = ord(ret[-1][0])
                for i in range(relation):
                    new_ptr = ord('a') if new_ptr > ord('z') else new_ptr
                    new_str.append(chr(new_ptr))
                    new_ptr += 1
                ret.append(new_str)
                ptr = ord(ret[-1][-1]) + 1

            else:
                new_str = []
                new_ptr = ptr
                for i in range(relation - relations[i - 1]):
                    new_ptr = ord('a') if new_ptr > ord('z') else new_ptr
                    new_str.append(chr(new_ptr))
                    new_ptr += 1
                ret[-1].extend(new_str)
                ptr = ord(ret[-1][-1]) + 1

                new_str = []
                new_ptr = ord(ret[-1][0])
                for i in range(relation):
                    new_ptr = ord('a') if new_ptr > ord('z') else new_ptr
                    new_str.append(chr(new_ptr))
                    new_ptr += 1
                ret.append(new_str)
                ptr = ord(ret[-1][-1]) + 1
        # print("index   ", i, "  ", ret)
    
    for i, s in enumerate(ret):
        ret[i] = "".join(s)

    return ret

if __name__  == "__main__":
    t = int(input())
    result = []
    for _ in range(t):
        n = map(int, input())
        relations = list(map(int, input().split()))
        # print(relations)
        result.append(commonPrefixes(relations))
    
    for res in result:
        print(*res, sep="\n")
        