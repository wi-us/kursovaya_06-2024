from peewee import *
import datetime

db = SqliteDatabase('Server//Orders_main.sqlite')
db.connect()

EMPTY = "NoData"
ID = "id"

class BaseModel(Model):
    class Meta:
        database = db

class Tables(BaseModel):
    guestCountMax = BigIntegerField(null=False)
    vipStatus = BooleanField(null=False)

    @classmethod
    def createTable(cls, **kwargs):
        return cls.create(**kwargs)

    @classmethod
    def deleteTable(cls, table_id):
        query = cls.delete().where(cls.id == table_id)
        query = Booking.delete().where(Booking.guest == cls)
        query.execute()

    @classmethod
    def getAllTables(cls):
        if cls.select().count() == 0:
            return EMPTY
        else:
            _arr = []
            for val in cls.select():
                _arr.append({"id": val.id, 
                             "guestCountMax": val.guestCountMax, 
                             "vipStatus": val.vipStatus})
            return _arr
    
    @classmethod
    def getValueById(cls, value):

        if cls.select().count() == 0:
            return None
        else:
            result =  cls.select(cls).order_by(cls.id.desc()).limit(1).tuples().get()
            return {"id": result.id, 
                    "guestCountMax": result.guestCountMax, 
                    "vipStatus": result.vipStatus}
            
    @classmethod
    def updateTable(cls, id, **kwargs):
        query = cls.update(**kwargs).where(cls.id == id)
        query.execute()

    @classmethod
    def getTable(cls, id):
        result = cls.select().where(cls.id == id)
        return {"id": result.id, 
                "guestCountMax": result.guestCountMax, 
                "vipStatus": result.vipStatus}

class Users(BaseModel):
    name = CharField(null=False)
    surname = CharField(null=False)
    phone = CharField(null=False)
    email = CharField(null=False)

    @classmethod
    def createTable(cls, **kwargs):
        return cls.create(**kwargs)

    @classmethod
    def deleteTableByID(cls, table_id):
        query = cls.delete().where(cls.id == table_id)
        query = Booking.delete().where(Booking.guest == cls)
        
        query.execute()

    @classmethod
    def getAllTables(cls):
        if cls.select().count() == 0:
            return EMPTY
        else:
            _arr = []
            for val in cls.select():

                    _arr.append({"id": val.id, 
                                 "name": val.name, 
                                 "surname": val.surname, 
                                 "phone": val.phone, 
                                 "email": val.email})


            return _arr
    
    @classmethod
    def getValueById(cls, value):

        if cls.select().count() == 0:
            return 0
        else:
            result = cls.select(cls).order_by(cls.id.desc()).limit(1).tuples().get()
            return {"id": result.id, 
                    "name": result.name, 
                    "surname": result.surname, 
                    "phone": result.phone, 
                    "email": result.email}
            
    @classmethod
    def updateTable(cls, id, **kwargs):
        query = cls.update(**kwargs).where(cls.id == id)
        query.execute()

    @classmethod
    def getTable(cls, id):
        result = cls.select().where(cls.id == id)
        return {"id": result.id, 
                "name": result.name, 
                "surname": result.surname, 
                "phone": result.phone, 
                "email": result.email}

class Booking(BaseModel):
    table = ForeignKeyField(Tables, backref='bookings', null=True)
    guest = ForeignKeyField(Users, backref='bookings', null=True)
    bookedDate = DateTimeField(default=datetime.datetime.now())
    guestsCount = BigIntegerField(null=False)

    @classmethod
    def createTable(cls, **kwargs):
        table = Tables.get(Tables.id == kwargs["table"].id)
        guests = Users.get(Users.id == kwargs["guest"].id)
        
        return cls.create(table=table, guest=guests, bookedDate=kwargs["bookedDate"], guestsCount=kwargs["guestsCount"])

    @classmethod
    def deleteTableByID(cls, table_id):
        cls.delete().where(cls.id == table_id)
        query = cls.delete()
        query.execute()

    @classmethod
    def getAllTables(cls):
        if cls.select().count() == 0:
            return EMPTY
        else:
            _arr = []
            for val in cls.select():
                    try:
                        _arr.append({"id": val.id, 
                                     "table": val.table, 
                                     "guestid": val.guest, 
                                     "bookedDate": val.bookedDate, 
                                     "guestsCount": val.guestsCount})
                    except:
                        cls.deleteTable(val.id)
            return _arr
    
    @classmethod
    def getValyeById(cls, value):

        if cls.select().count() == 0:
            return 0
        else:
            result = cls.select(cls).order_by(cls.id.desc()).limit(1).tuples().get()
            return {"id": result.id, 
                    "table": result.table, 
                    "guestid": result.guest, 
                    "bookedDate": result.bookedDate, 
                    "guestsCount": result.guestsCount}
            
    @classmethod
    def _updateTable(cls, *args):
        val = args[0]
        table = Tables.get(Tables.id == val[1])
        guests = Users.get(Users.id == val[2])
        query = cls.update(table=table, guest=guests, bookedDate=val[3], bookedTime=val[4], guestsCount=val[5]).where(cls.id == val[0])
        query.execute()

    @classmethod
    def updateTable(cls, id, **kwargs):
        table = Tables.get(Tables.id == kwargs["table"].id)
        guests = Users.get(Users.id == kwargs["guest"].id)
        query = cls.update(table=table, guest=guests, bookedDate=kwargs["bookedDate"], guestsCount=kwargs["guestsCount"]).where(cls.id == id)
        query.execute()
    
    @classmethod
    def getTable(cls, id):
        result = cls.select().where(cls.id == id)
        return {"id": result.id, 
                "table": result.table, 
                "guestid": result.guest, 
                "bookedDate": result.bookedDate, 
                "guestsCount": result.guestsCount}
    

Tables().create_table()
Users().create_table()
Booking().create_table()