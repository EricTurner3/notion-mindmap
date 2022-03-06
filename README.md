# notion-mindmap

Framework for developing and visualizing mind maps in notion.

### **WORK IN PROGRESS** - Forked from [here](https://github.com/davidAmiron/notion-mindmap) on 4 Mar 2022
* While this initially was a fork, everything here has been scrapped and completely redone. Only the original name remains
* After getting all of the data into SQLite3, I realized there are things called Graph DB, like neo4j, which is essentially exactly what I wanted to do. For now I will leave it as sqlite3, to dump that as csv for neo4j:
    ```bash
    $ sqlite3 notion.db
    sqlite> .headers on
    sqlite> .mode csv
    sqlite> .output page.csv
    sqlite> select * from PAGE;
    sqlite> .output page_parent.csv
    sqlite> select * from PAGE_PARENT;
    sqlite> .quit
    ```
* Instructions for importing into Neo4j Desktop can be found [here](https://neo4j.com/developer/desktop-csv-import/).
    ```
    // loading neo4j with page_parent.csv and page.csv
    // 1. Spin up a new instance and add the files to the instances /import folder
    //      - Note, if you don't know where this is, just try to run one of the load commands and it will error out and tell you where it should be.
    // 2. Launch neo4j browser and connect. Run these commands:

    // load page.csv
    LOAD CSV WITH HEADERS FROM 'file:///page.csv' AS row
    MERGE (p:Page {pageId: row.id, title:row.title, createdTime: row.created_time, lastEditedTime: row.last_edited_time, pageType:row.type, url:row.url})
    RETURN count(p)

    // load page_parent.csv
    LOAD CSV WITH HEADERS FROM 'file:///page_parent.csv' as row
    MERGE (pp:Parent {id: row.id, parentId: coalesce(row.parent_id, "Workspace"), parentType: row.parent_type})

    // create connections
    LOAD CSV WITH HEADERS FROM 'file:///page_parent.csv' as row
    MATCH (p:Page {pageId: row.id})
    MATCH (pp:Parent {id: row.id})
    MERGE (pp)-[:IS]->(p)
    RETURN *;

    LOAD CSV WITH HEADERS FROM 'file:///page_parent.csv' as row
    MATCH (p:Page {pageId: row.id})
    MATCH (pp:Parent {parentId: row.parent_id})
    MERGE (p)-[:CHILD_OF]->(pp)
    RETURN *;

    ```
* At some point, I may look into creating the csvs automatically or just running commands to directly add to neo4j. There is just more setup involved vs sqlite.

## Setup
1. Clone this project and install prereqs, preferably in a venv and run `pip install -r requirements.txt`
2. Get your notion token, see [here](https://developers.notion.com/docs/getting-started) and place it in the `./token` file.
1. Authorize the token to your pages/databases
1. Run the script


## Setup (For Beginners)
1. This code is written in [Python](https://www.python.org/downloads/), and it's best to use [Pip](https://pip.pypa.io/en/stable/installation/) for package management and [virtualenv](https://pip.pypa.io/en/stable/installation/) for virtual environments (see more below)
1. Clone this repo onto your computer with `git clone https://github.com/EricTurner3/notion-mindmap`, or use the Download ZIP feature and enter into the directory with Command Prompt or Powershell
1. Virtual environments help prevent conflictions if you have multiple projects that require different versions of the same library. `virtualenv venv` will create a `./venv` folder for you to use
1. With `./venv` created, run:
    - Windows:  `. .\venv\Scripts\activate.ps1`
    - *nix: `source /venv/bin/activate`
1. Your terminal will display `(venv)` as a prefix now to indicate you are in the virtual environment. Run `pip install -r requirements.txt` to install all the requirements to use this project
1. Now read the directions [here](https://developers.notion.com/docs/getting-started) to grab your token and place it in the `./token` file
1. Authorize the token to your pages/databases
1. Run the script


