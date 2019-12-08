# [Tutorial](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)
[Goal Video](https://www.youtube.com/watch?v=uZgRbnIsgrA)
Skipped the 2nd part: database

## Dependencies
```
    pip install django-cors-headers
```

## Commands
### New project or apps
```
    $ django-admin startproject projectname
    $ python manage.py startapp appname
```

### Start the server
```
    $ python manage.py runserver 0:8000
```

### Modify models
```
    $ python manage.py makemigrations
    $ python manage.py migrate
```

### Create admin user
```
    # also remember to add site to admin.py file
    $ python manage.py createsuperuser
```


## Test modules in shell
```
    $ python manage.py shell
    > from product.models import Product

    > Product.objects.all()

    > Product.objects.create(title='New Product', description='a new product',
    >       price=23.32, summary='nice!', featured=True)

    >Product.objects.get(id=1)
```

## Templates
`project/templates/some\_path/\*.html` has higher priority than
`project/app/templates/some\_path/\*.html`
