class ListDivideException(Exception):
    pass

def listDivide(numbers, divide=2):
    return len([i for i in numbers if i%divide==0])

def testListDivide():
    result = [0]*5
    result[0] = listDivide([1,2,3,4,5])
    result[1] = listDivide([2,4,6,8,10]) 
    result[2] = listDivide([30, 54, 63,98, 100], divide=10)
    result[3] = listDivide([])
    result[4] = listDivide([1,2,3,4,5], 1)
    
    if result != [2,5,2,0,5]:
        raise ListDivideException("Wrong Ouput")

if __name__=="__main__":
    testListDivide()
    
