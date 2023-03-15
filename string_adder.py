def canComplete(string_inp,org_string):
    original_str = list(org_string)
    answer = True
    org_dict = {}
    for i in org_string:
        if i in org_dict:
            org_dict[i] += 1
        else:
            org_dict[i] = 1
    # print(org_dict)
    
    new_list = {}
    for i in range(0,len(string_inp)):
        if i in new_list:
            new_list[string_inp[i]]+=1
        else:
            new_list[string_inp[i]] = 1
    # print(new_list)

    if len(string_inp) <= len(org_string):
        for i in range(0,len(string_inp)):
            if string_inp[i] in original_str:
                if i <= original_str.index(string_inp[i]) :
                    answer = True
                    
                else:
                    answer = False
                    
                    return answer
            else:
                answer = False
                
                return answer

        for i in range(0,len(string_inp)):
            if new_list[string_inp[i]] <= org_dict[string_inp[i]]:
                answer = True
                       
            else:
                answer = False
                return answer
    else:
        answer = False
        return answer
    
    return answer

str_inp = str(input())
org_str = str(input())

print(canComplete(str_inp,org_str))