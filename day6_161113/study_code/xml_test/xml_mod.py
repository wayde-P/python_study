import xml.etree.ElementTree as ET

tree = ET.parse("country.xml")
root = tree.getroot()
print(root.tag)