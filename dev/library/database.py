from pprint import pprint

def fetch_page_title(page):
    opt1 = None
    opt2 = None
    opt3 = None

    # pages may not actually have a title (like db items)
    # check if the elements even exist to pull them
    if page.get('properties', {}).get('title', {}).get('title', [{}]):
        opt1 = page.get('properties', {}).get('title', {}).get('title', [{}])[0].get('plain_text')
    if page.get('title'):
        opt2 = page.get('title', [{}])[0].get('plain_text')
    if opt1 == None and opt2 == None:
        opt3 = fetch_page_title_db(page)
    return opt1 or opt2 or opt3 or ''

# the third type will be nested in a property, for a database item
# problem is, the property can be named anything, we need to find the id="title"
def fetch_page_title_db(page):
    for p_key, p_val in page['properties'].items():
        if p_val['id'] == 'title':
            # even if it has a "id":"title" dict, still may end up having no page title for the db item
            if len(p_val.get('title')) >= 1:
                return p_val.get('title', [{}])[0].get('plain_text') 
            else:
                return ""               

def create_db(db, pages):
    print('* No database found! Creating notion.db...')
    with db:
        db.execute("""
            CREATE TABLE PAGE (
                id VARCHAR(40),
                title VARCHAR(100),
                created_time DATETIME,
                last_edited_time DATETIME,
                type VARCHAR(10),
                url VARCHAR(90)
            );
        """)
        db.execute("""
            CREATE TABLE PAGE_PARENT (
                id VARCHAR(40),
                parent_id VARCHAR(40),
                parent_type VARCHAR(15)
            );
        """)
    print('* Schema loaded. Populating data from db.json (this may take awhile)...')
        # iterate over the pages and load them into the db

    for page in pages:
        #from pprint import pprint
        #pprint(page)
        p_id = page['id']
        # title can be in one of several places depending on page type
        title = fetch_page_title(page)
        print('** Importing {} - {}'.format(p_id, title))