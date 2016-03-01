"""
Small sphinx extension to enable making image sliders.
"""

from sphinx.util.compat import Directive
from docutils import nodes

class slider(nodes.raw): pass

def visit_slider_html(self, node):
    #self.body.append(self.starttag(node, 'div', 'slider'))
    self.body.append("<div id='slider'>\n")
    for im in node.images:
        self.body.append("    <img src='%s' />\n" % im)
def depart_slider_html(self, node):
    self.body.append('</div>\n')

class SliderDirective(Directive):
        has_content = True
        def run(self):
            el = slider('')
            el.images = [t.strip() for t in self.content]
            return [el]
    

def setup(Sphynx):
    
    Sphynx.add_javascript('js-image-slider.js')
    Sphynx.add_stylesheet('js-image-slider.css')
    
    Sphynx.add_node(slider, html=(visit_slider_html, depart_slider_html))
    Sphynx.add_directive('slider', SliderDirective)
