from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Orders(db.Model):
    __tablename__ = 'orders' #Must be defined the table name

    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    created = db.Culmn(db.String, nullable=False)
    company_id = db.Column(db.String, nullable=False)
    company_details = db.Column(JSON)
    workshop_details = db.Column(JSON)
    breakdown_location_gps = db.Column(db.String, nullable=False)
    breakdown_location_address = db.Column(db.String, nullable=False)
    breakdown_location_postal_code = db.Column(db.String, nullable=False)
    breakdown_location_city = db.Column(db.String, nullable=False)
    truck_details = db.Column(JSON)

    def __init__(self, company_id, created, company_details, workshop_details, breakdown_location_gps,):
        self.company_id = company_id
        self.created = created
        self.company_details = company_details
        self.breakdown_location_gps = breakdown_location_gps
        self.workshop_details = workshop_details

    def __repr__(self):
        return "<Name: {}, company_id: {}>".format(self.name, self.company_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAll():
        orders = Orders.query.all()
        result = []
        for order in orders:
            obj = {
                'id': order.id,
                'company_id': order.company_id,
                'name': order.name
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
