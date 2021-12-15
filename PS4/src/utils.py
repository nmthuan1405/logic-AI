from logic import Clause, KnowledgeBase
import re

def read_input(file_name):
    alpha = Clause()
    KB = KnowledgeBase()

    with open(file_name, 'r') as f:
        alpha = Clause.parse(f.readline().rstrip())
        n = int(f.readline())
        for i in range(n):
            KB.append(Clause.parse(f.readline().rstrip()))
    
    return alpha, KB

def write_output(file_name, result):
    res, clauses, count = result

    with open(file_name, 'w') as f:
        for i in range(0, len(count) - 1):
            begin = count[i]
            end = count[i + 1]
            
            f.write(str(end - begin) + '\n')
            for clause in clauses[begin:end]:
                f.write(clause.to_string() + '\n')
        
        if res:
            f.write('YES\n')
        else:
            f.write('NO\n')

def output_filename(filename):
    number = re.findall('\d+', filename)[0]
    return f'output{number}.txt'
