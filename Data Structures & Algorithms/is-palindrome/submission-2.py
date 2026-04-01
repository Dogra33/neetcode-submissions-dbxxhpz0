import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        string = re.sub(r'[^a-z0-9]', '', s)
        length = len(string)
        if length == 0:
            return True
        print(string)
        mid =  int((length)/2)
        print("Mid point = ", string[mid])
        left, right =0,0
        if length%2 == 0:
            print("Even")
            left = mid -1
            right = mid

        else:
            print("Odd")
            left = mid-1
            right = mid+1
        
        while left >= 0 and right < length:
                print('Left = ', string[left])
                print('Right = ', string[right])
                if string[left] == string[right]:
                    if left == 0 and right < length-1:
                        return True
                    else:
                        left -=1
                        right +=1
                else:
                    return False
        return True