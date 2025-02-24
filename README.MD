# GET:

    Get all menu items:
        /restaurant/menu/

---

    Get single menu item:
        /restaurant/menu/1

---

    Get all bookings:
        /restaurant/booking/tables/
            (In the headers must provide key value pair of:
            Key: Authorization, Value: Token: your_generated_token
            )

# POST:

    Create new user:
        /auth/users/
            (Must provide info in body. example:
            {
                "name": "John",
                "email": "test@test.com",
                "password": "abc123"
            }
            )

---

    Create menu item:
        /restaurant/menu/

---

    Generate auth token:
        /auth/token/login/
            (In the body must provide info. Use this info:
            {"username": "testUser", "password":"testPassword1"}
            )

---

    Create a booking:
        /restaurant/booking/tables/
        (In the headers must provide key value pair of:
         Key: Authorization, Value: Token: your_generated_token
         In the body must provide details. example:
         {
            "name": "John",
            "no_of_guests": 2,
            "booking_date": "2025-04-26T01:17:59Z"
         }
        )
