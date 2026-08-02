# Robot Fleet Management System 🤖

## Overview

Robot Fleet Management System is a relational database project designed to manage and organize information about a fleet of robots. The system stores and tracks robot details, locations, missions, sensors, and sensor readings using a structured SQL database.

This project demonstrates database design skills, SQL programming, relational database concepts, and the ability to model real-world systems through data relationships.

---

## Project Purpose

Managing a fleet of robots requires an efficient system to store and access important information such as:

- Robot details and status
- Robot locations
- Mission assignments
- Sensor information
- Sensor-generated readings

This database provides a structured way to organize this information while maintaining data consistency and relationships between different entities.

---

# Features

- Store robot information
- Track robot locations
- Manage robot missions
- Store sensor details
- Record sensor readings
- Retrieve information using SQL queries
- Maintain relationships using primary keys and foreign keys
- Organize complex data using relational database principles

---

# Database Design

The database is built using a relational model with the following entities:

## Robots

Stores information about each robot.

**Includes:**
- Robot ID
- Robot name
- Model
- Status
- Battery level
- Location ID

---

## Locations

Stores information about where robots are located.

**Includes:**
- Location ID
- Location name
- Coordinates
- Area details

---

## Missions

Stores tasks assigned to robots.

**Includes:**
- Mission ID
- Mission name
- Description
- Status
- Start date
- End date

---

## Sensors

Stores sensors installed on robots.

**Includes:**
- Sensor ID
- Robot ID
- Sensor type
- Sensor status

---

## Sensor Readings

Stores data collected from sensors.

**Includes:**
- Reading ID
- Sensor ID
- Reading value
- Timestamp

---

# Entity Relationship Diagram (ERD)

The ER diagram represents the structure and relationships between database entities.

![Robot Fleet Management ER Diagram](robot-fleet-erd.png)

---

# Database Relationships

The system includes the following relationships:

- A robot can have multiple sensors.
- A robot can be assigned multiple missions.
- A location can contain multiple robots.
- A sensor can generate multiple readings.
- Primary keys uniquely identify records.
- Foreign keys maintain relationships between tables.

---

# Technologies Used

- SQL
- SQLite
- Relational Database Design
- Entity Relationship Diagrams (ERD)
- Git & GitHub

---

