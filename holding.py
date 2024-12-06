def xkcd_API_call():
    response = requests.get('https://xkcd.com/info.0.json')
    parsed_data = response.json()
    comic_number = parsed_data['num']
    img_url = parsed_data['img']
    alt_text = parsed_data['alt']
    return comic_number, img_url, alt_text 
num, url, alr = xkcd_API_call()
