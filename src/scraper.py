import requests
from bs4 import BeautifulSoup

response = requests.get('https://serenesforest.net/the-sacred-stones/characters/growth-rates/')  # FE8

# print(response.status_code)
# print(response.headers)
page_content = response.content

soup = BeautifulSoup(page_content, features='html.parser')  # clean raw content

# print(soup)

"""
links = soup.find_all('a')
print(links)
"""

# characters = soup.find_all('td')
# print(characters)

# for x in characters:
    # print(x)
    # print('')
    # print('')

# print(characters[0])

"""
<tr>
    <td> ...
    stats
</tr>
"""

# characters = soup.find_all('tr')
# print(characters)

# for char in characters:
    # print(char)
    # print('')

# print(characters[1])

# character = soup.find('Eirika')
# print(character)

"""
characters = soup.find_all('tr')

for character in characters:
    if 'Eirika' in character.text
        print(character)
"""

# characters = soup.find_all('tr')

# for character in characters:
    # if 'Eirika' in character.text
        # print(character)

# for c in characters:
    # print(c.text)


"""
Print Eirika stats.
"""

# characters = soup.find_all('tr')  # get all characters

# print(type(characters))  result set

# for character in characters:
    # print(type(character)) tag
    # print(character)
    # print(type(character.text))
    # print(character.text)


# chars = soup.find_all('tr')

# for char in chars:
#     # print(char.text)

#     data = char.text.split('\n')
#     print(data)


def getGrowths(content):
    stats = [
        f'HP: {content[2]}',
        f'Str / Mag: {content[3]}',
        f'Skill: {content[4]}',
        f'Speed: {content[5]}',
        f'Luck: {content[6]}',
        f'Defense: {content[7]}',
        f'Resistance: {content[8]}'
    ]

    print(stats)



characters = soup.find_all('tr')

for character in characters:
    data = character.text.split('\n')  # ['', 'Eirika', '70', '40', '60', '60', '60', '30', '30', '']

    if data[1] == 'Eirika':
        growths = getGrowths(data)
