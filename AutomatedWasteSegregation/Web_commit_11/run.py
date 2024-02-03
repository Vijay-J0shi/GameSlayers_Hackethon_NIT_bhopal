
from flashblog import app,db
from flashblog.models import *

if __name__ == "__main__":  # used to run directly python module
    app.run(debug=True)
    with app.app_context():
        db.create_all()
       
         # Create tables based on the models
       






# print(User.query.first())
