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
## 🚀 How to Run

### Clone the Repository
```bash
git clone https://github.com/your-username/task-scheduler.git
cd task-scheduler
