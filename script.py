from app.models import *
from app import db

me = Usuario('rodrigo', 'rodrigondec@gmail.com', 'rodrigo123')

db.session.add(me)
db.session.commit()