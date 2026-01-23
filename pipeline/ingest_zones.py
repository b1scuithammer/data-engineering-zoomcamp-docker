#!/usr/bin/env python
# coding: utf-8

import click
import pandas as pd
from sqlalchemy import create_engine


@click.command()
@click.option('--pg-user', default='postgres', help='PostgreSQL user')
@click.option('--pg-pass', default='postgres', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--csv-file', default='taxi_zone_lookup.csv', help='Path to CSV file')
@click.option('--target-table', default='taxi_zone_lookup', help='Target table name')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, csv_file, target_table):
    """Ingest taxi zone lookup data into PostgreSQL database."""
    
    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')
    
    # Read and ingest the CSV
    df = pd.read_csv(csv_file)
    df.to_sql(target_table, con=engine, if_exists='replace', index=False)
    
    print(f"✓ {target_table} table created successfully with {len(df)} rows")


if __name__ == '__main__':
    run()
