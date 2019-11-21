def list_all_js_function_names(path_to_js_file):
    """
    path_to_js_file is a path to a file on your hard drive
    This function will read the entire input file and then return a list of js function names as strings
    """
    with open(path_to_js_file) as f:
        counter = 0
        names = []
        start = []
        for each_line in f.readlines():
            counter +=1
            if "function" in each_line:
                #print(counter)
                func = each_line.split(" ")
                #print(func)
                start.append(counter)
                if "function" in func[2]:
                    names.append(func[0])
                if func[0] == "function":
                    names.append(func[1].split("()")[0])

        print(start)
        return names

print(list_all_js_function_names("notes.txt"))


