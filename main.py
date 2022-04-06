from bs4 import BeautifulSoup
import requests
import json
import pprint


url = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')
# print(soup.prettify())
props_str = soup.find(name='script', id='__NEXT_DATA__').text
# print(type(props_str))

props_obj = json.loads(props_str)
# print(type(props_obj))

json_obj = json.dumps(props_obj, indent=2, sort_keys=True)
# print(type(json_obj))

data_base = (props_obj['props']['pageProps']['apolloState'])
images = (data_base['Article:5d118bb6a91b155aa79bfc19']['_layout'][7]['content']['images'])
# print((data_base), "\n")
# print(images)
image_names = [(images[x]['__ref']) for x in range(100)]
# for x in range(100):
#     image_names.append(images[x]['__ref'])

# print(type(image_names))

title_text = [(data_base[image_names[x]]['titleText']) for x in range(100)]
# for x in range(100):
#     title_text.append(data_base[image_names[x]]['titleText'])

ordered_movies = title_text[::-1]
print(ordered_movies)

with open('movies.txt', 'w') as file:
    for item in ordered_movies:
        file.write('%s\n' % item)

# for movie in

