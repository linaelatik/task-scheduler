class Task:
    """
    Class used in defining tasks.

    Attributes
    ----------
    id (int): The identifier for the task.
    description (str): Description of the task.
    start_time (int): Start time of the task in minutes.
    duration (int): Duration of the task in minutes.
    dependencies (list): List of task dependencies.
    status (str): Current status of the task.
    has_time_constraint (bool): Flag indicating whether the task has a time constraint.
    """
   
    def __init__(self, id, description, start_time, duration, dependencies, preference, status="N"):
     
        self.id = id
        self.description = description
        self.duration = duration
        self.dependencies = dependencies
        self.status = status
        self.start_time= start_time * 60
        self.has_time_constraint = isinstance(start_time, int)
        self.preference = preference