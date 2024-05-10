import database.database as db
import json

def serializeJson(object) -> str:
    return json.dumps(object)

def deserializeJson(string : str) -> str:
    return json.loads(string)


CODE_200 = "200 OK"
CODE_400 = "400 Bad Request"
CODE_401 = "401 Unauthorized"
CODE_404 = "404 Not Found"
CODE_501 = "501 Not Implemented"

class API:
    """
    /user/\n
    /table/\n
    /booking/
    """

    PATHS = {
            "user":"/user/",
            "table":"/table/",
            "booking":"/booking/",
    }

    class User:
        path = "/user/"
        def add(**kwargs) -> dict:
            """ 
            Method:         POST\n
            Description:    add a new user row to database\n
            Return:         None
            """

            try:
                db.Users().createTable()
                return {'code': CODE_200, 'answer': "Success"}
            except:
                return {'code': CODE_400, 'answer': None}
       
        def get(id : int) -> str:
            """
            Method:         GET\n
            Description:    get a user row by id\n
            Return:         Serialized JSON
            """
            try:
                data = db.Users().getTable(id)
                response = dict(**data)
                return {'code': CODE_200, 'answer': data}
            except:
                return CODE_400
        
        def get() -> str:
            """
            Method:         GET\n
            Description:    get all user rows\n
            Return:         Serialized JSON
            """
            try:
                data = db.Users().getAllTables()
                response = dict(**data)
                return {'code': CODE_200, 'answer': data}
            except:
                return {'code': CODE_400, 'answer': None}

        
        def put(id, **kwargs) -> None:
            """
            Method:         PUT\n
            Description:    edit user row by id\n
            Return:         None
            """         

            try:
                db.Users().updateTable(id, **kwargs)
                return {'code': CODE_200, 'answer': "Success"}
            except:
                return {'code': CODE_400, 'answer': None}

        
        def delete(id : int) -> None:
            """
            Method:         DELETE\n
            Description:    delete user row by id\n
            Return:         None
            """
            try:
                db.Users().deleteTableByID(id)
                return {'code': CODE_200, 'answer': "Success"}
            except:
                return {'code': CODE_400, 'answer': None}
        
        def delete(ids : list[int]) -> None:
            """
            Method:         DELETE\n
            Description:    delete user rows by ids\n
            Return:         None
            """

            try:
                for i in range(len(ids)):
                    db.Users().deleteTableByID(ids[i])
                return {'code': CODE_200, 'answer': "Success"}
            except:
                return {'code': CODE_400, 'answer': None}


    class Table:
        path = "/table/"
        def add(**kwargs) -> None:
            """ 
            Method:         POST\n
            Description:    add a new table row to database\n
            Return:         None
            """
            try:
                db.Tables().createTable(**kwargs)
                return {'code': CODE_200, 'answer': "Success"}
            except:
                return {'code': CODE_400, 'answer': None}
       
        def get(id : int) -> str:
            """
            Method:         GET\n
            Description:    get a table row by id\n
            Return:         Serialized JSON
            """

            try:
                data = db.Tables().getTable(id)
                response = dict(**data)
                return {'code': CODE_200, 'answer': data}
            except:
                return {'code': CODE_400, 'answer': None}
        
        def get() -> str:
            """
            Method:         GET\n
            Description:    get all table rows\n
            Return:         Serialized JSON
            """

            try:
                data = db.Tables().getAllTables()
                
                return {'code': CODE_200, 'answer': data}
            except:
                return {'code': CODE_400, 'answer': None}
        
        def put(id, **kwargs) -> None:
            """
            Method:         PUT\n
            Description:    edit table row by id\n
            Return:         None
            """         
            try:
                db.Tables().updateTable(id, **kwargs)
                return {'code': CODE_200, 'answer': "Success"}
            except:
                return {'code': CODE_400, 'answer': None}
        
        def delete(id : int) -> None:
            """
            Method:         DELETE\n
            Description:    delete table row by id\n
            Return:         None
            """

            try:
                db.Tables().deleteTable(id)
                return {'code': CODE_200, 'answer': "Success"}
            except:
                return {'code': CODE_400, 'answer': None}
        
        def delete(ids : list[int]) -> None:
            """
            Method:         DELETE\n
            Description:    delete table rows by ids\n
            Return:         None
            """

            try:
                for i in range(len(ids)):
                    db.Tables().deleteTable(ids[i])
                return {'code': CODE_200, 'answer': "Success"}
            except:
                return {'code': CODE_400, 'answer': None}

    class Booking:
        path = "/booking/"
        def add(**kwargs) -> None:
            """ 
            Method:         POST\n
            Description:    add a new booking row to database\n
            Return:         None
            """

            try:
                db.Booking().createTable(**kwargs)
                return {'code': CODE_200, 'answer': "Success"}
            except:
                return {'code': CODE_400, 'answer': None}
       
        def get(id : int) -> str:
            """
            Method:         GET\n
            Description:    get a booking row by id\n
            Return:         Serialized JSON
            """

            try:
                data = db.Booking().getTable(id)
                return {'code': CODE_200, 'answer': data}
            except:
                return {'code': CODE_400, 'answer': None}
        
        def get() -> str:
            """
            Method:         GET\n
            Description:    get all booking rows\n
            Return:         Serialized JSON
            """
            try:
                data = db.Booking().getAllTables()
                return {'code': CODE_200, 'answer': data}
            except:
                return {'code': CODE_400, 'answer': None}
        
        def put(id, **kwargs) -> None:
            """
            Method:         PUT\n
            Description:    edit booking row by id\n
            Return:         None
            """         
            try:
                db.Booking().updateTable(id, **kwargs)
                return {'code': CODE_200, 'answer': "Success"}
            except:
                return {'code': CODE_400, 'answer': None}
        
        def delete(id : int) -> None:
            """
            Method:         DELETE\n
            Description:    delete booking row by id\n
            Return:         None
            """

            try:
                db.Booking().deleteTableByID(id)
                return {'code': CODE_200, 'answer': "Success"}
            except:
                return {'code': CODE_400, 'answer': None}
        
        def delete(ids : list[int]) -> None:
            """
            Method:         DELETE\n
            Description:    delete booking rows by ids\n
            Return:         None
            """

            try:
                for i in range(len(ids)):
                    db.Booking().deleteTableByID(ids[i])
                return {'code': CODE_200, 'answer': "Success"}
            except:
                return {'code': CODE_400, 'answer': None}
