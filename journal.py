import datetime
from collections import OrderedDict
from peewee import *

# make a sqlite connection
db = SqliteDatabase('journal.db')

# an ordered dict used to display menu and call relevant functions
menu = OrderedDict([
    ('a', 'add_entry'),
    ('v', 'view_entries')
])


# our entry model is going to hold our journal entries
class Entry(Model):
    """ Holds jounral entries"""
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
    """ Create db and table if not already done"""
    db.connect()
    # safe=True so peewee won't break if ran multiple times with already created tables
    db.create_tables([Entry], safe=True)


def menu_loop():
    """ Show the menu"""
    
    
def add_entry():
    """ Add an entry"""
    
    
def view_entries():
    """ View previous entries"""
    

def delete_entry(entry):
    """ Delete an entry"""
    
    
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
    