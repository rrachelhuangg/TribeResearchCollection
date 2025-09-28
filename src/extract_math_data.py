from firecrawl import Firecrawl
import random
import json

firecrawl = Firecrawl(api_key='fc-71d8f0b5d1f344419cde5d315c57a9ca')

math_prof_links = [
    {"https://prclare.people.wm.edu/research.php":0},
    {"https://scholar.google.com/citations?hl=en&tzom=240&user=HoBn35YAAAAJ&view_op=list_works&sortby=pubdate":0},
    {"https://www.fan-ge.net/":0},
    {"https://scholar.google.com/citations?user=9P_VwdgAAAAJ":0},
    {"https://scholar.google.com/citations?user=eSwoS1sAAAAJ&hl=en&oi=ao":0},
    {"https://www.math.wm.edu/~rrkinc/research.html":0},
    {"https://cklixx.people.wm.edu/#research":0},
    {"https://sites.google.com/view/atninh/research?authuser=0":0},
    {"https://scholar.google.com/citations?user=rMKp4WoAAAAJ&hl=en&oi=ao":0},
    {"https://jxshix.people.wm.edu/publication.html":0},
    {"https://yumingsun.github.io/personal_website/publication/":0},
    {"https://www.math.wm.edu/~eswartz/publications":0},
    {"https://people.wm.edu/~gwang01/pubs.html":0},
    {"https://gyu.people.wm.edu/research.htm":0}
]

count = 0
selected_links = []
while count < 5:
    select = random.randint(0, len(math_prof_links)-1)
    check = ""
    for entry in math_prof_links[select]:
        check = entry
        break
    print("CHECK: ", check)
    if math_prof_links[select][check]==0:
        math_prof_links[select][check]=1
        count += 1
        response = firecrawl.crawl(check,
            limit=1,
            scrape_options={
                'formats': [
                    'links',
                ],
                'proxy': 'auto',
                'maxAge': 600000,
                'onlyMainContent': True,
                'prompt':'Extract all of the links from this page.'
            }
        )
        prof_links = []
        for doc in response.data:
            for link in doc.links:
                if '.pdf' in link:
                    if len(prof_links) >=5:
                        break
                    else:
                        prof_links += [link]
        selected_links += prof_links

print("SELECTED LINKS: ", selected_links)

schema = {
    "type": "object",
    "properties": {"title": {"type":"string"}, "description": {"type": "string"}},
    "required": ["description"],
}

overall_math_data = {}

for link in selected_links:
    res = firecrawl.extract(
        urls=[link],
        prompt="Extract the page title and description.",
        schema=schema,
    )
    data = res.data["description"]
    print("LINK: ", link)
    print("DATA: ", data)
    overall_math_data[link] = data

with open("math_data.json", "w") as file:
    json.dump(overall_math_data, file, indent=4)


