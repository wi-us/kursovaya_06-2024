import api 
import enums

def routeToAPI(method : str, path : str, **kwargs):
    db : api.API.User | api.API.Table | api.API.Booking

    try:
        match path:
            case "table":
                db = api.API.Table
            case "user":
                db = api.API.User
            case "booking":
                db = api.API.Booking
    except:
        return "Bad path"

    _id = 0
    _path = ""
    if "/" in path:
        _splited = path.split('/')
        _path = _splited[0]
        _id = _splited[2]

    match method:
                case "GET":
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


        