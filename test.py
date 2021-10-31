from parser_ import Parser
from Ltoken import Token
from iterator import Iterator
from drawer import Drawer

rules = {'F': 'F+F', '+': 'F-F', '-': 'F'}
axiom = 'F'
test = Iterator(axiom, rules, 5)

rules_for_parser = {'F': 'MoveToken', '+': 'RotateToken(90)', '-': 'RotateToken(-90)'}

parser = Parser(test.get_final(), rules_for_parser)
parser.get_result()

tok = Token(parser.get_result())
tok.sorted_list()
#print(tok.svg_views)


draww=Drawer()
draww.cline_list_svg_view(tok.svg_views)
draww.draw(draww.cline_list_svg_view(tok.svg_views))




