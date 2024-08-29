import sys
from crew import SoftwareEngineeringCrew


def run(inputs):
    """
    Run the crew.
    """
    results = SoftwareEngineeringCrew().crew().kickoff(inputs=inputs)
    return results


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "idea": "A Website that saves user information for a ticket purchase for a football game"
    }
    try:
        SoftwareEngineeringCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SoftwareEngineeringCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "idea": "A Website that saves user information for a ticket purchase for a football game"
    }
    try:
        SoftwareEngineeringCrew().crew().test(n_iterations=int(sys.argv[1]),
                                              openai_model_name=sys.argv[2],
                                              inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
