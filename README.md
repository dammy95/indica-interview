# INDICA TECHNOLOGY Fullstack Developer Assessment – Damilola Olagunju

This is the repo to the Fullstack Developer Assessment for Indica Technology written in Python and using the Django web framework and Javascript using the Next.js framework.

The project uses nginx as a proxyserver and gunicorn as the WSGI server.

## Development Setup

To set up the project locally, please make sure you have [Docker](https://www.docker.com/products/docker-desktop/) installed.


1. Navigate to the project directory:

    ```bash
    cd indica-interview
    ```

2. Run the docker container:

    ```bash
    docker-compose up --build
    ```

3. Generate the test data (IMPORTANT)
    ```bash
    docker compose exec web python manage.py generate_test_data
    ```

4. Navigate to `http://localhost` to view the project


## Run unit tests

To run the unit tests for this project (make sure the docker container is already running):

```bash
    docker compose exec web pytest
```


    