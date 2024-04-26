# Brightwheel Media Exporter
Python library to export photos and vidoes of your children from the Brightwheel daycare/preschool app.

# Installation
## Pip
```
pip install brightwheel
```

## Docker
You can build the docker container and export the images without python:
```
docker build -t brightwheel
docker run -v /local_dir/:/media:rw brightwheel "<AUTH COOKIE>" /media
```

# Authentication
This library communicates with the Brightwheel API"s via a auth cookie obtained from the browser session. To get this cookie:
1. Log into the Brightwheel website: https://schools.mybrightwheel.com
2. Open your browser developer console, navigate to the `Network` tab.
3. Select the `Fetch/XHR` request filter.
4. Click on almost any of the data requests, then the `Cookies` tab.
5. Copy the value of the `_brightwheel_v2`, that is the auth cookie.	


# Usage
Available methods:
- `get_me(...)`: Retrieves info about the current user session.
- `get_students(...)`: Gets all the students available to the current user.
- `get_activities(...)`: Retrieves one page of student activities.
- `get_all_activities(...)`: Gets all activities for a specific student.
