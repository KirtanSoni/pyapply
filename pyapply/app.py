import logging
import time

#import importlib


def listener(interval: int, inputcallback, callback) -> None:
    clipboard = inputcallback()
    while True:
        if clipboard == inputcallback():
            continue
        clipboard = inputcallback()
        try:
            callback(clipboard)
        except Exception as e:
            logging.error(f"Error in listener: {e}")
        time.sleep(interval)




# INPUT_FACTORY = 'pyapply.inputFactory.' 
# def file_factory(path: str, strategy: str) -> str: 
#     """
#     Dynamically imports a module based on the provided strategy and calls its getdescription function.

#     Parameters:
#     clipboard (str): The current content of the clipboard.
#     strategy (str): The name of the module to import from the inputFactory package.

#     Returns:
#     str: The description obtained from the getdescription function of the imported module.
#     """
#     try:
#         module_name = f"{INPUT_FACTORY}{strategy}"
#         module = importlib.import_module(module_name)
#         getdescription = getattr(module, 'getdescription')
#         description = getdescription(path)
#         return description
#     except Exception as e:
#         logging.error(f"Error in file_factory: {e}")
#         raise e
    