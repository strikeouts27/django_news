Django For Beginners Reference Material:
# Describe what is going on in your own words.

# chapter 14 
Ran the start app aritcles command and than input that new app in the django_project INSTALLED_APPS = [] section.
In order to create a custom user class a Django programmer has a few choices they can us AUTH_USER_MODEL for references within a models.py file. 
Or they can use get_user_model() which is reccomended fo everywhere else such as views, tests, etc.
Once a new model is made we need to run the make migrations command and than the migrate comand. 

startapp command-> installed_apps configuration-> establish models-> make migrations-> migrate-> runserver->list_display
