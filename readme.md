# to ACtivate the virtual environment

source venv/bin/activate

# to install requirement.txt

pip install -r requirements.txt


#to run the project

python manage.py runserver


# admin user
username: admin
password : admin@123

# registered user

username: anurag
password : anurag123


# to test the APIs of whole project

python manage.py test


# APIs

1. To register a user

http://127.0.0.1:8000/account/register/

2. Login for a user

http://127.0.0.1:8000/account/login/

3. Logout

http://127.0.0.1:8000/account/logout/

3. to create Categosry (for Authenticated user )

http://127.0.0.1:8000/ebook/category/

4. to view the list of category ( for Authenticated user )

http://127.0.0.1:8000/ebook/categorylist/

5. to update and delete category ( for Authenticated user )

http://127.0.0.1:8000/ebook/category/{ id of the category }/

6. To create a ebook( for authenticated user)

http://127.0.0.1:8000/ebook/

7. to view the list of ebook( for authenticated user)

http://127.0.0.1:8000/ebook/list

8. to view the ebook individually( for authenticated user)

http://127.0.0.1:8000/ebook/list/{ id of the ebook }

9. to update the ebook( for created user only )

http://127.0.0.1:8000/ebook/update/ebook/{id of the Ebook }/

10. to delete the ebook( for created user only)

http://127.0.0.1:8000/ebook/delete/{id of the Ebook }/

11. to rate for a Ebook

http://127.0.0.1:8000/ebook/{id of the Ebook }/rate

12. to update ,delete review( for corresponding review user)

http://127.0.0.1:8000/ebook/rating/3/
