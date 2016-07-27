Install:
```
sudo apt-get install python-dev libjpeg-dev zlib1g-dev libpng12-dev libxml2-dev libxslt-dev python-virtualenv python-pip git openjdk-7-jre

virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
cp config.py.example config.py
./manage.py createdb
./manage.py runserver


virtualenv venv -p python3
venv\Scripts\activate.bat
pip install -r requirements.txt
copy config.py.example config.py
manage.py createdb
manage.py runserver

```
