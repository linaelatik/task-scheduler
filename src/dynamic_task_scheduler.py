class TaskSchedulerDynamic:
    """
    Class for scheduling tasks dynamically.

    Attributes
    ----------
    tasks : list
        List of Task objects.
    priority_queue_strt : list
        Priority queue based on start time.
    heap : MaxHeapq
        Heap instance for managing task priorities.
    current_time : int
        Current simulation time.
    global_max : list
        List containing the maximum utility calculated.
    global_tasks : list
        List containing the most optimal tasks found.
    mem_dict : dict
        Dictionary for storing intermediate results during scheduling.
    available_tasks : list
        List of tasks that are currently available for scheduling.
    task_priority_values : dict
        Dictionary storing priority values for each task.
    """

    NOT_STARTED = 'N'
    IN_PRIORITY_QUEUE = 'I'
    COMPLETED = 'C'

    def __init__(self, tasks):
        """
        Initializes a new TaskScheduler object.

        Parameters
        ----------
        tasks : list
            List of Task objects.
        """
        self.tasks = tasks
        self.priority_queue_strt = []
        self.heap = MaxHeapq()
        self.current_time = 0
        self.global_max = [0]
        self.global_tasks = [{}]
        self.mem_dict = {}
        self.available_tasks = []
        self.task_priority_values = {}

    def print_task_descriptions(self):
        """
        Prints the descriptions of the tasks added to the scheduler.
        """
        print("Tasks added to the scheduler:")
        print("--------------------------------------")
        for task in self.tasks:
            print(f"➡️'{task.description}', duration = {task.duration} mins.")
            if len(task.dependencies) > 0:
                print(f"\t ⚠️ This task depends on others!")

    def remove_dependency(self, task_id):
        """
        Removes the dependency of a task with the specified ID.

        Parameters
        ----------
        task_id (int): The ID of the task whose dependency is to be removed.
        """
        for task in self.tasks:
            if task.id != task_id and task_id in task.dependencies:
                task.dependencies.remove(task_id)

    def calculate_priority(self, task_id):
        """
        Calculates the priority of a task based on its dependencies and start times.

        Parameters
        ----------
        task_id (int): The identifier for the task.

        Returns
        ----------
        int: The calculated priority for the task.
        """
        dependencies = 0
        preference = 0

        for task in self.tasks:
            if task_id in task.dependencies:
                dependencies += 10
            if task.id == task_id:
                preference = task.preference

        priority = dependencies + preference
        return priority

    def get_ready_tasks(self):
        """
        Gets tasks ready for execution based on their dependencies and inserts them
        into their correct priority queues with their priority value.
        """
        ready_tasks_prio_strt = []

        for task in self.tasks:
            if task.status == self.NOT_STARTED:
                if task.has_time_constraint: #for tasks with time constraints
                    ready_tasks_prio_strt.append(task)
                else:
                    if len(task.dependencies) == 0: #for available tasks with no time constraints
                        self.available_tasks.append(task)
                        task.status = self.IN_PRIORITY_QUEUE

        for task in ready_tasks_prio_strt:
            task.status = self.IN_PRIORITY_QUEUE
            priority = -1 * task.start_time
            self.heap.heappush(self.priority_queue_strt, (task, priority))

    def unscheduled_tasks_exist(self):
        """
        Checks if there are any unscheduled tasks.

        Returns
        ----------
        bool: True if there are unscheduled tasks, False otherwise.
        """
        for task in self.tasks:
            if task.status == self.NOT_STARTED:
                return True
        return False

    def format_time(self, time):
        """
        Formats the time in minutes to hours and minutes.

        Parameters
        ----------
        time (int): The time in minutes.

        Returns
        ----------
        str: The formatted time in the 'hh:mm' format.
        """
        time = int(time)
        return f"{time // 60}h{time % 60:02d}"

    def execute_task(self, task, priority):
        """
        Executes a task and updates its status.

        Parameters
        ----------
        task (Task): The task to be executed.
        priority (int): The priority value of the task.
        """
        print(f"🕰t={self.format_time(self.current_time)}")
        print(f"\tstarted '{task.description}' for {task.duration} mins...")

        self.current_time += task.duration
        print(f"\t✅ t={self.format_time(self.current_time)}, task completed! '{priority} priority'")

        self.remove_dependency(task.id)
        task.status = self.COMPLETED
        
    def execute_global_tasks(self):
        """
        Executes globally scheduled tasks based on dynamic programming results.
        """
        for task in self.global_tasks[0]:
            priority = self.task_priority_values.get(task.id, 0)
            self.execute_task(task, priority)
        self.global_tasks = [{}]

    def dynamic_programming_memory(self, done_so_far, utility_so_far, limit):
        """
        Applies dynamic programming with memoization to optimize task scheduling.

        Parameters
        ----------
        done_so_far (set): Set of tasks that have already been scheduled.
        utility_so_far (int): Current utility value.
        limit (int): Time limit in minutes for scheduling tasks.
        """
        for task in self.available_tasks: 
            temp = set(done_so_far)
            temp.add(task)
            current_tasks = frozenset(temp)

            if current_tasks in self.mem_dict: #if we already found the combination of tasks
                temp.remove(task)
                current_tasks = frozenset(temp)
                continue #move on to the following task

            self.task_priority_values[task.id] = self.calculate_priority(task.id)

            current_utility = utility_so_far + self.calculate_priority(task.id)
            self.mem_dict[current_tasks] = current_utility

            if current_utility > self.global_max[0]:
                self.global_max[0] = current_utility
                self.global_tasks[0] = current_tasks
                self.remove_dependency(task.id)
                self.available_tasks.remove(task)

                limit -= task.duration
            else:
                current_utility = utility_so_far

            if limit <= 0:
                continue

            self.get_ready_tasks()
            self.dynamic_programming_memory(current_tasks, current_utility, limit)

    def run_scheduler(self, starting_time):
        """
        Runs the scheduler to execute tasks based on dependencies.

        Parameters
        ----------
        starting_time (int): The starting time of the scheduler.
        """
        self.current_time = starting_time * 60
        self.get_ready_tasks()


        while self.unscheduled_tasks_exist() or self.priority_queue_strt or self.global_tasks[0]:
            if len(self.priority_queue_strt) > 0:
                task_strt, prio_strt = self.heap.heappop(self.priority_queue_strt)

                if self.current_time == task_strt.start_time:
                    self.execute_task(task_strt, prio_strt)
                    self.get_ready_tasks()
                else:
                    limit = task_strt.start_time - self.current_time
                    self.dynamic_programming_memory(set(), 0, limit)
                    self.execute_global_tasks()
                    self.heap.heappush(self.priority_queue_strt, (task_strt, prio_strt))
            else:
                limit = (20*60) - self.current_time
                self.dynamic_programming_memory(set(), 0, limit)
                self.execute_global_tasks()