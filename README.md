
# Server Challenge

This is my work for the PennLabs 2018 server challenge. I built it in Python using the Django framework. The requirements are contained in `requirements.txt`.  The code for steps 1-9 of the server challenge are contained in the `challenge` directory, and my implementation of step 10 is in `fun.py`.

`/challenge/challenge`  contains boilerplate Django code. `/challenge/templates` contains some html templates I used for the front end. `/challenge/clubs` includes most of the implementation of the club review features. The implementation of the user object (step 2) is in `/challenge/clubs/models.py`, and I used Django's user object to help implement the user object and user authentication. I had some difficulty implementing the behavior for `POST` requests, so that information can be provided to the server through forms. I implemented these forms and a basic front end for step 9. 

Let me know if you have any questions!