Descargar los fuentes, y en el archivo settings.json colocar la ruta del entorno virtual que se creará.

pipenv --python 3.10.6 #crea entorno
pipenv install -r requirements.txt
pipenv install pylint pylint-django autopep8 pycodestyle --dev
pipenv shell
python manage.py migrate
python manage.py createsuperuser #crear el usuario sa, sa@sa.com, sa para la conexión a base de datos.
python manage.py showmigrations
pipenv run syshacienda
