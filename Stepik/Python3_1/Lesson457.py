from xml.etree import ElementTree
tree = ElementTree.parse('example.xml')
root = tree.getroot()
print(root)
print(root.tag, root.attrib)
for child in root:
    print(child.tag, child.attrib)