from task_manager import TaskManager  # Import the TaskManager class
from utils import clear_screen        # Import screen clearing function

def main():
    manager = TaskManager()  # Create an instance of TaskManager

    while True:
        clear_screen()  # Clear the terminal screen for better readability

        # Display the header and list of tasks
        print("=== Task Manager ===")
        manager.list_tasks()

        # Display the menu options
        print("\nMenu:")
        print("1 - Add task")
        print("2 - Mark as done")
        print("3 - Unmark as done")
        print("4 - Delete task")
        print("0 - Exit")

        # Get user's choice
        choice = input("Choose an option: ")

        # Handle menu options
        if choice == '1':
            desc = input("Task description: ")
            manager.add_task(desc)
        elif choice == '2':
            index = int(input("Task number to mark as done: "))
            manager.mark_done(index)
        elif choice == '3':
            index = int(input("Task number to unmark as done: "))
            manager.unmark_done(index)
        elif choice == '4':
            index = int(input("Task number to delete: "))
            manager.delete_task(index)
        elif choice == '0':
            break  # Exit the loop and end the program
        else:
            # Invalid option handling
            input("Invalid option. Press Enter to continue.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
