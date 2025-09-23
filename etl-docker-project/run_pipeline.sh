#!/bin/bash

echo "Starting ETL pipeline..."

# Remove old containers and networks
docker-compose down --remove-orphans

# Start DB container in detached mode
docker-compose up -d db

# Waiting for DB to be Ready
echo "Waiting for database..."
until docker exec etl_db_container pg_isready -U etl_user -d etl_db -h localhost > /dev/null 2>&1; do
  sleep 2
done
echo "Database is ready!"

# Build ETL Image 
# docker-compose build etl


# Run ETL container and build it
docker-compose run --rm --build etl

echo "ETL pipeline completed successfully"

# Keep DB running so I can inspect it in DBeaver
echo "Postgres container is still running on port 5434. You can connect now."

