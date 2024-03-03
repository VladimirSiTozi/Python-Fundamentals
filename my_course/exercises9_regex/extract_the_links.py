import re


valid_urls = []
pattern = r'((w{3})\.([a-zA-Z0-9-\.]+)\.([a-z]+))'
line = input()
while line:
    match = re.search(pattern, line)
    if match:
        valid_urls.append(match.group(0))

    line = input()

for url in valid_urls:
    print(url)

# input
# You can check us at www.london-hotels.co.uk !
# We provide the best services in London.
# Here are some reviews in some blogs:
# London Hotels are awesome! - www.indigo.bloggers.com
# I am very satisfied with their services - ww.ivan.bg
# Best Hotel Services! - www.rebel21.sedecrem.moc
#
# Join WebStars now for free, at www.web-stars.com
# You can also support our partners:
# Internet - www.internet.com
# WebSpiders - www.webspiders101.com
# Sentinel - www.sentinel.-ko