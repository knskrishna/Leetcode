'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

'''
class Solution(object):
    def isValid(self, s):
        if len(s)%2!=0 or len(s)==0:
            return False
        stack=[]
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stack.append(i)
            if len(stack)>0:
                if i==")" and stack[-1]=="(":
                    stack.pop()
                elif i=="]" and stack[-1]=="[":
                    stack.pop()
                elif i=="}" and stack[-1]=="{":
                    stack.pop()
                elif i==")" or i=="]" or i=="}":
                    return False
            else:
                if i==")" or i=="]" or i=="}":
                    return False
        if len(stack)==0:
            return True
        else:
            return False