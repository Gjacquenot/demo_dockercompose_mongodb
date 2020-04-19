# Demo dockercompose mongodb

![CI](https://github.com/Gjacquenot/demo_dockercompose_mongodb/workflows/CI/badge.svg?branch=master)

This repository contains a docker-compose demo with a mongodb server and a Python client.

A simple `make` command will run docker-compose with two services:

- a mongodb server with authentification
- a pymongo client that will connect to the server and add some documents to the database.

[Continuous integration](https://github.com/Gjacquenot/demo_dockercompose_mongodb/actions) is performed with GitHub actions.
A log of this continuous integration can be seen [here](https://github.com/Gjacquenot/demo_dockercompose_mongodb/runs/599371974?check_suite_focus=true).

Credits for the code can be found
[here](https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb) and 
[here](https://medium.com/faun/managing-mongodb-on-docker-with-docker-compose-26bf8a0bbae3).
