import api 
import enums

def routeToAPI(method : str, path : str, **kwargs):
    db : api.API.User | api.API.Table | api.API.Booking
    _id = 0
    _phone : str | int = None
    _path = ""
    if "/" in path:
        _splited = path.split('/')
        _path = _splited[1]
        if len(_splited) > 2 and _splited[2] != '':
            if _path == 'user-find':
                _phone = _splited[2].replace(' ', '')
                _phone = _splited[2].replace('(', '')
                _phone = _splited[2].replace(')', '')
                _phone = _splited[2].replace('-', '')
                _phone = _splited[2].replace('_', '')
                _phone = int(_splited[2].replace('+', ''))
            else:
                _id = _splited[2]

    try:
        match _path:
            case "table":
                db = api.API.Table
            case "user":
                db = api.API.User
            case "user-find":
                db = api.API.User
            case "booking":
                db = api.API.Booking
            case "booked-dates":
                db = api.API.Booking
    except:
        return {"code":enums.CODE_404, "answer": "Bad path"}



    match method:
                case "GET":
                    if _path == "user-find" and _phone != None:
                        return db.find(_phone)
                    elif _path == "booked-dates":
                        return db.getBookedDates()
                    if _id == 0:
                        return db.get()
                    else:
                        return db.get(id=_id)
                case "POST":
                    if _id != 0:
                        return {"code":enums.CODE_404, "answer": None}
                    else:
                        return db.add(**kwargs)
                case "DELETE":
                    if _id == 0:
                        return {"code":enums.CODE_404, "answer": None}
                    else:
                        return db.delete(id=_id)
                case "PUT":
                    if _id == 0:
                        return {"code":enums.CODE_404, "answer": None}
                    else:
                        return db.put(id=_id, **kwargs)


        