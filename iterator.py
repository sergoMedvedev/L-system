# Входные данные : Аксиома, правила, количество повторений
# Количество повторений это replay
class iterator:

    def __init__(self,axiom,rules,replay):
        self.axiom = axiom
        self.rules = rules
        self.replay=replay


    def get_final(self):
        out=[]
        for number in range(1,self.replay+1):
            for tokens in self.axiom:
                if tokens == 'F':
                    out.append(self.rules[tokens])
                    continue
                elif tokens == '+':
                    out.append(self.rules[tokens])
                    continue
                elif tokens == '-':
                    out.append(self.rules[tokens])
                    continue
        self.axiom=''
        for i in out:
            self.axiom+=i

        return print(self.axiom)





