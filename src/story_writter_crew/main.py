#!/usr/bin/env python
from story_writter_crew.crew import StoryCrew   

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'A story about a brave knight who saves a village from a dragon.',
    }

    try:
        StoryCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

