sudo apt install python3-pip
sudo apt install python3.8-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigations
python manage.py migrate
python manage.py runserver