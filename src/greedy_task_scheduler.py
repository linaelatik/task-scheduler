class TaskSchedulerGreedy:
    """
    Class used for scheduling tasks.

    Attributes
    ----------
    tasks (list): List of Task objects.
    priority_queue_dep (list): Priority queue based on dependencies.
    priority_queue_strt (list): Priority queue based on start time.
    heap (MaxHeapq): Heap instance.
    closest_start_time_dict (dict): Dictionary to store the earliest start time in dependent tasks.
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
        self.priority_queue_dep = [] 
        self.priority_queue_strt = [] 
        self.heap = MaxHeapq() 
        self.current_time= 0
 

    def print_self(self):
        """
        Prints the tasks added to the simple scheduler.
        """
        print("Tasks added to the simple scheduler:")
        print("--------------------------------------")
        for t in self.tasks:
            print(f"➡️'{t.description}', duration = {t.duration} mins.")
            if len(t.dependencies) > 0:
                print(f"\t ⚠️ This task depends on others!")

    def remove_dependency(self, id):
        """
        Removes the dependency of a task with the specified ID.

        Parameters
        ----------
        id (int): The ID of the task whose dependency is to be removed.
        """
        for t in self.tasks:
            if t.id != id and id in t.dependencies:
                t.dependencies.remove(id)  # Remove the dependency from the task
        
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



    
    def get_tasks_ready(self, current_time):
        """
        Gets tasks ready for execution based on their dependencies and inserts them 
        in their correct priority queus with their priority value.

        Parameters
        ----------
        current_time (int): Current time in minutes.
        """
        ready_tasks_prio_dep = []
        ready_tasks_prio_strt = []

        for task in self.tasks:
            if task.status == self.NOT_STARTED and len(task.dependencies) == 0:
                if task.has_time_constraint:
                    ready_tasks_prio_strt.append(task)
                else:
                    ready_tasks_prio_dep.append(task)
                    
        #Insert tasks in their correct priority queues
        
        for task in ready_tasks_prio_dep:
            task.status = self.IN_PRIORITY_QUEUE
            priority = self.calculate_priority(task.id)
            self.heap.heappush(self.priority_queue_dep, (task, priority))


        for task in ready_tasks_prio_strt:
            task.status = self.IN_PRIORITY_QUEUE
            priority = -1 * (task.start_time / 60)
            self.heap.heappush(self.priority_queue_strt, (task, priority))
            
    def check_unscheduled_tasks(self):
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
        
        print(f"🕰t={self.format_time(self.current_time)}")
        print(f"\tstarted '{task.description}' for {task.duration} mins...")

        self.current_time += task.duration
        print(f"\t✅ t={self.format_time(self.current_time)}, task completed! '{priority} priority'")
    
        self.remove_dependency(task.id)
        task.status = self.COMPLETED
        
    
    def run_scheduler(self, starting_time):
        """
        Runs the task scheduler based on the starting time.

        Parameters
        ----------
        starting_time (int): The starting time in hours.
        """
        self.current_time = starting_time * 60
        
        time_limit= 13*60
        
        print("Running a simple scheduler:\n")
        
        self.heap.build_max_heap(self.priority_queue_dep)
        
        self.heap.build_max_heap(self.priority_queue_strt)
        
        while self.check_unscheduled_tasks() or self.priority_queue_dep or self.priority_queue_strt:

            self.get_tasks_ready(self.current_time)
             
            if self.current_time >= time_limit: 
                break

            if len(self.priority_queue_dep) > 0 and len(self.priority_queue_strt) > 0:
                task1, prio_strt = self.heap.heappop(self.priority_queue_strt)
                task2, prio_dep = self.heap.heappop(self.priority_queue_dep)
                if self.current_time == task1.start_time or self.current_time + task2.duration > task1.start_time:
                    self.current_time= task1.start_time 
                    self.execute_task(task1, prio_strt)
                    
                    self.heap.heappush(self.priority_queue_strt, (task2, prio_strt))
    
                elif self.current_time + task2.duration <= task1.start_time:
                
                    self.execute_task(task2, prio_dep)
                    self.heap.heappush(self.priority_queue_strt, (task1, prio_strt))
                    
            elif len(self.priority_queue_dep) > 0 and len(self.priority_queue_strt) == 0:
                task2, prio_dep = self.heap.heappop(self.priority_queue_dep)
                                                    
                self.execute_task(task2, prio_dep)
                
            elif len(self.priority_queue_dep) == 0 and len(self.priority_queue_strt) > 0:
                task1, prio_strt = self.heap.heappop(self.priority_queue_strt)
                self.current_time= task1.start_time
                
                self.execute_task(task1, prio_strt) 
                
        total_time = self.current_time - (starting_time * 60)

        print(f"\n🏁 Completed all planned tasks in {total_time // 60}h{total_time % 60:02d}min!")