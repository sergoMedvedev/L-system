from parser_ import Parser
from Ltoken import Token
from iterator import Iterator
from drawer import Drawer

rules = {'F': 'F+F', '+': 'F-F', '-': 'F'}
axiom = 'F'
test = Iterator(axiom, rules, 2)
#print(test.get_final())

rules_for_parser = {'F': 'MoveToken', '+': 'RotateToken(90)', '-': 'RotateToken(-90)'}





parser = Parser(test.get_final(), rules_for_parser)
#parser.get_result()
#print(parser.get_result())


tok = Token(parser.get_result())
#tok.sorted_list()
tok.sorted_list()



draww=Drawer()
#draww.cline_list_svg_view(tok.svg_views)
print(draww.cline_list_svg_view(tok.svg_views),'\n')
draww.draw(draww.cline_list_svg_view(tok.svg_views))




