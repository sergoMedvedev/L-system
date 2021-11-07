import drawSvg as draw
import math


class State:
    def __init__(self, x=0, y=0, direction=0):
        self.x = x
        self.y = y
        self.direction = direction


class Token:

    def __init__(self, final_list, angel):
        self.list = final_list
        self.angel = angel

    def sorted_list(self):
        state = State()
        self.svg_views = []
        for tokens in self.list:
            if tokens == 'RotateToken(+)':
                angel = self.angel / 360 * 2 * math.pi
                self.token = RotaitToken(self.angel)
                self.svg_views.append(self.token.get_svg_view(state, angel))
            elif tokens == 'RotateToken(-)':
                angel = self.angel / 360 * 2 * math.pi
                self.token = RotaitToken(angel)
                self.svg_views.append(self.token.get_svg_view(state, angel))
            elif tokens == 'MoveToken':
                self.token = MoveToken()
                self.svg_views.append(self.token.get_svg_view(state))


class MoveToken:


    def get_svg_view(self, state):
        old_x = state.x
        old_y = state.y
        state.x = state.x + 5 * math.cos(state.direction)
        state.y = state.y + 5 * math.sin(state.direction)
        return [
            draw.Line(
                old_x, old_y,
                state.x, state.y,
                stroke='black'
            )
        ]


class RotaitToken:

    def __init__(self,angel):
        self.angel=angel

    def get_svg_view(self, state, angel):
        if angel == angel / 360 * 2 * math.pi:
            state.direction += angel / 360 * 2 * math.pi
        else:
            state.direction += angel / 360 * -2 * math.pi
        return 0
