# SCV Tournaments
Code sample using Python Django as backend and Vue.js as frontend

Clone project
```sh
git clone https://github.com/moltedopablo/scv_tournaments.git
```
## Quick docker install
Install docker and docker-compose 

https://docs.docker.com/get-docker

https://docs.docker.com/compose/install

Get the containers up
```sh
cd scv_tournaments
docker-compose up -d
```
Access at
```sh
http://localhost:8080
```
### Backend installation for development

Install python 3.8 and virtual env
```sh
sudo apt-get install python3.8
sudo apt-get install python3.8-venv
```
Create virtualenv
```sh
python3.8 -m venv ~/.virtualenvs/scv_tournaments
```
Activate virtualenv
```sh
source ~/.virtualenvs/scv_tournaments/bin/activate
```

Install requirements 
```sh
cd scv_tournaments/backend
pip install -r requirements.txt
```
Run migrations
```sh
python manage.py migrate
```
Run server
```sh
python manage.py runserver
```
Access at
```sh
http://localhost:8000/api
```

### Frontend installation for development
Install npm
```sh
sudo apt install npm
```
Install dependencies 
```sh
cd scv_tournaments/frontend/scv_tournaments
npm install
```
Run server
```sh
npm run serve
```
Access at
```sh
http://localhost:8080/
```