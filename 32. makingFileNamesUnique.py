from collections import defaultdict

def addBracketIndex(name, index):
    return name + f'({index})'

def changeBracketIndex(name, index):
    index = index if name.find(f'{index}') != -1 else index - 1
    return name.replace(f'({index})', f'({index + 1})')    

def changeNameIndex(name, index):
    if name.endswith(')'):
        return changeBracketIndex(name, index)
    else:
        return addBracketIndex(name, index)

def getFolderNames(names):
    """
    :type names: List[str]
    :rtype: List[str]
    """

    hashset = set()
    k = [1 for i in range(len(names))]
    
    for i in range(len(names)):
        if names[i] in hashset and not names[i].endswith(')'):
            while names[i] in hashset:
                names[i] = changeNameIndex(names[i], k[i])
                k[i] += 1
        else:
            if k[i] == 1:
                while names[i] in hashset:
                    names[i] = addBracketIndex(names[i], k[i])
                    k[i] += 1
            else:
                while names[i] in hashset:
                    names[i] = changeBracketIndex(names[i], k[i])
                    k[i] += 1
        hashset.add(names[i])                    

    return names

def getFolderNames(names):
    """
    :type names: List[str]
    :rtype: List[str]
    """

    hashmap = {}
    for i in range(len(names)):
        changed = names[i]
        if names[i] in hashmap:
            k = hashmap[names[i]]
            while changed in hashmap:
                k += 1
                changed = f'{names[i]}({k})'
            hashmap[changed] = k
        hashmap[changed] = 0                   

    return list(hashmap.keys())

def getFolderNames(names):
        hashmap = defaultdict(int)
        for i in range(len(names)):
            changed = names[i]
            if names[i] in hashmap:
                k = hashmap[names[i]]
                while changed in hashmap:
                    k += 1
                    changed = f'{names[i]}({k})'
                hashmap[changed] = k
            hashmap[changed] = 0  

        return list(hashmap.keys())

def getFolderNames(names):
        hashmap = defaultdict(int)
        ans = []
        for i in range(len(names)):
            if hashmap[names[i]] > 0:
                while f'{names[i]}({hashmap[names[i]]})' in hashmap.keys():
                    hashmap[names[i]] += 1
                ans.append(f'{names[i]}({hashmap[names[i]]})')
                hashmap[f'{names[i]}({hashmap[names[i]]})'] += 1
            else:
                ans.append(names[i])
            hashmap[names[i]] += 1  

        return ans

def getFolderNames(names):
        hashmap = defaultdict(int)
        for i in range(len(names)):
            if hashmap[names[i]] > 0:
                while f'{names[i]}({hashmap[names[i]]})' in hashmap.keys():
                    hashmap[names[i]] += 1
                names[i] = f'{names[i]}({hashmap[names[i]]})'
                hashmap[f'{names[i]}({hashmap[names[i]]})'] += 1
            else:
                names[i] = names[i]
            hashmap[names[i]] += 1  

        return names
    
tests = [(["wano","wano","wano","wano"], ["wano","wano(1)","wano(2)","wano(3)"]),
         (["pes","fifa","gta","pes(2019)"], ["pes","fifa","gta","pes(2019)"]),
         (["gta","gta(1)","gta","avalon"], ["gta","gta(1)","gta(2)","avalon"]),
         (["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"],
          ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]),
         (["kaido","kaido(1)","kaido","kaido(1)"],
          ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]),
         (["t","l(1)(3)","o","i(3)(1)","j(1)","g","z","z","q(3)(2)","u(1)(3)","x","m","l(4)(2)","o","h","s","e","c","v"],
          ["t","l(1)(3)","o","i(3)(1)","j(1)","g","z","z(1)","q(3)(2)","u(1)(3)","x","m","l(4)(2)","o(1)","h","s","e","c","v"]),
         (["d(2)(4)","n","y","q(3)","q(3)","p(2)","o","k(4)","x(1)","m(1)","a(2)","z","p(2)(3)","d","g","t","n","z(3)","a","d(2)","b","t","m","r(1)(2)","k","c","p(2)(1)","c","l(1)","l","b","u","o","h(2)","p(3)(3)","d","o","c","c","v","a","g","j","m","g(4)","h","b(2)","r(3)","e","b(1)","f(4)","i","m","r","m","w(3)(4)","p","a","g","b","s","r","b(1)","f","k","q","p"],
          ["d(2)(4)","n","y","q(3)","q(3)(1)","p(2)","o","k(4)","x(1)","m(1)","a(2)","z","p(2)(3)","d","g","t","n(1)","z(3)","a","d(2)","b","t(1)","m","r(1)(2)","k","c","p(2)(1)","c(1)","l(1)","l","b(1)","u","o(1)","h(2)","p(3)(3)","d(1)","o(2)","c(2)","c(3)","v","a(1)","g(1)","j","m(2)","g(4)","h","b(2)","r(3)","e","b(1)(1)","f(4)","i","m(3)","r","m(4)","w(3)(4)","p","a(3)","g(2)","b(3)","s","r(1)","b(1)(2)","f","k(1)","q","p(1)"])]

for test in tests:
    names, expected = test
    actual = getFolderNames(names)
    print(actual == expected, actual, expected)
    
