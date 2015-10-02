from flask_frozen import Freezer
from flask_flatpages import FlatPages
from engelhard import app

pages = FlatPages(app)

freezer = Freezer(app)

@freezer.register_generator
def profile_details():
  yield '/profiles/elmendorf/'

if __name__ == '__main__':
    freezer.freeze()