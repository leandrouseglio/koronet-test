# koronet-test

## Deploy with docker compose
    
```
$ docker-compose up -d

```
## Expected output
```
$ docker compose ps
NAME                  COMMAND                  SERVICE             STATUS              PORTS
koronet-test-web      "python3 app.py"         web                 running             0.0.0.0:8000->8000/tcp
redislabs/redismod    "redis-server --load…"   redis               running             0.0.0.0:6379->6379/tcp
```
