import drawSvg as draw


class State:
    def __init__(self, x=0, y=0, direction=0):
        self.x = x
        self.y = y
        self.direction = direction


class Token:

    def __init__(self, final_list):
        self.final_list = final_list


    def sorted_list(self):
        state = State()
        self.svg_views = []
        for tokens in self.final_list:
            if tokens == 'RotateToken(-90)':
                self.angla = int('-90')
                self.token = RotaitToken(self.angla)
                self.svg_views.append(self.token.get_svg_view(state,self.angla))
            elif tokens == 'RotateToken(90)':
                self.angla = int(90)
                self.token = RotaitToken(self.angla)
                self.svg_views.append(self.token.get_svg_view(state,self.angla))
            elif tokens == 'MoveToken':
                self.angla = 0
                self.token = MoveToken(self.angla)
                self.svg_views.append(self.token.get_svg_view(state))


class MoveToken(Token, State):

    def get_svg_view(self, state):
        old_x = state.x
        old_y = state.y
        if state.direction == 0:
            state.x += 10
        elif state.direction == 90:
            state.y += 10
        elif state.direction == -90:
            state.y -= 10
        elif (state.direction == 180) or (state.direction == -180):
            state.x -= 10
        return [
            draw.Line(
                old_x, old_y,
                state.x, state.y
            )
        ]


class RotaitToken(Token):

    def get_svg_view(self, state,angla):
        if angla == 90:
            state.direction+=90
        else:
            state.direction-=90
        return 0


#final_list = ['MoveToken', 'RotateToken(-90)', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'MoveToken', 'MoveToken',
#              'RotateToken(90)', 'MoveToken',
#              'MoveToken', 'RotateToken(90)', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'RotateToken(-90)',
#              'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken',
#              'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken',
#              'RotateToken(90)', 'MoveToken', 'RotateToken(-90)', 'MoveToken', 'MoveToken', 'RotateToken(90)',
#              'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'MoveToken', 'MoveToken', 'RotateToken(90)',
#              'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'RotateToken(90)', 'MoveToken',
#              'RotateToken(-90)', 'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'MoveToken',
#              'RotateToken(90)', 'MoveToken', 'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'MoveToken',
#              'RotateToken(90)', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'RotateToken(-90)', 'MoveToken',
#              'MoveToken', 'RotateToken(90)', 'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'MoveToken',
#              'MoveToken', 'RotateToken(90)', 'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken',
#              'RotateToken(90)', 'MoveToken', 'RotateToken(-90)', 'MoveToken', 'MoveToken', 'RotateToken(90)',
#              'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'MoveToken', 'MoveToken', 'RotateToken(90)',
#              'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken', 'RotateToken(90)', 'MoveToken',
#              'RotateToken(-90)', 'MoveToken', 'MoveToken', 'RotateToken(90)', 'MoveToken']
#
#first_test = Token(final_list)
#first_test.sorted_list()
#print(first_test.svg_views)
