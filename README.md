# task-scheduler
# Task Scheduling Algorithms: Greedy and Dynamic Programming

## 📜 Overview
This project implements a **Task Scheduler** using two approaches:
1. **Greedy Algorithm**: Makes locally optimal decisions at each step.
2. **Dynamic Programming**: Finds the global optimal solution by exploring all possible combinations while utilizing memoization for efficiency.

The scheduler handles tasks with dependencies and time constraints while prioritizing tasks based on utility. It includes features like multitasking support and efficient time management.

---

## 🎯 Features
- **Task Dependency Management**:
  - Tasks can depend on one or more other tasks.
  - The scheduler ensures dependent tasks are executed in the correct order.
  
- **Time-Constrained Tasks**:
  - Handles tasks with strict start times, scheduling them appropriately.
  
- **Multitasking Support**:
  - Tasks can be executed simultaneously if categorized as multitaskable.

- **Algorithms Implemented**:
  1. **Greedy Algorithm**:
     - Prioritizes tasks with the highest utility.
     - Works well in scenarios where locally optimal choices are sufficient.
  2. **Dynamic Programming**:
     - Explores all possible combinations to maximize total utility.
     - Accounts for dependencies and future consequences of scheduling decisions.

- **Utility-Based Scheduling**:
  - Tasks are ranked based on their utility, determined by:
    - **Dependencies**: Tasks with more dependent tasks are given higher priority.
    - **User Preference**: Tasks with higher user-assigned preferences are prioritized.

---

## 🛠️ Project Structure
task-scheduler/ ├── src/ │ ├── init.py # Marks the folder as a Python package │ ├── task.py # Task class and utility calculations │ ├── greedy_scheduler.py # Greedy algorithm implementation │ ├── dynamic_scheduler.py # Dynamic programming implementation │ ├── max_heap.py # Max heap data structure for priority queues │ └── test_cases.py # Test cases for validating the algorithms ├── README.md # Documentation └── .gitignore # Files to ignore (e.g., pycache)

yaml
Copy code

---

## 🚀 How to Run

### Clone the Repository
```bash
git clone https://github.com/your-username/task-scheduler.git
cd task-scheduler
Run Test Cases
To validate the algorithms:

bash
Copy code
python src/test_cases.py
Example Usage
python
Copy code
from src.greedy_scheduler import TaskSchedulerGreedy
from src.dynamic_scheduler import TaskSchedulerDynamic
from src.task import Task

# Define tasks
tasks = [
    Task(id=1, description='Wake up', start_time=8, duration=30, dependencies=[], preference=8),
    Task(id=2, description='Have breakfast', start_time='NA', duration=60, dependencies=[1], preference=6),
    Task(id=3, description='Walk to library', start_time='NA', duration=30, dependencies=[1], preference=10),
]

# Run the Greedy Scheduler
greedy_scheduler = TaskSchedulerGreedy(tasks)
greedy_scheduler.run_scheduler(starting_time=8)

# Run the Dynamic Scheduler
dynamic_scheduler = TaskSchedulerDynamic(tasks)
dynamic_scheduler.run_scheduler(starting_time=8)
📊 Experimental Results
Performance Comparison
Algorithm	Time Complexity	Space Complexity	Utility Achieved
Greedy Algorithm	O(N log N)	O(N)	96
Dynamic Programming	O(N)	O(2^N)	103
Observations:
Dynamic Programming achieves a higher utility but has higher space requirements.
Greedy Algorithm is faster and requires less memory, making it suitable for simpler scheduling problems.