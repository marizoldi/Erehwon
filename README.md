# Erehwon

Erehwon is an on-line collaborative tool for connecting people involved in socio-political interventions, building communities of interest, and enabling and empowering civic engagement in socio-political activities in public spaces by sharing and exchanging methods, values and practices, beyond spatial territories and physical borders. The project was conceived by Beatriz Cantinho and Mariza Dima, and the first prototype has been developed with the support of Osso Cultural Association, Queen Mary University of London, and Stress.fm.  

[Project info](http://www.osso.pt/en/adrift/erehwon-3)

The [first prototype](https://github.com/marizoldi/Erehwon) was created over a hackathon weekend on the 28th and 29th May 2016. Developers (Front-end: [Liliana Kastilio](https://github.com/lili2311), [Karen Lee](https://github.com/neraks) |
Graphic Designer:[Marta Monge](https://github.com/emmecomemarta) | UX Design:[Mariza Dima](https://github.com/marizoldi)

![Wireframe](http://www.osso.pt/wp-content/uploads/2016/02/heroimage-02.jpg)

We continue its development using Angular and Postgres on a voluntarily basis and seeking new collaborations. If you wish to contribute to the development and have any questions please contact [Mariza Dima](https://github.com/marizoldi).



## Development Setup

For a new installation of the project for Windows, using Command Prompt (including Python 2.7.9, pip, virutalenv and virtualenvwrapper installation):
see [Tim Reilly's article](http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/)
which makes the whole process, UP TO Step 7 below, really simple)


1. Install [virtualenv](https://virtualenv.pypa.io/en/stable/)

	``sudo pip install virtualenv``

2. Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html):

	 ``pip install virtualenvwrapper``

3. Create a new env for the project:

	 ``mkvirtualenv erehwon``

4. Clone the repo:

	``git@github.com:marizoldi/Erehwon.git``

5. Go inside the newly added **erehwon** directory:

	``cd erehwon``

6. Activate the virtual environment:

	 ``workon erehwon``

	 This will now ensure anything you install is within this environment.

7. Install the requirements:

	 ``pip install -r requirements.txt``

8. You will need to have [Postgres installed](https://www.postgresql.org/download/) and up and running

9. Create a database locally for the project:

	``createdb erehwon``

10. Go inside front-end folder:

	 ``cd frontend``

11. Install all the dependencies:

	 ``npm install``


## Running the project locally
1. Go inside the django app directory where the manage.py sits:

	``../Erehwon/erehwon``

2. Run django server:

	``python manage.py runserver`` or ``./manage.py runserver``

3. The project is now running on ``http://127.0.0.1:8000/`` in your browser.

## Front End changes
1. Make css and javascript changes in the ``frontend`` folder
2. Make any HTML changes in the Django templates located in ``erehwon/templates``
3. Use ``grunt default`` in the front-end folder to build, watch and copy all the required files automatically into the Django static folder.

## Deploying to Heroku
1. Create a Heroku Account
2. Get added to the app in the Heroku Dashboard
3. In the terminal ``heroku login``
4. Within you project directory ``heroku git:remote -a erehwon``
5. Once you are ready to deploy, from master branch you can run ``git push heroku master`` make sure you have committed all the changes before running this and the ``git status`` is clean.
6. Go to http://erehwon.herokuapp.com/ to view the live site.
