# Badges

## Usage
* Follow the setup below
* Run `./manage.sh migrate`
* Run `./manage.sh test badges`
## Introduction

Sketchfab is a platform on which 3D creators can upload models and the public enjoy them. It has been doing well so far but we feel that our users could use Sketchfab even more. Maybe rewarding them for doing actions on the site could motivate them. What about badges ?

As a user, you earn a badge when you met a set of criterions. 3 examples we thought about:

* Collector: you uploaded 5 models
* Star: one of your models as been viewed more than a 100 times
* Pionneer: you have joined sketchfab more than a year ago

## Instructions

You have to implement these badges so that the tests in the "badges" application pass (`./manage.sh test badges`).

Some advices:

* You are free to use any third party library or tool
* The code we provide is intentionally not perfect and may be buggy, be welcome to fix or improve it
* Don't spend too much time on this (2-3 hours top)
* Any extra badge would be great to improve our site !

## Setup

* Install docker: https://docs.docker.com/engine/installation/
* Install docker compose: https://docs.docker.com/compose/install/
* Clone this repository: `git clone https://github.com/sketchfab/badges-test.git && cd badges-test`
* Build the docker image : `./docker.sh build`
* Start the stack: `./docker.sh up`
* You server is accessible at http://locahost
* You may run a django command (shell, makemigrations, migrate...) with: `./manage.sh <command>`
