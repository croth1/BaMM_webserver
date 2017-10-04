
# Starting the webserver

## Preparing the database directories on the host

All persistent data will be stored on the host. I am using the directory `/var/webserver`. Make sure to choose a folder in which your BaMM user account has read/write access.

```bash
WEBSERVER_DIR=/var/webserver
# create folder structure
mkdir -p $WEBSERVER_DIR/{media_db/logs,mysql_db,redis_db}

cd $WEBSERVER_DIR
git clone git@github.com:soedinglab/BaMM_webserver.git
cd  BaMM_webserver
git checkout make_startup_work
git pull origin make_startup_work
git submodule update --init --recursive
```

## Setting the environment variables for docker-compose
Move to a folder of your choice and clone the webserver again.

```bash
cd ~/git_repositories
git clone git@github.com:soedinglab/BaMM_webserver.git
cd BaMM_webserver
git submodule update --init --recursive
cp .env_template .env
```

open `.env` with an editor of your choice and set the variables:

```
BAMM_USER_UID=1000

MYSQL_PASSWORD=3aMM!mot1f
MYSQL_ROOT_PASSWORD=3aMM!mot1f
NETWORK_PREFIX=172.12.12


WEBSERVER_DIR=/var/webserver/BaMM_webserver
MYSQL_DB_DIR=/var/webserver/mysql_db
REDIS_DB_DIR=/var/webserver/redis_db
MEDIA_DIR=/var/webserver/media_db
```

Make sure `BAMM_USER_UID` matches the UID of your user account. You can find your UID by executing `echo $UID` in the shell.

## Building and starting the webserver
Now use `docker-compose build` to download and build all docker images.

After successfully building the webserver, use `docker-compose up` to start the webserver. In case you see errors related to mysql stop the server by `ctrl-C` and let is shut down gracefully and restart with `docker-compose up`. The error should be gone.

## Profit

Now you should be able to access the webserver at  `0.0.0.0:10080` in your favorite browser.

## Noteworthy things

* The webserver code inside the container is in `$WEBSERVER_DIR/BaMM_webserver`. Changes to that code should be automatically be available in the server. The webserver has to be started from `~/git_repositories/BaMM_webserver` however.
* All files created by the webserver are accessible on the host in `$WEBSERVER_DIR/media_db`
