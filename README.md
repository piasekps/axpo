Development environment with Docker Compose
===========================================

Using `docker-compose` one can easily build and run the whole stack for development. This includes the _web__, but also _database_.


Requirements
------------

The system should have installed:
- `docker` (release 17.09.0+)
- `docker-compose` (version 3.4+)



Start
-----

First build env using `docker-compose build`, next run `docker-compose up`.


Additional notes
----------------

#### Ports
Backend container is running on port 8085.

Backends can be accessed at localhost:8085
