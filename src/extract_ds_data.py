from firecrawl import Firecrawl
import random
import json

firecrawl = Firecrawl(api_key='fc-71d8f0b5d1f344419cde5d315c57a9ca')

ds_prof_links = [
    {"https://haipeng-chen.github.io/":0}, 
    {"https://cristianofanelli.com/research/":0}, 
    {"https://yhe15.people.wm.edu/publication.html":0}, 
    {"https://alexandernwala.com/publications/":0}, 
    {"https://scholar.google.com/citations?user=j4EYclEAAAAJ&hl=en":0}, 
    {"https://swensonlab.weebly.com/pubs.html":0}, 
    {"https://jd92.wang/publications/":0}, 
    {"https://eaglew.github.io/publications/ ":0}, 
]

count = 0
selected_links = []
while count < 5:
    select = random.randint(0, len(ds_prof_links)-1)
    check = ""
    for entry in ds_prof_links[select]:
        check = entry
        break
    print("CHECK: ", check)
    if ds_prof_links[select][check]==0:
        ds_prof_links[select][check]=1
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

overall_ds_data = {}

for link in selected_links:
    res = firecrawl.extract(
        urls=[link],
        prompt="Extract the page title and description.",
        schema=schema,
    )
    data = res.data["description"]
    print("LINK: ", link)
    print("DATA: ", data)
    overall_ds_data[link] = data

with open("ds_data.json", "w") as file:
    json.dump(overall_ds_data, file, indent=4)


