class Stack():                      #Stack 클래스 생성
    def __init__(self):             #클래스 초기화
        self.stack = []
    
    def push(self, data):           #스택에 데이터 추가
        self.stack.append(data)     
    
    def pop(self):                  #스택에서 데이터 반환
        popObject = None
        if self.isEmpty():         #스택이 비어있으면 False, 있으면 반환
            return False
        else:
            popObject = self.stack.pop()
        
        return popObject
    
    def top(self):                  #스택의 가장 위에 있는 데이터 반환
        topObject = None
        if self.isEmpty():          #스택 최상단이 비어있으면 False, 있으면 반환
            return False
        else:
            topObject = self.stack[-1]
        
        return topObject 
    
    def isEmpty(self):              #스택이 비어있으면 True, 채워져있으면 False
        isEmpty = False
        if len(self.stack) == 0:
            isEmpty = True
        
        return isEmpty
    #reverses 함수 추가를 위해 추가함
    def reverses(self):
        self.stack.reverse()

def calculator(lst):
    lst.reverses()  # 입력받은 스택은 pop으로 꺼낼 시 역순으로 계산되므로 정방향 계산을 위해 reverse()함수사용

    formula = ""  # eval함수 사용을 위해 string값으로 선언

    while lst.isEmpty() == 0:
        formula = formula + str(lst.pop())

    return eval(formula)