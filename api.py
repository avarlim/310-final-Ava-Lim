import json, pprint, requests, urllib, random
import keys

def rand_font(style='None'):
    with urllib.request.urlopen(
            'https://www.googleapis.com/webfonts/v1/webfonts?key=' + keys.google_api_key) as response1:
        data = response1.read().decode()
    all_fonts = json.loads(data)
    all_fonts = all_fonts['items']
    if style == 'None':
        return all_fonts[random.randrange(1, len(all_fonts))]['family']
    font_list = []
    for font in all_fonts:
        if font['category'] == style:
            font_list.append(font)
    return font_list[random.randrange(1, len(font_list))]['family']

def colors_request(b=['N', 'N', 'N', 'N', 'N']):
    url = r'http://colormind.io/api/'
    if b == ['N', 'N', 'N', 'N', 'N']:
        data = {'model': 'ui'}
    else:
        data = {'model': 'ui', 'input': b}
    colors = requests.post(url, json=data)
    color_list = colors.json()
    color_list = color_list['result']
    return color_list

def rbg_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def palett(color_list):
    hex = []
    for c in color_list:
        hex.append(rbg_to_hex(c[0], c[1], c[2]))
    # print(hex)
    base_url = 'https://palett.es/'
    for h in hex:
        base_url += h[1:] + '-'
    url = base_url[:-1]
    return [hex, url]


# rand_font(all_fonts)
# rand_font(styles['sans-serif'])
# colors_request(b=[30, 30, 29], c=[30, 30, 29])

# print(rand_font('handwriting'))