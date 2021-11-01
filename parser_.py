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
        print(self.final_list)
        return self.final_list



#axiom_out='F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F'
#rules_for_parser = {'F': 'MoveToken', '+': 'RotateToken(90)', '-': 'RotateToken(-90)'}
#
#testt=Parser(axiom_out,rules_for_parser)
#print(testt.get_result())
