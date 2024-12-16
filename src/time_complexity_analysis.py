import time
import matplotlib.pyplot as plt
from io import StringIO
import sys
import numpy as np
import random



def simulate_time_complexity(num_tasks):
    # Create a list of tasks with random dependencies
    tasks = []
    for i in range(num_tasks):
        task = Task(
            id=i,
            description=f'Task {i}',
            start_time='NA',
            duration= random.randint(10, 60),
            dependencies = [] ,
            preference=random.randint(1, 10)
        )
        tasks.append(task)

    # Initialize the TaskScheduler
    scheduler = TaskSchedulerGreedy(tasks)

    # Measure execution time for different input sizes
    execution_times = []
    for i in range(num_tasks):
        start_time = time.time()
        scheduler.run_scheduler(8)
        execution_time = time.time() - start_time
        execution_times.append(execution_time)

    return execution_times

def plot_time_complexity(num_tasks, execution_times):
    plt.plot(range(num_tasks), execution_times, marker='o', linestyle='-', color='b')
    plt.title('Experimental Time Complexity Analysis')
    plt.xlabel('Number of Available Tasks')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.show()

def test_greedy_task_scheduler(n):
    """
    Test the performance of the task scheduler for a given number of tasks.

    Parameters
    ----------
        n (int): The number of tasks to be generated and tested.

    Returns
    ----------
        float: The time taken for the task scheduler to run for 'n' tasks.
    """
    tasks = []  # Generate 'n' tasks here
    for i in range(n):
        # Create tasks and add them to the list
        task = Task(id=i+1, description=f"Task {i+1}", start_time='NA', duration=30, dependencies=[],
                    preference=random.randint(1, 10))
        tasks.append(task)

    scheduler = TaskSchedulerGreedy(tasks)
    start_time = time.time()

    # Redirect stdout to a buffer
    stdout_buffer = StringIO()
    sys.stdout = stdout_buffer

    scheduler.run_scheduler(8)

    # Reset stdout
    sys.stdout = sys.__stdout__

    end_time = time.time()

    return end_time - start_time



def plot_task_scheduler_performance(max_tasks):
    """
    Plot the performance analysis of the task scheduler.

    Parameters
    ----------
        max_tasks (int): The maximum number of tasks to be tested.
    """
    durations = []
    task_counts = []
    log_n = []

    for i in range(1, max_tasks + 1):
        duration = test_greedy_task_scheduler(i)
        durations.append(duration)
        task_counts.append(i)
        log_n.append(np.log(i))

    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Number of Tasks')
    ax1.set_ylabel('Time (seconds)', color='tab:red')
    ax1.plot(task_counts, durations, color='tab:red', label='Task Scheduler Performance')

    ax3 = ax1.twinx()
    ax3.set_ylabel('Log(n)', color='tab:green')
    ax3.plot(task_counts, log_n, color='tab:green', label='log(n)')

    ax1.set_yscale('log')
    ax1.set_xscale('linear')

    fig.tight_layout()
    plt.title('Task Scheduler Performance and Scaling Analysis')
    ax1.legend(loc='upper left')
    ax3.legend(loc='lower right')
    plt.show()