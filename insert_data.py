
from app import db, Property

# Dummy property data
properties = [
    Property(price=100000, location="Downtown", type="sale"),
    Property(price=2000, location="Uptown", type="rent"),
    Property(price=500000, location="Suburbs", type="sale"),
    Property(price=1500, location="City Center", type="rent")
]

# Insert the dummy data into the database
db.session.bulk_save_objects(properties)
db.session.commit()

print("Dummy data inserted successfully!")
