import drawSvg as draw
import math


class State:
    def __init__(self, x=0, y=0, direction=0):
        self.x = x
        self.y = y
        self.direction = direction


class Token():

    def __init__(self,final_list):
        self.list=final_list







    def sorted_list(self):
        state = State()
        self.svg_views = []
        for tokens in self.list:
            if tokens == 'RotateToken(-90)':
                angla = math.pi / -2
                self.token = RotaitToken(angla)
                self.svg_views.append(self.token.get_svg_view(state, angla))
            elif tokens == 'RotateToken(90)':
                angla = math.pi / 2
                self.token = RotaitToken(angla)
                self.svg_views.append(self.token.get_svg_view(state, angla))
            elif tokens == 'MoveToken':
                angla = 0
                self.token = MoveToken(angla)
                self.svg_views.append(self.token.get_svg_view(state, angla))


class MoveToken(Token, State):

    def get_svg_view(self, state, angla=0):
        old_x = state.x
        old_y = state.y
        state.x = state.x + 10 * math.cos(state.direction)
        state.y = state.y + 10 * math.sin(state.direction)
        # print(state.x,' ',state.y)

        # if state.direction == 0:
        #    state.x += 10
        # elif state.direction == 90:
        #    state.y += 10
        # elif state.direction == -90:
        #    state.y -= 10
        # elif (state.direction == 180) or (state.direction == -180):
        #    state.x -= 10
        return [
            draw.Line(
                old_x, old_y,
                state.x, state.y,
                stroke='black'

            )
        ]


class RotaitToken(Token):

    def get_svg_view(self, state, angla):

        if angla == math.pi / 2:
            state.direction += math.pi / 2
            # print(state.x,' ',state.y,' ',state.direction)
        else:
            state.direction += math.pi / -2
            # print(state.x,' ',state.y,' ',state.direction)
        return 0
