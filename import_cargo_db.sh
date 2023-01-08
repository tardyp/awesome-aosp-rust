# simple script to automate the crates.io data import
. tosource
mkdir -p /tmp/crates.io
docker run --name pg -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD  -p 5432:5432  -v /tmp/crates.io:/tmp/crates.io -d postgres
curl https://static.crates.io/db-dump.tar.gz | tar xz -C /tmp/crates.io
docker exec pg bash -c "psql -U postgres postgres  < /tmp/crates.io/*/schema.sql"
docker exec pg bash -c "cd /tmp/crates.io/*; psql -U postgres postgres  < import.sql"
