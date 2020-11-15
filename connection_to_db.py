#import pymysql.cursors
from sqlalchemy import create_engine
import psycopg2

engine = create_engine("postgresql://postgres:1111@localhost/cafe")


