def main():
    # Store the robots that are currently being managed by the control center.
    robots = [
        {
            "name": "Atlas-01",
            "status": "ACTIVE",
            "battery": 87,
            "sensor_status": "NORMAL"
        },
        {
            "name": "Scout-02",
            "status": "IN_MAINTENANCE",
            "battery": 35,
            "sensor_status": "WARNING"
        },
        {
            "name": "Cargo-03",
            "status": "ACTIVE",
            "battery": 92,
            "sensor_status": "NORMAL"
        }
    ]

    # Missions are stored here while the program is running.
    missions = []

    # Keep showing the menu until the user chooses to exit.
    while True:
        print("\n=== RoboFleet Control Center ===")
        print("1. Robot health analysis")
        print("2. Sensor analysis")
        print("3. Create mission")
        print("4. View missions")
        print("5. Fleet report")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print(robot_health_analysis(robots))

        elif choice == "2":
            print(sensor_analysis(robots))

        elif choice == "3":
            create_mission(missions, robots)

        elif choice == "4":
            print(view_missions(missions))

        elif choice == "5":
            print(fleet_report(robots, missions))

        elif choice == "6":
            print("Exiting RoboFleet Control Center.")
            break

        else:
            print("Invalid choice. Please choose a number from 1 to 6.")


def robot_health_analysis(robots):
    # Check the status and battery level of each robot.
    results = []

    for robot in robots:
        if robot["status"] != "ACTIVE":
            results.append(
                f"{robot['name']}: Attention required - "
                f"status is {robot['status']}."
            )
        elif robot["battery"] < 40:
            results.append(
                f"{robot['name']}: Low battery ({robot['battery']}%)."
            )
        else:
            results.append(
                f"{robot['name']}: Healthy."
            )

    return "\n".join(results)


def sensor_analysis(robots):
    # Check whether each robot has normal or warning sensor status.
    results = []

    for robot in robots:
        if robot["sensor_status"] == "NORMAL":
            results.append(f"{robot['name']}: Sensors normal.")
        else:
            results.append(
                f"{robot['name']}: Sensor warning detected."
            )

    return "\n".join(results)


def fleet_report(robots, missions):
    # Count the current condition of the robot fleet.
    total_robots = len(robots)

    active_robots = 0
    robots_needing_attention = 0
    low_battery_robots = 0

    for robot in robots:
        if robot["status"] == "ACTIVE":
            active_robots += 1

        if robot["status"] != "ACTIVE":
            robots_needing_attention += 1

        if robot["battery"] < 40:
            low_battery_robots += 1

    # Count missions that have been assigned but not completed.
    assigned_missions = 0

    for mission in missions:
        if mission["status"] == "ASSIGNED":
            assigned_missions += 1

    return (
        "\n=== FLEET REPORT ===\n"
        f"Total robots: {total_robots}\n"
        f"Active robots: {active_robots}\n"
        f"Robots needing attention: {robots_needing_attention}\n"
        f"Low battery robots: {low_battery_robots}\n"
        f"Assigned missions: {assigned_missions}"
    )


def recommend_action(robot):
    # Decide whether the robot is ready for a new mission.
    if robot["status"] == "IN_MAINTENANCE":
        return f"{robot['name']}: Do not assign missions. Maintenance required."

    if robot["status"] == "OFFLINE":
        return f"{robot['name']}: Do not use. Robot is offline."

    if robot["battery"] < 20:
        return f"{robot['name']}: Charge immediately."

    if robot["battery"] < 40:
        return f"{robot['name']}: Charge before assigning a long mission."

    if robot["sensor_status"] == "WARNING":
        return f"{robot['name']}: Check sensors before assigning a mission."

    return f"{robot['name']}: Ready for mission assignment."


def create_mission(missions, robots):
    # Ask the user which robot should receive the mission.
    robot_name = input("Enter robot name: ").strip()

    if robot_name == "":
        print("Error: Robot name cannot be empty.")
        return

    # Find the robot without making the search case-sensitive.
    selected_robot = None

    for robot in robots:
        if robot["name"].lower() == robot_name.lower():
            selected_robot = robot
            break

    if selected_robot is None:
        print("Error: Robot not found.")
        return

    # Show a recommendation before assigning the mission.
    recommendation = recommend_action(selected_robot)
    print(recommendation)

    # Robots that are not active cannot receive a mission.
    if selected_robot["status"] != "ACTIVE":
        print("Mission cannot be assigned to this robot.")
        return

    # Prevent missions from being assigned to robots with critically low battery.
    if selected_robot["battery"] < 20:
        print("Mission cannot be assigned because the battery is too low.")
        return

    mission_type = input("Enter mission type: ").strip()

    if mission_type == "":
        print("Error: Mission type cannot be empty.")
        return

    # Create the mission and add it to the list.
    mission = {
        "robot": selected_robot["name"],
        "type": mission_type,
        "status": "ASSIGNED"
    }

    missions.append(mission)

    print("Mission created successfully.")


def view_missions(missions):
    # Display a message if no missions have been created.
    if len(missions) == 0:
        return "No missions have been created."

    results = []

    # Format each mission so it can be displayed in the menu.
    for mission in missions:
        results.append(
            f"Robot: {mission['robot']} | "
            f"Type: {mission['type']} | "
            f"Status: {mission['status']}"
        )

    return "\n".join(results)


if __name__ == "__main__":
    main()
