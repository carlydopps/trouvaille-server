# Trouvaille (Backend)

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
1. Clone the [frontend repository](https://github.com/carlydopps/trouvaille) and change directories in the terminal

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
