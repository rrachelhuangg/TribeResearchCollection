from firecrawl import Firecrawl
import random
import json

firecrawl = Firecrawl(api_key='fc-71d8f0b5d1f344419cde5d315c57a9ca')

bio_prof_links = [
    {"https://allenlab.pages.wm.edu/publications/":0},
    {"https://lizabethallison.com/publications/":0},
    {"https://andersonlab.pages.wm.edu/publications/":0},
    {"https://sites.google.com/email.wm.edu/bestman-lab/publications?authuser=0":0},
    {"https://sites.google.com/email.wm.edu/randy-chambers/publications?authuser=0":0},
    {"https://dancristollab.pages.wm.edu/publications/":0},
    {"https://dalgleishplantecologylab.pages.wm.edu/publications/":0},
    {"https://forsythlab.pages.wm.edu/publications-and-support/":0},
    {"https://sites.google.com/email.wm.edu/hintonlab/publications?authuser=0":0},
    {"https://sites.google.com/view/leulab/publications?authuser=0":0},
    {"https://www.helenmurphy.net/publications":0},
    {"https://sites.google.com/view/puzey-lab/publications?authuser=0":0},
    {"https://www.ncbi.nlm.nih.gov/myncbi/1xAWOJKM7f4kx/bibliography/public/?sortby=pubDate&sdirection=ascending":0},
    {"https://dcshak.pages.wm.edu/publications-2/":0},
    {"https://jpswad.wixsite.com/johnpswaddle/publications-1":0},
    {"https://www.ncbi.nlm.nih.gov/myncbi/1nAmNq-VbfWQv/bibliography/public/":0},
    {"https://sites.google.com/view/williamson-lab-at-wm/research?authuser=0":0},
    {"https://sites.google.com/view/sahalab/publications?authuser=0":0}
]

count = 0
selected_links = []
while count < 5:
    select = random.randint(0, len(bio_prof_links)-1)
    check = ""
    for entry in bio_prof_links[select]:
        check = entry
        break
    print("CHECK: ", check)
    if bio_prof_links[select][check]==0:
        bio_prof_links[select][check]=1
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

overall_bio_data = {}

for link in selected_links:
    res = firecrawl.extract(
        urls=[link],
        prompt="Extract the page title and description.",
        schema=schema,
    )
    data = res.data["description"]
    print("LINK: ", link)
    print("DATA: ", data)
    overall_bio_data[link] = data

with open("bio_data.json", "w") as file:
    json.dump(overall_bio_data, file, indent=4)


