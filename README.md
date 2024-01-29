         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 
 

simple deploymnent

http://eb-cloud-ninja-dev.us-west-2.elasticbeanstalk.com/

https://github.com/data5570/django-eb-starter/tree/master


multiple apps deployment

http://eb-cloud-ninja-multiple-apps.eba-f8zid3hg.us-west-2.elasticbeanstalk.com/users/hello/

https://github.com/data5570/django-eb-starter/tree/multiple-apps


git init

git clone https://github.com/data5570/django-eb-starter

cd django-eb-starter

pip3 install -r requirements.txt

python manage.py makemigrations

python manage.py migrate


eb create eb-cloud-ninja-dev

eb create eb-cloud-ninja-multiple-apps

eb deploy eb-cloud-ninja-dev

eb deploy eb-cloud-ninja-multiple-apps

eb status eb-cloud-ninja-dev

eb status eb-cloud-ninja-multiple-apps


if when running `python3 manage.py runserver` if the cloud9 console does not provide you with a proxy url then? run it like this `python3 manage.py runserver 0.0.0.0:8080`

if your eb deploy stops working then do a new `eb create eb-cloud-ninja-something-else`

todo: start from example like https://github.com/redianmarku/Django-Twitter-Clone

todo: make it so when check-in it automatically runs `eb deploy` for corresponding branch using git actions