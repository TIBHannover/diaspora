con=$(sudo docker ps -a --format '{{.ID}}')
for c in $con
do
h=$(docker inspect -f '{{.State.Status}}' $c)
h1="running"
if [ "$h" != "$h1" ]
then
   echo "container not runnning"
   exit 1
else
   echo "running"
fi
done
docker compose build
dokcer compose stop
docker compose up -d
