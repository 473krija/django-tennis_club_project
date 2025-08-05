# django-tennis_club_project
A beginner-friendly Django project to practice web development using Django.


A beginner-friendly Django project to practice web development using Django. Starting with the installation of Django using the pip command in the command prompt. Creating a virtual environment in the django interface for proceeding with a project. Created a new project named my_tennis_club: django-admin startproject my_tennis_club Navigated to the project directory and started the development server: python manage.py runserver

Creating a Django App: Navigated to the project directory and created an app named members: python manage.py startapp members Creating Views Updated the default code in members/views.py to display "Hello World!" on the web page.

Creating App-Level URLs: Created a new file urls.py inside the members folder. Added URL patterns and imported the path function. Root URL Routing Modified my_tennis_club/urls.py (root project URL file) to include members.urls.

Creating Templates: Created a templates folder inside the members app. Added an HTML file for the front-end view. Updated views.py to use Django’s loader to render the template.

Registering App Modified settings.py in the my_tennis_club project folder: Added 'members' to the INSTALLED_APPS list.

Running the Template: Restarted the server to confirm that the HTML template was rendered successfully. Working with Models: Opened models.py in the members app. Created a model Member with fields like firstname, lastname, etc.

Making Migrations: Created migration files for the model: python manage.py makemigrations members Applied the migration to create the actual table in the database: python manage.py migrate

Inserting Data into the Table: Opened the Django shell: python manage.py shell Inserted data into the Member table and used: Member.objects.all()

Creating the admin page: For this run the server in the command prompt using the command: python manage.py runserver In the webpage open 127.0.0.1:8000/admin/ page for the django administration page.

Creating the user and password for the admin page: In the command prompt type python manage.py createsuperuser It asks for username,email address, and the password when entered it log in into the administration page. In the admin webpage login with the username and the password and there you can see the the groups and users table.

Including MemberModel in the admin page: For this open the admin.py file and add the code which imports the Member(class) from the models Also add the code admin.site.register(Member)

set list display Changes: This doen to display the members name instead of member1,member2 etc. For this there are two ways: First change the string representation in the Member model using str() The second method is set the list_display property of the member admin class. For this open the admin.py in the model, there create a memberadmin() class and specify the lsit_display tuple. This shows the name in the admin page correctly.

Checking the code using the pylint function: Install the pylint function using pip install pylint in the command prompt and check the code files for the rateings.

Connecting to the database MySQL: By default the when the model is created it is added to the database that is sqlite for changing thed database to other change the settings.py file in the project folder. For this first install mysql using pip install mysqlclient in the command prompt and then create database according to the project.

Working with Foriegn Key: Creating models using foreign key and executing it. Using of the models.CASCADE with the on_delete field in the foreign key.

Creating another app to use foriegn key to connect tables from differnt app: Creating another app called sports in the same project folder and using foriegn key to connect it to the tables in the members app.

Creating templates for the models in the sports app and entering it in the admin.py file and adding it to the main template page so that it can be seen in the main browser and in the django default admin browser.

Run the server to see the final page: in the command prompt enter python manage.py runserver, and open the browser to see the results. Start the development server /127.0.0.1:8000/admin/ to see the final results. 
