# Inventory backend app

A project for Shopify internship - basic CRUD backend app.

## Stack

Django, sqlite3, Bootstrap

## Demo

Link: *repl.it add link here*

## Endpoints

'/' - Inventory list  
'/item/n/' - item detail -  edit or delete item here  
'/create/' - a form to add item to the inventory  
'/location_list/' - add or remove warehouse/storage locations for inventory items.  

## Files

shopify_tt/ - Django project folder  
requirements.txt - dependancies  
readme.md - this file  

Main Django files:  
    - inventory/models.py  
    - inventory/views.py  
    - inventory/urls.py  
    - inventory/templates/ - HTML templates for the app  

## Installation

Copy files from repository  
Install dependancies from requirements.txt  
Create .env file with 'SECRET_KEY=valuehere' key  
python manage.py createsuperuser - create main to access Django Admin panel  
python manage.py makemigrations - prepare db migrations  
python manage.py migrate - migrate the database  
python manage.py runserver - starts the development server  