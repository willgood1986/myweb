# -*- coding: utf-8 -*-
def findtarget(source, target):
    ''' to find two nums which the sum result is equal to target
    '''
    left, right = 0, len(source) - 1
    sortedlst = sorted(source)
    for i in range(len(sortedlst)//2):
        if left == right:
            print('This should not happend')
            break
        if (sortedlst[left] + sortedlst[right]) > target:
            right = right - 1
        elif (sortedlst[left] + sortedlst[right]) < target:
            left = left + 1
        else:
            return sortedlst[left], sortedlst[right]


if __name__ == '__main__':
    lst = list(range(10))
    results = findtarget(lst, 7)
    if (results):
        print("left is {left}, right is {right}".format(left=results[0],right=results[1]))

            
            
