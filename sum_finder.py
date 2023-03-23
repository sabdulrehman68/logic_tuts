class Elements:
    def __init__(self,ele_list,target):
        self.ele_list = ele_list
        self.target = target
    
    def find_sum(self,):
        l1 = []
        for i in range(0,len(self.ele_list)):
            for j in range(i,len(self.ele_list)):
                if i != j:
                    sum = self.ele_list[i] + self.ele_list[j]
                    if sum == self.target:
                        tup = (i,j)
                        l1.append(tup)
                    
                else:
                    continue
        
        return l1

if __name__ == '__main__':
    no = int(input("Enter no. of elements in the list:"))
    print("Enter the elements of list:")
    elements = []
    for i in range(0,no):
        ele = int(input())
        elements.append(ele)
    targ = int(input("Enter target value:"))
    new_obj = Elements(elements,targ)
    
    sum_list = new_obj.find_sum()
    if len(sum_list) != 0:
        for x in range(len(sum_list)):
            print(sum_list[x],)
    else:
        print(None)