import re
class Solution:
    def validIPAddress(self, IP: str) -> str:
        ip=list(IP)
        if '.' in ip:
            lis=IP.split('.')
        elif ':' in ip:
            lis=IP.split(':')
        else:
            return 'Neither'
        print(lis)
        if len(lis)==4:
            for i in lis:
                if i=='' or (i[0]=='0' and len(i)>1):
                    return 'Neither'
                if not i.isnumeric():
                    return 'Neither'
                elif i.isnumeric() and int(i)>255:
                    return 'Neither'
            return 'IPv4'
        elif len(lis)==8:
            pattern=r"\b[0-9a-fA-F]{1,4}\b"
            for i in lis:
                if i=='':
                    return 'Neither'
                a=re.match(pattern,i)
                if a and len(i)<=4:
                    pass
                else:
                    return 'Neither'
            return 'IPv6'   
        else:
            return 'Neither'