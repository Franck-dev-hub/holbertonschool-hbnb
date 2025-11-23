# HB&B part 3 - Back-end
## Description
This repository constitutes the third part of the HB&B project and provides the back-end of the web app.

## Project structure
```tree
./
├── README.md
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   └── v1
│   │       ├── __init__.py
│   │       ├── amenities.py
│   │       ├── auth.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       └── users.py
│   ├── extensions.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── amenity.py
│   │   ├── base.py
│   │   ├── model.py
│   │   ├── place.py
│   │   ├── review.py
│   │   └── user.py
│   ├── persistence
│   │   ├── __init__.py
│   │   └── repository.py
│   └── services
│       ├── __init__.py
│       └── facade.py
├── config.py
├── instance
│   └── development.db
├── main.py
├── populate_db.py
├── pyproject.toml
├── requirements.txt
├── run.py
├── task 10 - Database Diagrams.png
└── tests
    ├── test_Amenity.py
    ├── test_Place.py
    ├── test_Review.py
    └── test_User.py
```
