from project import robot_health_analysis
from project import sensor_analysis
from project import fleet_report


def test_robot_health_analysis():
    robots = [
        {
            "name": "TestBot",
            "status": "ACTIVE",
            "battery": 90,
            "sensor_status": "NORMAL"
        }
    ]

    result = robot_health_analysis(robots)

    assert "TestBot: Healthy." in result


def test_sensor_analysis():
    robots = [
        {
            "name": "SensorBot",
            "status": "ACTIVE",
            "battery": 80,
            "sensor_status": "NORMAL"
        }
    ]

    result = sensor_analysis(robots)

    assert "Sensors normal." in result


def test_fleet_report():
    robots = [
        {
            "name": "ReportBot",
            "status": "ACTIVE",
            "battery": 90,
            "sensor_status": "NORMAL"
        }
    ]

    missions = []

    result = fleet_report(robots, missions)

    assert "Total robots: 1" in result
    assert "Active robots: 1" in result

def test_robot_health_analysis_low_battery():
    robots = [
        {
            "name": "LowBatteryBot",
            "status": "ACTIVE",
            "battery": 15,
            "sensor_status": "NORMAL"
        }
    ]

    result = robot_health_analysis(robots)

    assert "Low battery" in result


def test_sensor_analysis_warning():
    robots = [
        {
            "name": "WarningBot",
            "status": "ACTIVE",
            "battery": 80,
            "sensor_status": "WARNING"
        }
    ]

    result = sensor_analysis(robots)

    assert "Sensor warning detected." in result


def test_fleet_report_empty_fleet():
    robots = []
    missions = []

    result = fleet_report(robots, missions)

    assert "Total robots: 0" in result
