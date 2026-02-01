#!/usr/bin/python3

import re

def calc(A,B):
        ai=str(A)
        bi=str(B)
        #修正1：整数のみにマッチする正規表現に変更
        p = re.compile('^\d+$')
        
        #修正2：AとBの両方が整数の文字列かつint型であることを確認
        if p.match(ai) and p.match(bi) and isinstance(A, int) and isinstance(B, int):
                a=int(ai)
                b=int(bi)
                #修正3：境界値（1と999）を含み、AとBの大小関係を問わない条件に変更
                if 1 <= a <= 999 and 1 <= b <= 999:
                        valid=True
                else:
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                return ans
        else:
                return -1
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
