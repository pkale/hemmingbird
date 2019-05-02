# hemmingbird
distributed tailor system


Product Description: 
We are Hemmingbird and we want to make made to measure clothing more affordable and accessible. Hemmingbird is an online platform that connects tailors in Asia to the overseas market in the United States, where users can shop from a range of affordably priced and ethically produced made to measure clothing. 

Main Site: www.hemmingbird.co 

Instructions to installing and launching backend locally: 
1.	cd music_service/



Installing an official release with pip¶

$ python

You will get an output that shows you the version number of the installed Python similar to this;

Python 3.6.3 (default, Oct  4 2017, 06:09:15)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.37)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>

This is the recommended way to install Django.
1.	Install pip. The easiest is to use the standalone pip installer. If your distribution already has pip installed, you might need to update it if it’s outdated. If it’s outdated, you’ll know because installation won’t work.
2.	Take a look at virtualenv and virtualenvwrapper. These tools provide isolated Python environments, which are more practical than installing packages systemwide. They also allow installing packages without administrator privileges. The contributing tutorial walks through how to create a virtualenv.
3.	After you’ve created and activated a virtual environment, enter the command:
/ 
$ pip install Django

After installing django, go ahead and install djangorestframework in the virtual environment you created earlier.

pip install djangorestframework

Inside hemming bird api  folder: 

python manage.py makemigrations
python manage.py migrate
 python manage.py runserver
