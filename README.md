echo "# python_django_receipe" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/dilipdivate/python_django_receipe.git
git push -u origin main

Create Docker secret token and store in GITHUB secret

Create requirements.txt and dev file

run -- docker build .
run -- docker-compose build
docker-compose run --rm app sh -c "flake8"
docker-compose run --rm app sh -c "django-admin startproject app ."
docker-compose up

Open http://127.0.0.1:8000/ in browser

<!-- To Test -->

docker-compose run --rm app sh -c "python manage.py test"
docker-compose run --rm app sh -c "python manage.py wait_for_db"

<!-- To run core app -->

docker-compose run --rm app sh -c "python manage.py startapp core"

docker-compose run --rm app sh -c "python manage.py makemigrations"
