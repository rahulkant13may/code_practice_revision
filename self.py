import subprocess
#subprocess.check_output(['ls','-l']) #all that is technically needed...
subprocess.call('django-admin startproject mysite',shell=True)

# import shlex, subprocess

# subprocess.Popen('django-admin startproject mysite')