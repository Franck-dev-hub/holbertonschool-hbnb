# HB&B part 2 - basic structure
## Description
This repository constitutes the second part of the HB&B project and provides its basic structure.

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
│   │       ├── places.py
│   │       ├── reviews.py
│   │       └── users.py
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
├── main.py
├── run.py
└── tests
    ├── test_Amenity.py
    ├── test_Place.py
    ├── test_Review.py
    └── test_User.py
```
