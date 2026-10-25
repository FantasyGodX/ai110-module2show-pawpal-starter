from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List


@dataclass
class Task:
    """Represents a pet care task."""

    description: str
    time: str
    frequency: str = "once"
    completed: bool = False
    due_date: date = field(default_factory=date.today)

    def mark_complete(self):
        """Marks the task as complete."""
        self.completed = True

    def create_next_occurrence(self):
        """Creates next occurrence for recurring tasks."""
        if self.frequency == "daily":
            return Task(
                description=self.description,
                time=self.time,
                frequency="daily",
                due_date=self.due_date + timedelta(days=1)
            )

        if self.frequency == "weekly":
            return Task(
                description=self.description,
                time=self.time,
                frequency="weekly",
                due_date=self.due_date + timedelta(weeks=1)
            )

        return None


@dataclass
class Pet:
    """Represents a pet."""

    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task):
        """Adds a task to the pet."""
        self.tasks.append(task)

    def get_tasks(self):
        """Returns all pet tasks."""
        return self.tasks


@dataclass
class Owner:
    """Represents a pet owner."""

    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet):
        """Adds a pet to the owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Returns all tasks from all pets."""
        results = []

        for pet in self.pets:
            for task in pet.tasks:
                results.append((pet.name, task))

        return results


class Scheduler:
    """Organizes and manages tasks."""

    def __init__(self, owner):
        self.owner = owner

    def get_schedule(self):
        """Gets all tasks sorted by time."""
        return sorted(
            self.owner.get_all_tasks(),
            key=lambda item: item[1].time
        )

    def sort_by_time(self):
        """Returns tasks sorted chronologically."""
        return self.get_schedule()

    def filter_by_pet(self, pet_name):
        """Filters tasks by pet."""
        return [
            (pet, task)
            for pet, task in self.owner.get_all_tasks()
            if pet == pet_name
        ]

    def filter_by_status(self, completed):
        """Filters tasks by completion status."""
        return [
            (pet, task)
            for pet, task in self.owner.get_all_tasks()
            if task.completed == completed
        ]

    def detect_conflicts(self):
        """Detects duplicate task times."""
        conflicts = []

        schedule = self.get_schedule()

        seen = {}

        for pet_name, task in schedule:
            if task.time in seen:
                conflicts.append(
                    f"Conflict: {pet_name} '{task.description}' "
                    f"shares {task.time} with "
                    f"{seen[task.time]}"
                )
            else:
                seen[task.time] = (
                    f"{pet_name} '{task.description}'"
                )

        return conflicts

    def mark_task_complete(self, pet_name, task_description):
        """
        Marks a task complete and creates recurring tasks.
        """
        for pet in self.owner.pets:
            if pet.name == pet_name:

                for task in pet.tasks:

                    if task.description == task_description:

                        task.mark_complete()

                        new_task = task.create_next_occurrence()

                        if new_task:
                            pet.add_task(new_task)

                        return True

        return False