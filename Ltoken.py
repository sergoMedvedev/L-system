class Token:

    def __init__(self,final_list):
        self.final_list=final_list
        self.token=...
        self.angla=...


    def To_str(self):
         return 'bais_token'



    def sorted_list(self):
        for tokens in self.final_list:
            print(tokens)
            if (tokens[-4]+tokens[-3]+tokens[-2]) == '-90':
                self.angla = int('-90')
                self.token = RotaitToken(self.angla)
                self.token.do_paint(self.angla)
            elif (tokens[-3]+tokens[-2]) == '90':
                self.angla = int(90)
                self.token = RotaitToken(self.angla)


            elif (tokens[-4]+tokens[-3]+tokens[-2]) == '-90' and (tokens[-3]+tokens[-2]) == '90':
                self.angla = 0
                self.token = MoveToken(self.angla)


    def do_paint(self,angla):











class MoveToken(Token):

    def __init__(self,angla):
        self.angla = angla


    def To_str(self):
        return 'move token'












class RotaitToken(Token):




    def To_str(self):
        return 'rotait token'+ str(self.angle)


    def fff(self):
        ...





final_list=['MoveToken', 'RotateToken(90)', 'MoveToken', 'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'RotateToken(-90)', 'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'RotateToken(-90)', 'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'RotateToken(-90)', 'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken']

first_test=Token(final_list)
first_test.sorted_list()
