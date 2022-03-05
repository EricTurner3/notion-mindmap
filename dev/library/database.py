def fetch_page_title(page):
    opt1 = page.get('properties', {}).get('title', {}).get('title', [{}])[0].get('plain_text')
    opt2 = page.get('title', [{}])[0].get('plain_text')
    opt3 = fetch_page_title_db(page)

    return opt1 or opt2 or opt3 or '!!!!!!!!!!!!!! ERR !!!!!!!!!!!!!!'

# the third type will be nested in a property, for a database item
# problem is, the property can be named anything, we need to find the id="title"
def fetch_page_title_db(page):
    try:
        for property in page['properties']:
            for subprop in property:
                for id, val in subprop.items():
                    if id == 'id' and val == 'title':
                        return subprop.get('title', [{}])[0].get('plain_text')                
    except: 
        return None
