from backend.app.agents.planning_agent import PlanningAgent


def main():
    agent = PlanningAgent()

    plan = agent.create_plan(
        "Research Redis and compare PostgreSQL"
    )

    print("\nGenerated Plan:\n")

    for task in plan:
        print(task)


if __name__ == "__main__":
    main()