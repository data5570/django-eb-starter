# Elastic Beanstalk Deployment Guide 🚀

---

### Simple Deployment

- **EB Environment Base URL**: [eb-cloud-ninja-dev.us-west-2.elasticbeanstalk.com](http://eb-cloud-ninja-dev.us-west-2.elasticbeanstalk.com/)
- **Source Code**: [Django EB Starter - Master Branch](https://github.com/data5570/django-eb-starter/tree/master)

### Multiple Apps Deployment

- **EB Environment Base URL**: [eb-cloud-ninja-multiple-apps.eba-f8zid3hg.us-west-2.elasticbeanstalk.com/](http://eb-cloud-ninja-multiple-apps.eba-f8zid3hg.us-west-2.elasticbeanstalk.com/)
- **EB Environment Users URL**: [eb-cloud-ninja-multiple-apps.eba-f8zid3hg.us-west-2.elasticbeanstalk.com/users/hello/](http://eb-cloud-ninja-multiple-apps.eba-f8zid3hg.us-west-2.elasticbeanstalk.com/users/hello/)
- **Source Code**: [Django EB Starter - Multiple Apps Branch](https://github.com/data5570/django-eb-starter/tree/multiple-apps)

---

## Initial Setup

```bash
git clone https://github.com/data5570/django-eb-starter
cd django-eb-starter
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8080
```

## Deployment Commands
```bash
eb create eb-cloud-ninja-dev

eb create eb-cloud-ninja-multiple-apps

eb deploy eb-cloud-ninja-dev

eb deploy eb-cloud-ninja-multiple-apps

eb status eb-cloud-ninja-dev

eb status eb-cloud-ninja-multiple-apps
```

## Troubleshooting


**Issue**: Cloud9 doesn't provide a proxy URL when running python3 manage.py runserver.

**Solution**: Use `python3 manage.py runserver 0.0.0.0:8080`


**Issue**: `eb deploy` stops working.

**Solution**: Create a new environment with `eb create eb-cloud-ninja-something-else`

## Todos

todo: start from example like https://github.com/redianmarku/Django-Twitter-Clone but maybe find an even better one that works fully

todo: make it so when check-in it automatically runs `eb deploy` for corresponding branch using git actions