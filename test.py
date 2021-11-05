from parser_ import Parser
from Ltoken import Token
from iterator import Iterator
from drawer import Drawer

rules = {'X': 'X+YF+', 'Y': '-FX-Y'}
axiom = 'FX'
test = Iterator(axiom, rules,10)

rules_for_parser = {'F': 'MoveToken', '+': 'RotateToken(-90)', '-': 'RotateToken(90)'}
parser = Parser(test.get_final(), rules_for_parser)


tok = Token(parser.get_result())
#tok.sorted_list()
tok.sorted_list()


draww=Drawer()
#draww.cline_list_svg_view(tok.svg_views)
draww.cline_list_svg_view(tok.svg_views)
draww.draw(draww.cline_list_svg_view(tok.svg_views))




