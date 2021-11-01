# Входные данные : Аксиома, правила, количество повторений
# Количество повторений это replay
class Iterator:

    def __init__(self, axiom, rules, replay):
        self.axiom = axiom
        self.rules = rules
        self.repeat = replay
        self.axiom_out = ''

    # получаем на входе оксиому и изменям ее n-ое количество раз.
    def get_final(self):
        out = ''
        axiom = self.axiom
        self.axiom=''
        s=1
        for number in range(1, self.repeat + 1):
            for tokens in axiom:
                if tokens == 'F':
                    s+=1
                    out+=tokens
                    if 'F' in self.rules:
                        out=out[:-1]
                        out+=self.rules[tokens]
                        if s+self.repeat+1 > len(axiom):  # тут проблема
                            axiom=out
                            out=''
                            s=1
                            break
                        else:
                            continue
                    else:
                        out+=tokens
                        continue
                elif tokens == '+':
                    out+=tokens
                    if '+' in self.rules:
                        out=out[:-1]
                        out+=self.rules[tokens]
                        if s+self.repeat+1 > len(axiom):  # тут проблема
                            axiom=out
                            out=''
                            s=1
                            break
                        else:
                            continue
                elif tokens == '-':
                    out+=tokens
                    if '-' in self.rules:
                        out=out[:-1]
                        out+=self.rules[tokens]
                        if s+self.repeat+1 > len(axiom):  # тут проблема
                            axiom=out
                            out=''
                            s=1
                            break
                        else:
                            continue
        if self.repeat == 1:
            self.axiom_out=axiom
        else:
            self.axiom_out=out
        return self.axiom_out



# не правильная механика замены. надо что бы каждый элемент запенялся по правилу. скорее всего лучше будет это делать через строку. работа со строками лучше.

rules = {'F': 'F+F-F-F+F'}
axiom = 'F'
test = Iterator(axiom, rules, 1)
print(test.get_final())
