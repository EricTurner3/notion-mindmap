import json
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