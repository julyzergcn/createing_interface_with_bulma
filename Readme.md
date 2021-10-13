### https://bulma.io/documentation/customize/with-node-sass/

### Commands to generate this project

```sh
mkdir -p ~/src/createing_interface_with_bulma && cd $_
npm init
yarn add bulma node-sass
```

### Or commands after download

```sh
  yarn
  yarn css-build
  yarn start
```

### Install font-awesome

```sh
yarn add font-awesome
cp -r node_modules/font-awesome/fonts dist/
```

### Install Google fonts

https://www.npmjs.com/package/googlefonts-inliner

```sh
yarn add googlefonts-inliner postcss
yarn add postcss-cli
```

### Install Django

python3 -mvenv env
echo 'source env/bin/activate' > load_env.sh
. load_env.sh
pip install django
pip freeze -l > requirements.txt
django-admin.py startproject django_project
cd django_project
python manage.py migrate
python manage.py runserver
