# Входные данные : Аксиома, правила, количество повторений
# Количество повторений это replay
class Iterator:

    def __init__(self, axiom, rules, replay):
        self.axiom = axiom
        self.rules = rules
        self.repeat = replay
        self.axiom_out = ''

    def get_final(self):
        step_axiom = ''

        def variables_tokens(tokens, step_axiom):
            if (tokens == 'X') and (tokens in self.rules):
                step_axiom += self.rules[tokens]
            elif (tokens == 'Y') and (tokens in self.rules):
                step_axiom += self.rules[tokens]
            return step_axiom

        def const_tokens(tokens, step_axiom):
            if tokens == '+':
                step_axiom += tokens
            elif tokens == '-':
                step_axiom += tokens
            elif tokens == 'F':
                step_axiom += tokens
            return step_axiom

        for number in range(1, self.repeat + 1):
            for tokens in self.axiom:
                if tokens == 'X':
                    step_axiom=variables_tokens(tokens, step_axiom)
                elif tokens == 'Y':
                    step_axiom=variables_tokens(tokens, step_axiom)
                elif tokens == '+':
                    step_axiom=const_tokens(tokens, step_axiom)
                elif tokens == 'F':
                    step_axiom=const_tokens(tokens, step_axiom)
                elif tokens == '-':
                    step_axiom=const_tokens(tokens, step_axiom)
            self.axiom = step_axiom
            step_axiom = ''
        return self.axiom



