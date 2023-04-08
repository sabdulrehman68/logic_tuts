def remove_ly(string_inp):
    str_list = string_inp.split(' ')
    for i in range(len(str_list)):
        word = str_list[i]
        if word.endswith("ly"):
            str_list[i] = word[:-2]
            
    str_out = " ".join(map(str,str_list))
    return str_out

string = remove_ly("The patient simply waited patiently in the clinic")
print(string)