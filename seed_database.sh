rm db.sqlite3
rm -rf ./trouvailleapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations trouvailleapi
python3 manage.py migrate trouvailleapi
python3 manage.py loaddata destinations
python3 manage.py loaddata durations
python3 manage.py loaddata experience_types
python3 manage.py loaddata experiences
python3 manage.py loaddata seasons
python3 manage.py loaddata styles
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata travelers
python3 manage.py loaddata subscriptions
python3 manage.py loaddata trips
python3 manage.py loaddata trip_destinations
python3 manage.py loaddata trip_experiences