# vendor-catalogues

1 - Creat a venv

2 - To create a container with a container name and your password of postgres, run:

    -> docker run --name [container_name] -e POSTGRES_PASSWORD=[password] -d postgres
    
3 - To create a database run:

    -> docker exec -it [container_name] psql -U postgres
    
    -> create database db_vendor_catalogues;
    
4 - A file .env is necessary in the server directory with the variables. Parameters: 

    DB_HOST=localhost
    
    DB_NAME=db_vendor_catalogues
    
    DB_USER=postgres
    
    DB_PASSWORD=[password]
    
    HOST=0.0.0.0
    
    PORT=5000
    
5 - To build the project in a docker, run:

    -> docker build -t vendor-catalogues-api:latest .
    
    -> docker run -d -p 5000:5000 vendor-catalogues-api
    
6 - Acess the project in http://127.0.0.1:5000

7 - Swagger documentation in http://127.0.0.1:5000/ui
