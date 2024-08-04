$env:PGPASSWORD = $env:DB_POSTGRESQL_PWD;
psql --host=localhost --port=5432 --username=$env:DB_POSTGRESQL_USER -d mydb_example
$env:PGPASSWORD = "";