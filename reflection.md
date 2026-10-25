# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

I identified four core classes: Owner, Pet, Task, and Scheduler. Owner stores and manages pets. Pet stores basic pet information and tasks. Task represents a scheduled activity and contains time, completion status, and recurrence information. Scheduler acts as the central controller that organizes tasks, sorts schedules, filters results, and detects conflicts.

**b. Design changes**

During implementation I added recurring task functionality directly to the Task class through the create_next_occurrence() method. This reduced complexity inside Scheduler and improved encapsulation by keeping recurrence behavior with the task it belongs to.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers task time, task completion status, recurrence frequency, and pet ownership. Time was prioritized because generating a clear chronological schedule is the most important feature for pet care planning.

**b. Tradeoffs**

The conflict detector only checks whether two tasks occur at exactly the same time. It does not calculate overlapping durations. This tradeoff keeps the implementation simple while still identifying the most common scheduling conflicts.

---

## 3. AI Collaboration

**a. How you used AI**

AI was used to brainstorm system architecture, generate UML diagrams, create dataclass skeletons, develop sorting algorithms, and draft unit tests. The most helpful prompts were focused questions about specific methods and class relationships.

**b. Judgment and verification**

One AI suggestion involved creating a more complex scheduling engine using multiple inheritance. I rejected that approach because it added complexity without improving the required project functionality. I verified decisions by testing code behavior with pytest.

---

## 4. Testing and Verification

**a. What you tested**

I tested task completion, task addition, sorting correctness, recurring task generation, and conflict detection. These tests cover the most important interactions in the system.

**b. Confidence**

4/5 Confidence
The tests confirm all major functionality works correctly. Additional testing could include invalid time inputs, empty schedules, and more advanced overlapping task scenarios.

---

## 5. Reflection

**a. What went well**

The strongest part of the project was separating responsibilities between classes. The Scheduler remains focused on organization logic while Task contains task-specific behavior.

**b. What you would improve**

I would implement persistent storage using JSON or SQLite so that schedules remain available after closing the application.

**c. Key takeaway**

I learned that AI is most effective when used as a collaborator rather than a decision maker. The human developer must still evaluate architecture decisions, verify results, and ensure the final design remains maintainable.