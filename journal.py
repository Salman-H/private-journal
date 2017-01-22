from peewee import *

# make a sqlite connection
db = SqliteDatabase('journal.db')


# our entry model is going to hold our journal entries
class Entry(Model):
    """ Holds jounral entries"""
    # content
    # timestamp
    
    class Meta:
        database = db
        

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
    menu_loop()
    