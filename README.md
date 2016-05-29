# Erehwon

Erehwon is an on-line collaborative tool for connecting people involved in socio-political interventions, building communities of interest, and enabling and empowering civic engagement in socio-political activities in public spaces by sharing and exchanging methods, values and practices, beyond spatial territories and physical borders. The project was conceived by Beatriz Cantinho and Mariza Dima, and has been developed with the support of Osso Cultural Association, Queen Mary University of London, and Stress.fm.  

For more information on the project: (http://www.osso.pt/en/adrift/erehwon-3)

The prototype tool was created over a hackathon weekend on the 28th and 29th May 2016.

Developers
Front-end:
* [Liliana Castillo](https://github.com/lili2311)
* [Karen Lee](https://github.com/neraks)

Graphic Designer:
* [Marta Monge](https://github.com/emmecomemarta)

UX Design:
* [Mariza Dima](https://github.com/marizoldi)

We continue its development on a voluntarily basis and seeking new collaborations. In the next steps we are adding backend and looking at privacy-by-design. If you wish to contribute to the development and have any questions please contact [Mariza Dima](https://github.com/marizoldi).

![Wireframe](http://www.osso.pt/wp-content/uploads/2016/02/heroimage-02.jpg)

# Setup

1. Install [virtualenv](https://virtualenv.pypa.io/en/stable/): 

	```sudo pip install virtualenv```

2. Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html):

	 ```pip install virtualenvwrapper```
3. Create a new env for the project:
 
	 ```mkvirtualenv erehwon```
4. Clone the repo:

	`git@github.com:marizoldi/Erehwon.git`
	
5. Go inside the newly added **erehwon** directory:
	
	```cd erehwon```
	
6. Activate the virtual enviroment:
 
	 ```workon erehwon``` 
	 
	 This will now ensure anything you install is within this enviroment.
7. Install the requirements:

	 ```pip install -r requirements.txt``` 
5. Go inside frontend folder: 
	
	```cd frontend```
6. Install all the dependencies:

	 ```npm install```
