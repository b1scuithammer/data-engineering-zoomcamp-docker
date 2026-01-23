# data-engineering-zoomcamp-docker

# docker ingestion
docker run -it \
  --network=pipeline_default \
  taxi_ingest:v001 \
    --pg-user=postgres \
    --pg-pass=postgres \
    --pg-host=db \
    --pg-port=5432 \
    --pg-db=ny_taxi \
    --target-table=green_taxi_trips

# Q1
docker run --rm python:3.13 pip --version

# Q3
select count(*) from green_taxi_trips
where lpep_pickup_datetime between '2025-11-01' and '2025-12-01'
and trip_distance <=1;

# Q4
select trip_distance,lpep_pickup_datetime  from green_taxi_trips
where trip_distance < 100
order by trip_distance desc;

# Q5
select sum(g.total_amount) a, z1."Zone" from green_taxi_trips g, taxi_zone_lookup z1
where g."PULocationID" = z1."LocationID"
group by g."PULocationID", z1."Zone"
order by a desc;

# Q6
select max(g.tip_AMOUNT) a, z2."Zone" from green_taxi_trips g, taxi_zone_lookup z1, taxi_zone_lookup z2
where g."PULocationID" = z1."LocationID"
and g."DOLocationID" = z2."LocationID"
and z1."Zone" = 'East Harlem North'
group by g."DOLocationID", z2."Zone"
order by a desc;