# This is the script that is called inside the Postgres function that runs when the trigger is triggered\
# This workaround was made because when retrieving the row that was just inserted, Postgres returns the one before the\
#  last, not the last eventhough the trigger is AFTER INSERT. Later on, we discovered that as long as the python script\
#  is running, the insert isn't committed yet. So, we made this script that call some other script and terminates so that\
#  the insert is committed and we can fetch the id of he last inserted row.
import subprocess
import sys
subprocess.Popen(['/home/eslam/anaconda3/bin/python', '/home/eslam/Downloads/Task5/predict-and-insert.py'])
sys.exit(0)