# Brightwheel Media Exporter
Python library to export photos and vidoes of your children from the Brightwheel daycare/preschool app.

# Authentication
This library communicates with the Brightwheel API"s via a auth cookie obtained from the browser session. To get this cookie:
1. Log into the Brightwheel website: https://schools.mybrightwheel.com
2. Open your browser developer console, navigate to the `Network` tab.
3. Select the `Fetch/XHR` request filter.
4. Click on almost any of the data requests, then the `Cookies` tab.
5. Copy the value of the `_brightwheel_v2`, that is the auth cookie.	

# Installation
If you want to build a custom tool from the library you can install the code via pip. If you just want to download your kids photos, then you can use the bundled export script or docker container.

## Pip
```
pip install brightwheel
```

## Export Script
Poetry is the preferred method to use install the export script.
```
>> poetry install
>> brightwheel-export --help
```

If you don't want to use Poetry:
```
>> python brightwheel\export.py --help
```

## Docker
You can build the docker container and export the images without python:
```
docker build -t brightwheel
docker run -v /local_dir/:/media:rw brightwheel "<AUTH COOKIE>" /media
```

# Library Usage
Available methods:
- `get_me(...)`: Retrieves info about the current user session.
- `get_students(...)`: Gets all the students available to the current user.
- `get_activities(...)`: Retrieves one page of student activities.
- `get_all_activities(...)`: Gets all activities for a specific student.
