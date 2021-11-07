# Входные данные : Аксиома, правила, количество повторений
# Количество повторений это replay
class Iterator:

    def __init__(self, axiom, rules, replay):
        self.axiom = axiom
        self.rules = rules
        self.repeat = replay

    def get_string(self):
        out_list = ''
        out = self.axiom
        for number in range(1, self.repeat + 1):
            for tokens in out:
                if tokens in self.rules:
                    out_list += self.rules[tokens]
                else:
                    out_list += tokens
                    continue
            out = out_list
            out_list=''
        return out





