import argparse
import requests
from bs4 import BeautifulSoup

parser=argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=True, help="URL to attack")
args = vars(parser.parse_args())


URL = args['url']
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

images = soup.find_all("img")
links = soup.find_all("a")
rel_links = soup.find_all("link")

images_src = []
links_href = []


for i in range(0, len(images)):
    images_src.append(images[i]["src"])

for l in range(0, len(links)):
    try:
        links_href.append(links[l]["href"])

    except KeyError:
        continue


for r in range(0, len(rel_links)):
    try:
        links_href.append(rel_links[r]["href"])

    except KeyError:
        continue


path_break=[]

content = []

for i in images_src:
    if i[0:7] == "http://":
        pass

    elif i[0:8] == "https://":
        pass

    else:
        if i.split('/')[0] != "" and i.split('/')[0] not in content:
            content.append(i.split('/')[0])

        elif i.split('/')[0] == "":
            if i.split('/')[1] != "" and i.split('/')[1] not in content:
                content.append(i.split('/')[1])

            elif i.split('/')[1] == "" and i.split('/')[2] not in content:
                content.append(i.split("/")[2])


for l in links_href:
    if l[0:7] == "http://":
        pass

    elif l[0:8] == "https://":
        pass

    elif l[0:1] == "#":
        continue

    elif l.__contains__("/"):
        if l.split('/')[0] != "" and l.split('/')[0] not in content:
            content.append(l.split('/')[0])

        elif l.split('/')[1] not in content:
            content.append(l.split('/')[1])

    else:
        continue

files = []
directories = []

for c in content:
    if "." in c:
        files.append(c)

    else:
        directories.append(c)

print("On index page:")

print("\nDirectories:")

for d in directories:
    print(d)

print("\nFiles:")
for f in files:
    print(f)
