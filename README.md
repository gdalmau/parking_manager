# Parking manager
App to manage parking spots and make reservations


# Installing the requirements

1. Clone the repository:
`git clone git@github.com:gdalmau/parking_manager.git`

2. Create a virtual environment with Python 3.X (in the example Python 3.7):
```bash
sudo apt install virtualenvwrapper
mkvirtualenv parking-manager -p /usr/bin/python3.7
pip3 install .
```

# Creating the database

From the root of [manage.py](https://github.com/gdalmau/parking_manager/tree/master/parking_manager/manage.py).

`cd parking_manager`

1. Create the database

```bash
python manage.py migrate
```

2. Load the data

```bash
python manage.py loaddata parking_app/fixtures/*.json
```


# Running

Run the server with:

```bash
python manage.py runserver
```

## Docker

```bash
docker-compose up

```

# Endpoints

#### POST /api/customers/
The request body has the following content:

```json
{
    "name": "Customer name",
    "phone": "123456789"
}
```

Returns HTTP status 201 with the information of the customer created and the ID:

```json
{
    "id": 1,
    "name": "Customer name",
    "phone": "123456789",
    "created_at": "2019-01-01T10:00:00.000000Z"
}
```


#### GET /api/customers
Returns HTTP status 201 with all the customers information


#### POST /api/reservations/
Returns HTTP status 201 with the information of the reservation created:

```json
{
    "id": 2,
    "start_datetime": "2019-12-31T10:00:00Z",
    "end_datetime": "2019-12-31T12:00:00Z",
    "created_at": "2019-01-01T10:00:00.000000Z",
    "customer": 1,
    "spot": 2
}
```

#### GET /api/reservations
Returns HTTP status 201 with all the reservations information


# Improvements

- Create tests for the API and integrate with a CI tool like https://travis-ci.org/
- Integrate with Docker
- Create a simple frontend where the users can:
    - Register and login
    - Check the availability times of the parking
    - Make their own reservations
