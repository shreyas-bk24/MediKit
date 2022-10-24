import os.path

from MediKit import app
from MediKit.models import db, Products

if __name__ == "__main__":
    if not os.path.exists('./MediKit/medi-kit.db'):
        db.create_all()
    app.run(debug=True)
