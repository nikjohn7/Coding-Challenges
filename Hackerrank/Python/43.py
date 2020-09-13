from collections import Counter

# Complete the anagram function below.
def anagram(s):
    if len(s)%2==1:
        return -1
    s1=dict(Counter(s[:len(s)//2]))
    s2=dict(Counter(s[len(s)//2:]))
    c2=0
    
    for i in s2:
        t=s2[i]-(s1.get(i,0))
        if t>0:
            c2+=t
    return c2

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        print(str(result))