# Входные данные : Аксиома, правила, количество повторений
# Количество повторений это replay
class Iterator:

    def __init__(self, axiom, rules, replay):
        self.axiom = axiom
        self.rules = rules
        self.repeat = replay
        self.axiom_out=''

    # получаем на входе оксиому и изменям ее n-ое количество раз.
    def get_final(self):
        out = []
        axiom = self.axiom
        for number in range(1, self.repeat + 1):
            for tokens in axiom:
                if tokens == 'F':
                    out.append(self.rules[tokens])
                elif tokens == '+':
                    out.append(self.rules[tokens])
                elif tokens == '-':
                    out.append(self.rules[tokens])
            axiom = ''
            for letter in out:
                axiom += letter
        self.axiom_out=axiom
        return self.axiom_out

# нашел некоторые недочеты. все работает исправно.


