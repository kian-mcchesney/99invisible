import xml.etree.ElementTree as ET

import xml.etree.ElementTree as ET
tree = ET.parse('episode-sitemap.xml')
root = tree.getroot()

# In find/findall, prefix namespaced tags with the full namespace in braces
for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
    loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
    print(loc)



# I used this link https://stackoverflow.com/questions/62002418/sitemap-xml-parsing-in-python-3-x