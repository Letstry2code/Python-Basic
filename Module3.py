import os
# os.mkdir('Data analysis')
if not os.path.exists('Data analysis'): 
    os.mkdir('Data analysis')


print('The Current Location  is ')
print(os.getcwd())
print('The current directory content')
content=os.listdir()
print(content)

if os.path.isdir('data analysis'):
    print('data analysis is a directory')



if os.path.isfile('data analysis'):
    print('data analysis is a file')
print('size of pic',os.path.getsize('Module2.py')/(1024*1024),'MB')
    