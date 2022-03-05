from notion_client import Client
import sqlite3 as sl
import json
import os
# my functions, in separate files to keep this one cleaner
from library.download import get_all_pages, save_db_json
from library.database import create_db

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





# Stage 1: Notion Pages Download to JSON
# check for existing db.json file to use
if os.path.exists('./db.json'):
    val = input('* Hey! a db.json already exists! Do you want to download a new copy from notion? (y/n)')
    # download a fresh copy
    # not even gonna input validate. If 'y' isn't explicity passed then just move on.
    if val=='y':
        print('* Generating new db.json...')
        pages = get_all_pages(notion)
        save_db_json(pages)
    else:
        print('* Loading db.json...')
        pages = json.load(open('db.json'))

# no file found, download a new one
else:
    print('* I didn\'t find a db.json file so I\'m fetching your pages from Notion now...')
    pages = get_all_pages(notion)
    save_db_json(pages)


# Stage 2: JSON to Sqlite3
if os.path.exists('./notion.db'):
    val = input('* notion.db already exists! Do you want to recreate it? (y/n)')
    # download a fresh copy
    # not even gonna input validate. If 'y' isn't explicity passed then just move on.
    if val=='y':
        print('* Generating new notion.db...')
        os.remove('notion.db')          # removing it first causes sqlite3 to regenerate a new one
        con = sl.connect('./notion.db') 
        create_db(con, pages) 
    else:
        print('* Loading existing notion.db...')



