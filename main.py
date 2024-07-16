from app import app,db
from app import routers
from app.models.base import BaseModel

BaseModel.set_session(db.session)

if __name__ == '__main__':
    app.run()