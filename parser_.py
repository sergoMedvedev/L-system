# пробегаем по строке и определяет с какому классу токин относится символ


class Parser:

    def __init__(self, axiom, rules):
        self.axiom = axiom
        self.rules = rules
        self.final_list = []


    def get_result(self):
        for tokens in self.axiom:
            if tokens == 'F':
                self.final_list.append(self.rules['F'])
            elif tokens == '+':
                self.final_list.append(self.rules['+'])
            elif tokens == '-':
                self.final_list.append(self.rules['-'])
        return self.final_list




