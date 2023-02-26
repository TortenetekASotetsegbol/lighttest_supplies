import inspect
import logging
from importlib import import_module


def get_task_functions(modules):
    """
    define a function that takes a list of modules and returns a list of task functions
    """
    task_functions: list[object] = []
    for module in modules:
        try:
            # import the module using its name
            imported_module = import_module(module)
            # loop through each object in the imported module
            for _, obj in inspect.getmembers(imported_module):
                # check if the object is a function and its name contains "task_"
                if inspect.isfunction(obj) and "task_" in obj.__name__:
                    # append the function to the task functions list
                    task_functions.append(obj)
        except Exception as e:
            # catch any errors that may occur during importing or inspecting
            logging.error(f"Error while processing {module}: {e}")
    # return the task functions list
    return task_functions
