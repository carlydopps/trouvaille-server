# Trouvaille

A platform for travelers to discover and share personal adventures for those who want to take the road less traveled
<br />
<br />
## Application Overview

Trouvaille enables travelers to discover, create, and share personal adventures with each other. It can be difficult to find rare experiences in new places, which often leads to visiting tourist traps instead. The goal of Trouvaille is to make those personal experiences more accessible among fellow travelers and, in turn, create a trip full of “hidden gems” and unique adventures. An added goal is to build connections with other travelers and to make trips more meaningful by filling them with places recommended from someone they know or now follow.
<br />
<br />
## Technologies Used
[![My Skills](https://skills.thijs.gg/icons?i=js,py,react,django,html,css,git)](https://skills.thijs.gg)
<br />
<br />

## Features

- Users can login and register with a username and password
- Users can create and edit their profiles
- Users can create, view, edit, and delete trips
- Users can create, view, edit, and delete experiences
- Users can view, filter, and search for trips, destinations, and experiences
- Users can comment on and favorite trips
- Users can follow other users

## Running This Application

### Server Side
1. Clone the repository and change directories in the terminal

```
git clone git@github.com:carlydopps/trouvaille-server.git
cd trouvaille-server
```

2. Initialize virtual environment

```
pipenv shell
```

3. Start Django shell
```
python manage.py shell
```

### Client Side
[Frontend Repo](https://github.com/carlydopps/trouvaille)
1. Clone the frontend repository and change directories in the terminal

```
git clone git@github.com:carlydopps/trouvaille.git
cd trouvaille-client
```

2. Start server

```
npm install --save react-router-dom
npm start
```

## Demo Login

To view the application as a current traveler, please log in with the following:
- username: sam
- password: test

You can also register as a new user by clicking the 'Register' link in the top, right-hand corner.
<br />
<br />


## ERD
![ERD](https://res.cloudinary.com/dupram4w7/image/upload/v1673294937/Trouvaille/Screen_Shot_2023-01-09_at_2.06.34_PM_pobfrp.png)
