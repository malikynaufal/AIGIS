---
code: FKD211505
name: Basis Data
SKS: 2
semester: 5
department: Informatika
tags: [databases, SQL, data-management, experimental-data]
created: 2026-07-27
---

# FKD211505 — Basis Data

## Course Overview

Database management for physics and experimental data — this course covers relational database design, SQL, and data management best practices as applied to large-scale measurement data such as GNSS time series, gravity surveys, and geophysical data archives.

**Contact Hours:** 2 SKS (1 hour lecture + 1 hour lab per week)
**Prerequisites:** Pemrograman Lanjutan
**Co-requisites:** None

---

## 📋 Topics & Outline

### Unit 1: Relational Database Fundamentals (Weeks 1–5)

- **Database vs. flat file:** why databases scale better

- **Relational model:** Codd's rules

- **Relations, tuples, attributes, domains**

- **Keys:** primary keys, foreign keys, candidate keys

- **Entity-Relationship (ER) modeling:**
 - Entities (tables) and relationships
 - Cardinality: 1:1, 1:N, M:N
 - ER diagrams for physics data (e.g., experiment → measurements → parameters)

- **Normalization:**
 - 1NF: atomic values
 - 2NF: no partial dependencies
 - 3NF: no transitive dependencies
 - Normalization trade-offs: when to denormalize for performance

### Unit 2: SQL (Weeks 6–10)

- **DDL (Data Definition Language):**
 ```sql
 CREATE TABLE measurements (
 id SERIAL PRIMARY KEY,
 station TEXT NOT NULL,
 timestamp TIMESTAMP NOT NULL,
 x REAL,
 y REAL,
 z REAL,
 quality REAL
 );
 ```

- **DML (Data Manipulation Language):**
 ```sql
 INSERT, SELECT, UPDATE, DELETE
 ```

- **SELECT queries:** WHERE, JOIN (INNER, LEFT, RIGHT, FULL)

- **Aggregation:** COUNT, AVG, SUM, GROUP BY, HAVING

- **Subqueries and CTEs (WITH statements)**

- **Indexes:** why they speed up reads (B-tree structure)

- **Transactions and ACID properties**

### Unit 3: Database Design for Physics Data (Weeks 11–14)

- **Design patterns for science data:**
 - Station/time-series tables for GNSS observations
 - Hierarchical structure: experiment → run → measurement
 - File storage: binary large objects (BLOBs) vs. file system pointers

- **Spatial data** (PostGIS extension):
 ```sql
 CREATE TABLE stations (
 id SERIAL PRIMARY KEY,
 name TEXT,
 location GEOMETRY(Point, 4326)
 );
 ```

- **Time series databases** vs. relational for time-tagged data

- **Data quality control:** schema validation, constraint checking

### Unit 4: Data Management and Applications (Weeks 15–16)

- **Backup and recovery** strategies for research data

- **Data formats:** CSV, HDF5, NetCDF — when to use each

- **Version control for data:** using Git LFS, DVC

- **Database security:** user permissions, avoiding SQL injection

- **Efficient querying of large physics datasets** (partitioning, query optimization)

- **Practical exercise:** design a database schema for a GNSS network

- Tools: PostgreSQL, SQLite, DBeaver, Jupyter with `psycopg2`

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Design normalized relational database schemas from ER diagrams
2. Write SQL queries with joins, aggregations, and subqueries
3. Implement spatial queries using PostGIS
4. Choose appropriate data storage strategies for physics measurements
5. Ensure data integrity, quality, and backup practices
6. Connect to databases from Python and perform analysis

---

## 📚 References

1. Ramakrishnan, R. & Gehrke, J. (2003). *Database Management Systems*, 3rd ed. McGraw-Hill.
2. Elmasri, R. & Navathe, S.B. (2016). *Fundamentals of Database Systems*, 7th ed. Pearson.
3. PostGIS Documentation: https://postgis.net/documentation/
4. PostgreSQL Manual: https://www.postgresql.org/docs/
5. SQLite Documentation: https://sqlite.org/docs.html