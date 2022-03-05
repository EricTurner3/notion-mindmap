from notion_client import Client
from pprint import pprint
import json
import os

# why not
print(
'''
=========================================
.  .    ,          .  .      ..  .        
|\ | _ -+-* _ ._   |\/|*._  _||\/| _.._   
| \|(_) | |(_)[ )  |  ||[ )(_]|  |(_][_)  
                                     |  
=========================================                                      
'''
    )

# token is saved in ./token and read from that file
if os.path.exists('./token'):
    token = os.read(os.open('token', os.O_RDONLY), 100).strip()
    print('* Authorizing with token {}'.format(str(token)))
    notion = Client(auth=token)
else:
    print('! CRITICAL ERROR: NO TOKEN SET! Add your token to ./token')

def get_all_pages(client):
    count = 100             # number of results to return per page (max 100)
    query_pg = 0            # determine the count of pages being queried
    pages = list()          # store the page json
    next_cursor = None      # for next page
    while True:
        query_pg += 1
        print('** Fetching Page {}'.format(query_pg))
        data = client.search(**{"page_size": count, "start_cursor": next_cursor})
        pages.extend(data['results']) # add the contents to the main list
        next_cursor = data['next_cursor'] # grab the next page

        if not data['has_more']:
            break # leave the loop when 'has_more' returns False
    return pages

def save_db_json(pages):
    out_file = open("db.json", "w")
    print('** Total Pages Retrieved: {}'.format(len(pages)))
    print('** Outputting pages to ./db.json')
    json.dump(pages, out_file, indent = 6)
    out_file.close()



# Stage 1: Notion Pages Download to JSON
# check for existing db.json file to use
if os.path.exists('./db.json'):
    val = input('* Hey! a db.json already exists! Do you want to download a new copy from notion? (y/n)')
    # download a fresh copy
    if val=='y':
        print('* Generating new db.json...')
        save_db_json(get_all_pages(notion))
    # use existing copy
    else:
        print('* Moving on!')
# no file found, download a new one
else:
    print('* I didn\'t find a db.json file so I\'m fetching your pages from Notion now...')
    save_db_json(get_all_pages(notion))


# Stage 2: JSON to Sqlite3
  
