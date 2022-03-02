from bottle import default_app, run, error, get, view, post
import jwt
import time

####################
@get("/")
@view("index")
def _():
    return

@post("/send_jwt")
def _():
    cpr = "12345"
    iat = int(time.time())
    exp = iat + 600
    encoded_jwt = jwt.encode({"cpr":cpr, "iat": iat, "exp": exp}, "secret", algorithm="HS256")
    return encoded_jwt

####################
#decorator
@error(404)
def _(error):
    print(error) # terminal only.. for developer
    print(dir(error))
    return "Uppps... page not found"

####################
#create webserver and giv it host, port and set debug to true
#reloader sørger for den selv reloader når man ændre noget
# run should be the last line
try:
    # server AWS (production)
    import production
    application = default_app()
except:
    # Local machine (development)
    run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")