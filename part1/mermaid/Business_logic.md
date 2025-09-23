Business Logic Class Diagram

'''mermaid
classDiagram

class Base {
  +create
  +update
  +delete
  +listed
}

class User {
  +UUID IdUser
  +string first_name
  +string last_name
  +string email
  +string password
  +bool admin
}

class Place {
    +string title
    +string description
    +float price
    +list latitude
    +list longitude
    +User owner
}

class Review {
    +int rating
    +string comment
}

class Amenity {
  +string name
  +string description
}

Amenity --> Place : Part of
Place --> Amenity : Use
Review --> User
Review --> Place : Use
'''
