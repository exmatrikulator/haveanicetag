Not a key-value, but a tag-value database.  
Store information tag based. A combination of tags will get you a value.

**For example**

"Release 1" = "working"  
"Release 1" + "Android" = "working"  
"Release 1" + "Android" + "Mobile Foo" = "not working"  
"Release 1" + "Android" + "Mobile Bar" = "not tested"  
"Release 2" = "testing"


# Install

## Linux

```
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
cp config.py.example config.py
./manage.py createdb
./manage.py runserver
```

## Windows

```
virtualenv venv -p python3
venv\Scripts\activate.bat
pip install -r requirements.txt
copy config.py.example config.py
manage.py createdb
manage.py runserver
```
