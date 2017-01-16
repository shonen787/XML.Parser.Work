import xml.etree.ElementTree as ET
tree = ET.parse('file.xml')
root = tree.getroot()
children = 0

print root.tag
print root.attrib

#for child in root:
#    children = children + 1
#    print child.tag, child.attrib
#amount_of_files = children / 25
#print amount_of_files
