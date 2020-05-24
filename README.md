# pdfservice

Creates pdf from json data {'title': '', 'questions': []} and celery beat is used to send pdf after 5 minutes of inactivity

create virtual environment

pip install -r requirement.txt

celery -A apps worker -l info -B
