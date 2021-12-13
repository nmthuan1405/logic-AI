from __future__ import annotations

class Literal(str):
    def __invert__(self) -> Literal:
        if self[0] == '-':
            return Literal(self[1:])
        else:
            return Literal('-' + self)

class Clause(list):
    def __init__(self, *literals):
        for literal in literals:
            self.append(literal)

    def append(self, literal) -> None:
        if True in self:
            return

        if (literal is False) or (literal in self):
            return
        if (literal is True) or (~literal in self):
            self.clear()
            super().append(True)
            return

        super().append(literal)

    def remove_literal(self, literal: Literal) -> Clause:
        result = Clause(*self)
        result.remove(literal)
        return result

    def __add__(self, clause: Clause) -> Clause:
        result = Clause(*self)
        for literal in clause:
            result.append(literal)
        return result

    def __invert__(self) -> KnowledgeBase:
        result = KnowledgeBase()
        for literal in self:
            result.append(Clause(~literal))
        return result

class KnowledgeBase(list):
    def __init__(self, *clauses):
        for clause in clauses:
            self.append(clause)
    
    def append(self, clause: Clause) -> None:
        if clause not in self:
            super().append(clause)

    def issubset(self, KB: KnowledgeBase) -> bool:
        for clause in self:
            if clause not in KB:
                return False
        return True

    def __add__(self, KB: KnowledgeBase) -> KnowledgeBase:
        result = KnowledgeBase(*self)
        for clause in KB:
            result.append(clause)
        return result


def pl_resolution(KB: KnowledgeBase, alpha: Clause):
    clauses = KB + ~alpha

    new = KnowledgeBase()
    while True:
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvents = pl_resolve(clauses[i], clauses[j])
                new = new + resolvents

        if [] in resolvents:
            return True, new
        if new.issubset(clauses):
            return False, new
        clauses = clauses + new

def pl_resolve(clause1: Clause, clause2: Clause) -> KnowledgeBase:
    resolvents = KnowledgeBase()
    for literal1 in clause1:
        if ~literal1 in clause2:
            resolvents.append(clause1.remove_literal(literal1) + clause2.remove_literal(~literal1))
    
    return resolvents

a = Literal('a')
b = Literal('b')
c = Literal('c')
d = Literal('d')

A = Clause(a, b)
B = Clause(~b, c)
alpha = Clause(a, c)
KB = KnowledgeBase(A, B)

print(pl_resolution(KB, alpha))
