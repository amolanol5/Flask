from flask import Flask
import socket

app = Flask(__name__)

#variables  
ip = "google.com"
port = 80


#check availability port
def isOpen(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False

#validation
if isOpen(ip,port):
    var1 = "ok"
else:
    var1 = "fail"
            
#routes
@app.route("/")
def index():
    return var1

#routes
@app.route("/status")
def status():
    return var1


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")