def remove_ly(string_inp):
    str_list = string_inp.split(' ')
    for i in range(len(str_list)):
        word = str_list[i]
        if word.endswith("ly"):
            str_list[i] = word[:-2]      
    str_out = " ".join(map(str,str_list))
    return str_out

string_i = str(input())
string = remove_ly(string_i)
print(string)