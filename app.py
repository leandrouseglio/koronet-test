from flask import Flask
from redis import Redis
import pymysql

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

REDIS_HOST = "redis"
REDIS_PORT = 6379

@app.route('/')
def hello():
    return 'Hi Koronet Team\n'

@app.route('/redis')
def get_redis_client():
    try:
        redis.incr('hits')
        counter = str(redis.get('hits'),'utf-8')
        return "This webpage has been viewed "+counter+" time(s)"
    except redis.ConnectionError as e:
        return "Could not connect to Redis\n"
    
@app.route('/mysql')
def get_mysql_client():
    try:
        conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql')
        cur = conn.cursor()
        cur.execute("SELECT Host,User FROM user")
        for r in cur:
            print(r)
        cur.close()
        conn.close()
    except pymysql.err.OperationalError as e:
        return "Could not connect to MySQL\n"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)