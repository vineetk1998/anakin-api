# anakin-api
Python Django based application with ReST api exposed.

# Design Overview
* Project contains two django apps - User(Authentication) & Core(Everything else).
* Table *ProductInStore* is supposed to contain the reference to product and store it is in with it's availability and running promotion.
* Promotion is supposed to discount for now, hence should be an integer. So drop in price is equivalent to increase in promotion.


# API 
* get products
  ```
  Endpoint: <host>/api/product
  RequestMethod: GET
  QueryParams: 
    offset: integer(default=0)
    limit: integer(default=100)
  Auth: Not Required
  Response: {	
    status: True|False,
    message: Generic description of the error condition in English.
    data: [
      {
        name: string- name of product,
        brand: string- name of brand of product
      },
      {
      }
    ]
  }
  
  ```
* get retailStore for product
  ```
  Endpoint: <host>/api/retailStore
  RequestMethod: GET
  QueryParams:
    product: string
  Auth: Not Required
  Response: {	
    status: True|False,
    message: Generic description of the error condition in English.
    data: [
      {
        retailStore: string- name of retail Store,
        product: string- name of brand of product,
        promotion: string - discount value running,
        available: True|False
      },
      {
      }
    ]
  }
  ```
  
* register user
  ```
  Endpoint: <host>/api/user
  RequestMethod: POST
  Request: {
    username: string - unique,
    password: string
  }
  Response: {
    status: True|False,
    message: Generic description of the error condition in English.
  }
  
  ```


* login user
  ```
  Endpoint: <host>/api/user
  RequestMethod: POST
  Request: {
    username: string - unique,
    password: string
  }
  Response: {
    status: True|False,
    message: Generic description of the error condition in English.
  }
  ```

* update promotion
  ```
  Endpoint: <host>/api/promotion
  RequestMethod: PATCH
  Auth: Required
  Request: {
    retailStore: string,
    product: string,
    promotion: integer
  }
  Response: {
    status: True|False,
    message: Generic description of the error condition in English.
  }
  ```

* get notification
  ```
  Endpoint: <host>/ws/notification
  Response: {
    type: notification,
    message: price drop,
    data: {
      retailStore: string- name of retail Store,
      product: string- name of brand of product,
      promotion: string - discount value running,
      available: True|False
     }
  ```

## Run Locally
Prerequisite: docker
```bash
docker run -p 8000:8000 vineetk199998/anakin-api:latest
```
You can access api hosted on [localhost:8000/api](localhost:8000/api)

## Development

### Get Started
``` bash
git clone https://github.com/vineetk1998/anakin-api.git
cd anakin-api
python3.7 -m venv env     # install python3.7 based virtual environment
source env/bin/activate   # activate virtual environment
pip -i requirements.txt
python manage.py loaddata seeddata.json
gunicorn app.asgi:application -k uvicorn.workers.UvicornWorker 
```

### To migrate db changes
```bash
cd anakin-api
python manage.py makemigrations
python manage.py migrate
```

## Build Image
```bash
cd anakin-api
docker build -t anakin-api:latest .
```

## Problem Description
``` txt
Imagine that you are to create a website for brands, where they monitor the prices across the retailers who sell their products. Imagine that in your ecosystem there are 4 brands and 4 retailers.
At a minimum, the website is expected to have the following features -
Ability to view all the products across all the retailers
Ability to check all retail stores (imagine every retailer has only one store as of now) in which a product is being sold, along with the promotions run on it, and the stores where it is not available
User Sign up and login 
Ability to run a promotion on a product in a retailer store. 
Get alert when the price of a product decreases in any store - Any Brand?
```
