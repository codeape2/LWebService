import sys
from xml.etree import ElementTree as E
from xml.dom import minidom as D

doc = D.parse(sys.argv[1])
print doc.toprettyxml(indent="    ")
