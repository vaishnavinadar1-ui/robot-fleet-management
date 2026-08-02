# Robot Fleet Management System 

## Overview

Robot Fleet Management System is a Python-based command-line application that simulates a robot control center for managing and monitoring a fleet of robots.

The application allows users to analyze robot health, monitor sensor conditions, create missions, view assigned missions, and generate fleet reports. The project focuses on writing structured Python code, implementing business logic, and validating functionality through automated testing.

---

## Features

### Robot Health Analysis

- Checks robot operational status
- Identifies robots requiring attention
- Detects low battery conditions
- Provides health status reports

### Sensor Analysis

- Monitors sensor conditions
- Detects normal and warning sensor states
- Generates sensor analysis reports

### Mission Management

- Creates missions for available robots
- Searches robots by name
- Validates robot readiness before assigning missions
- Prevents assignment when:
  - Robot is under maintenance
  - Robot is offline
  - Battery level is critically low

### Fleet Report

Generates a summary report containing:

- Total robots
- Active robots
- Robots needing attention
- Low battery robots
- Assigned missions

---

# Testing

The project includes automated tests using **pytest**.

Test cases verify:

- Healthy robot detection
- Low battery detection
- Normal sensor conditions
- Sensor warning detection
- Fleet report generation
- Empty fleet handling

Run tests using:

```bash
pytest
