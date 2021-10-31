import drawSvg as draw


class Drawer:

    def cline_list_svg_view(self, svg_view):
        #print(svg_view, '\n')
        list = []
        for i in svg_view:
            if i != 0:
                list.append(i)
            else:
                continue
        return list

    def draw(self, svg_view):
        d = draw.Drawing(100, 100, origin=(0, 0), displayInline=False)
        for draww in svg_view:
            d.append(draww[0])
        d.setPixelScale(5)
        d.saveSvg('out_file')
