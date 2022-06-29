import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database import Author






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




# to run
# streamlit run

st.title("Books App")
st.subheader("We will use database to load and save data")