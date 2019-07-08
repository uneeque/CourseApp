# ProjectAPI
Project link:https://github.com/uneeque/CourseApp

#CourseApp
CoursesAPI is the simple api which gives opportunity to create and check courses

##Set-up instructions 
Create a virtual environment to isolate our package dependencies locally

$ python -m venv env

$ env\Scripts\activate

$ pip install djangorestframework

$ pip install python-decouple

$ python manage.py migrate

$ python manage.py runserver 

#Data Structure

##Course

`id: 1 (int) - The ID of the course`

`name: English Language (string(char)) - The title of the course`

`description:"'improve ur skills with us'" (string(char)) - The description of the course`

`category: Language courses (string) - The category of the courses`

`logo: "'https://image.shutterstock.com/image-vector/en-logo-260nw-414474397.jpg'" (string) - Logo of the course`

`contacts (array[Contacts])`

`branches (array[Branches])`

##Contacts


`type: 1 (PHONE) - The contact type`

`value: +996551080551(number) - The contact value`

`type: 2 (FACEBOOK) - The contact type`

`value: nursultan@facebook.com (text) - The contact value`

`type: 3 (GMAIL.COM) - The contact type`

`value: bazarbaev_nu@iuca.kg (text) - The contact value`

`Course: English language (string) - The title of the course`



