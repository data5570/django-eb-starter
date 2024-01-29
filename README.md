         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


git init

git clone

python manage.py makemigrations

python manage.py migrate


eb create eb-cloud-ninja-dev

eb create eb-cloud-ninja-multiple-apps

eb deploy eb-cloud-ninja-dev

eb deploy eb-cloud-ninja-multiple-apps

eb status eb-cloud-ninja-dev

eb status eb-cloud-ninja-multiple-apps


if when running `python manage.py runserver` if the cloud9 console does not provide you with a url then restart cloud9

todo: start from example like https://github.com/redianmarku/Django-Twitter-Clone

todo: make it so when check-in it automatically runs `eb deploy`