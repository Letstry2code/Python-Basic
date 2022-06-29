from sqlalchemy.orm import sessionmaker    
from sqlalchemy import create_engine
from Database import Author


def opendb():
    engine =create_engine('sqlite:///mydb.sqlite') ##Fixed Code
    Session=sessionmaker(bind=engine)
    return Session()

def add_author(name):
    db=opendb()                           #  Open db
    a=Author(name=name)                   # Create new author
    db.add(a)                               # Add author to db
    db.commit()                             # Commit changes        
    db.close()                              # Clsoe db        


def show_authors():
    db=opendb()
    authors=db.query(Author).all()
    db.close()
    return authors


def delete_author(name):
    try:
        db=opendb()
        a=db.query(Author).filter_by(name=name).first()
        db.delete(a)
        db.commit()
        db.close()
        print('Author Deleted')
    except:
        print('Author not Found')



while True:
    print('-'*20)
    print('1. Add Author')
    print('1. Display Author')
    print('3. Delete Author')
    print('4. Call it Quits')
    
    choice= input(' Enter The Choice : ')

    if choice == '1':
        name=input('Enter Author Name : ')
        add_author(name)
        print('Author added')
    elif choice == '2':
        for author in show_authors():
            print(author)
    elif choice == '3':
        name=('Enter Authors name to delete:  ')
        delete3_author(name)
    elif choice == '4':
        print('Yo!! Thats it')
        break      