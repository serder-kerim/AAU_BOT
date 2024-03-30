
def formater(tables):
    global collect_data
    global one_sem_data
    collect_data = []  
    one_sem_data = []
    pointer = 1

    for i in range(1, len(tables)):
        tmp_table = []
        if pointer > int(tables[i][0]):
            collect_data.append(one_sem_data)
            one_sem_data = []
        tmp_table.append(tables[i][0])
        tmp_table.append(tables[i][1])
        tmp_table.append(tables[i][4])
        tmp_table.append(tables[i][5])
        one_sem_data.append(tmp_table)
        pointer = int(tables[i][0])

    collect_data.append(one_sem_data)
    collect_data = collect_data[::-1]
        
def find_semisters(tables):
    count_semister = 0
    for i in range(1,len(tables)):
        index = tables[i][0]
        if index == "1":
            count_semister+=1
    return [str(i) for i in range(1, count_semister + 1)]

def create_table(semester):
    semester =int(semester) - 1
    string = f"""
    _Report Format_
    *No --> Course Title --> ECTS --> Grade*\n"""
    for i in range(len(collect_data[semester])):
        string += f"{collect_data[semester][i][0]} -> *{collect_data[semester][i][1]}* -> *{collect_data[semester][i][2]}* -> *{collect_data[semester][i][3]}*\n"
    return string


