# Demo dockercompose mongodb

![CI](https://github.com/Gjacquenot/demo_dockercompose_mongodb/workflows/CI/badge.svg?branch=master)

This repository contains a docker-compose demo with a mongodb server and a Python client.

A simple `make` command will run docker-compose with two services:

- a mongodb server with authentification
- a pymongo client that will connect to the server and add some documents to the database.
