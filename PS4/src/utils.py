OR = ' OR '

def read_input(file_name):
    alpha = None
    KB = []

    with open(file_name, 'r') as f:
        alpha = parse_clause(f.readline().rstrip())
        n = int(f.readline())
        for i in range(n):
            KB.append(parse_clause(f.readline().rstrip()))
    
    return alpha, KB

def parse_clause(clause_str):
    clause = []
    for literal in clause_str.split(OR):
        literal = literal.replace(' ', '')
        if literal != '':
            clause.append(literal)

    return clause