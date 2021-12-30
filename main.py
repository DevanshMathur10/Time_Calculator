# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main

finaltime=add_time("5:30 PM", "69:42","Thursday")
print("\n"+"\n"+finaltime+"\n"+"\n")

# Run unit tests automatically
main(module='test_module', exit=False)