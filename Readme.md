## About
This is a django project which gives out the diagnosed diseases provided the symptoms. The data is from apimedic api.
### Installation
Install the application using the following command-line instructions.(python version-3+, django version-1.9)
```sh
$ git clone https://github.com/elpsycongroo-kira/innovaccer_hackercamp.git
$ python manage.py migrate
$ python manage.py createsuperuser
```
Change the address of the template directory in settings.py of hackercamp folder, from '/home/coglab/Desktop' to your local directory where the project is installed.
Finally run
```sh
$ python manage.py runserver
```
Open '127.0.0.1:8000/symptoms/' in your browser. To know the changes in your database, go to '127.0.0.1:8000/admin/'


### Input format

In the Enter your symptoms.. text box in '127.0.0.1:8000/symptoms/' a comma seperated input of your symptoms should be given. For ex:-cough,sneezing or fever,cough e.t.c. The input is case-insensitive but they should be from the symptoms in https://apimedic.com/apitest and a sandbox trial account.

### What I have done 
I have taken input symptoms from the user and got the diseases data from apimedic api through my sandbox trial account. I have saved this data in the sqlite3 database so that it can directly be used from database, not from api. If more than one symptom is given, I have taken the diagnosed diseases from both the symptoms and took the common diseases out of them.

### TODOS in future
- To suggest me the nearest doctors whom I can visit given my location to them.
- The text-box takes a text like “I’m having a back pain”, and extracts symptoms and based on those symptoms returns the medical conditions.(I could do this by using information retrieval and extraction techniques,it takes some time first to create index file from apimedic data)
