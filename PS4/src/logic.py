def pl_resolution(KB, alpha):
    clauses = KB + get_negative_clause(alpha)
    news = []
    while True:
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvents = pl_resolve(clauses[i], clauses[j])
                if [] in resolvents:
                    return True
                new = new + resolvents

        if new in clauses:
            return False
        clauses = clauses + new


def pl_resolve(clause1, clause2):
    resloutents = []
    for literal1 in clause1:
        for literal2 in clause2:
            resolvents = pl_resolve_two_literals(literal1, literal2)
            if resolvents is not None:
                resloutents.append(resolvents)

    return resloutents

def pl_resolve_two_literals(literal1, literal2):
    if literal1 == get_negative_literal(literal2):
        return []
    elif literal1 == literal2:
        return [literal1]
    else:
        return None

def get_negative_clause(alpha):
    clauses = []
    for literal in alpha:
        clauses.append([get_negative_literal(literal)])
    
    return clauses

def get_negative_literal(literal):
    if literal[0] == '-':
        return literal[1:]
    else:
        return '-' + literal
