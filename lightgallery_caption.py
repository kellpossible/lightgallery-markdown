from markdown import Extension
from markdown.treeprocessors import Treeprocessor
from markdown.util import etree
import re

class ImagesTreeprocessor(Treeprocessor):
    def __init__(self, md):
        Treeprocessor.__init__(self, md)

    def run(self, root):
        parent_map = {c:p for p in root.iter() for c in p}
        images = root.getiterator("img")
        for image_node in images:
            a_node = parent_map[image_node]

            # check that parent of the image is an anchor
            if a_node.tag == 'a':
                # check that the href of the anchor matches the image href
                if a_node.get('href') == image_node.get('src'):
                    parent = parent_map[a_node]

                    # if there is no description in the image tag
                    # use the text in the parent p tag
                    if parent.tag == 'p' and a_node.tail != None:
                        desc = a_node.tail
                    else:
                        desc = ""

                    ix = list(parent).index(a_node)
                    div_node = etree.Element('div')
                    div_node.set("class","lightgallery")
                    a_node.set("data-sub-html", desc)
                    div_node.append(a_node)
                    parent.insert(ix, div_node)
                    parent.remove(a_node)


class LightGalleryExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.treeprocessors.add("lightgallery_caption", ImagesTreeprocessor(md), "_end")


def makeExtension(configs={}):
    return LightGalleryExtension(configs=configs)
