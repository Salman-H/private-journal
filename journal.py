from collections import OrderedDict
import datetime
import sys

from peewee import *

# make a sqlite connection
db = SqliteDatabase('journal.db')


# our entry model is going to hold our journal entries
class Entry(Model):
    """ Holds jounral entries."""
    # not using VarChar field since it demands a max length
    content = TextField()
    # we want the datetime for *whenever* an entry is created.
    # so we use .now instead of .now() since the latter will
    # simply give us the datetime for when we ran the script.
    timestamp = DateTimeField(default=datetime.datetime.now)
    
    # add db as the database attribute in the Meta class
    class Meta:
        database = db
 

def initialize():
    """ Create db and table if not already done."""
    db.connect()
    # safe=True so peewee won't break if ran multiple times with already created tables
    db.create_tables([Entry], safe=True)


def menu_loop():
    """ Show the menu."""
    choice = None
    
    while choice != 'q':
        print("\nEnter 'q' to quit.")
        for key, value in menu.items():
            # in our menu dict, keys are choices and values are functions
            print('{}) {}'.format(key, value.__doc__))
        
        # get user's choice from keyboard
        choice = input('Action: ').lower().strip()
        
        # call the function performing the action corresponding to the choice
        if choice in menu:
            menu[choice]()
    
    
def add_entry():
    """Add an entry."""
    print("Enter your entry. Press ctrl+d when finished.")
    data = sys.stdin.read().strip()
    
    if data:
        while True:
            action = input("\nSave Entry? [Yn] ").lower()
            if action in ('y', 'n'):
                break
            
        if action == "y":    
            Entry.create(content=data)
            print("Saved successfully!")
    
    
def view_entries(search_query=None):
    """View previous entries."""
    # get all entries ordered by latest ones first
    entries = Entry.select().order_by(Entry.timestamp.desc())
    
    # if user provided a query to search specific entries, we only show those entries
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))
        
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        print(timestamp)
        # underline the timestamp with '=' characters equal to its length
        print('=' * len(timestamp))
        # print the entry
        print(entry.content)
        
        print("\nn) for next entry")
        print("q) to return to main menu")
        
        while True:
            next_action = input('Action: [Nq] ').lower().strip()
            if next_action in ('n', 'q'):
                break
            
        if next_action == 'q':    
            break
        

def search_entries():
    """Search entries by keyword."""
    view_entries(input('Search query: '))


def delete_entry(entry):
    """Delete an entry."""
    
  
# an ordered dict used to display menu and call relevant functions
menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),
])


# since we'd wanna import this journal in a flask app if want it
# to run from something other than the command line, we wouldn't
# want it to just run when we import it. Instead, we'd wanna import
# this to reuse some of the main functions since the logic will
# remain the same regardless of whether the journal is accessed
# via a command-line or via a python web app; only the display
# of  information changes.
if __name__ == '__main__':
    initialize()
    menu_loop()
    