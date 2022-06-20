import streamlit as st
from zipfile import ZipFile
def changeFileName(file_name,lang):
    avant=file_name.split(".")[0]
    apre=file_name.split(".")[1]
    new_name=avant+"_"+lang+"."+apre 
    return new_name


# here the title
st.title("Welcome")

# here list of uploaded file
files = st.file_uploader("Choose files", accept_multiple_files=True)

# list languages
list_lang=st.text_input("Insert Lang").split(" ")

# zip file
myZip=ZipFile("list_files.zip",'w')

for file in files:
    for lang in list_lang:
        name=changeFileName(file.name,lang)
        myZip.writestr(name, file.getvalue())

myZip.close()

with open("list_files.zip","rb") as f:
    st.download_button('Donwload Me',f,file_name="myArc.zip")

if st.button('CLEAR'):
    del files
    myZip=ZipFile("list_files.zip",'w')
    myZip.close()
