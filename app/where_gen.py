# function for generating where clause

def whereGenerator(input : str):
    arguments = input.split('|')
    non_ints = ["CCA3", "continent", "name", "discipline_name", "event"]
    dict = {}
    for argument in arguments:
        argument_split = argument.split(':')
        if argument_split[0] in non_ints:
            argument_split[1] = '"' + argument_split[1] + '"'
        if argument_split[0] not in dict:
            dict[argument_split[0]] = []
        dict[argument_split[0]].append(argument_split[1])

    output = "WHERE "

    check0 = 0
    for key in dict.keys():
        if check0:
            output = output + " AND "
        else: check0 = 1
        
        check1 = 0
        temp = "("
        for item in dict[key]:
            if check1:
                temp = temp + " OR "
            else: check1 = 1
            temp = temp + f"{key} = {item}"

        temp = temp + ")"
        output = output + temp

    return output

def setGenerator(input : str):
    arguments = input.split('|')
    non_ints = ["CCA3", "continent", "name", "discipline_name", "event"]
    dict = {}
    for argument in arguments:
        argument_split = argument.split(':')
        if argument_split[0] in non_ints:
            argument_split[1] = '"' + argument_split[1] + '"'
        if argument_split[0] not in dict:
            dict[argument_split[0]] = []
        dict[argument_split[0]].append(argument_split[1])

    output = "SET "

    check0 = 0
    for key in dict.keys():
        if check0:
            output = output + " , "
        else: check0 = 1
        
        output = output + f"{key} = {dict[key][0]}"

    return output


def insertGenerator(input, table):
    dic = []
    if table == 0:
        dic = [1,1,1]
    elif table == 1:
        dic = [1,1,1,1]
    else:
        dic = [1,0,1,0,0,0,0,0,0,0]
    output = ""
    args = input.split(',')
    check = 0
    for i in range(len(args)):
        if check:
            output = output + ","
        check = 1
        arg = args[i]
        if dic[i]:
            arg = "'"+arg+"'"
        output = output + arg
    return output


if __name__ == "__main__":
    string = "a,b,c,d,e,f,g,h,i,j"
    print(string)
    print(insertGenerator(string,2))
