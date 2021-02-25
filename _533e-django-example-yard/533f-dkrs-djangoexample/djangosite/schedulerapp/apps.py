
# https://stackoverflow.com/questions/6791911/execute-code-when-django-starts-once-only

from django.apps import AppConfig
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

class SchedulerappConfig(AppConfig):
    name = 'schedulerapp'
    # verbose_name = "Periodic-Schedule-App"


    def ready(self):
        
        def myjob01():
            print(datetime.now(),' hello v10 from schedulerapp')
            f = open("/data/schedulerapp-output01.txt", "a")
            f.write(str(datetime.now()) + " myjob01 v10 has run!\n")
            f.close()

        # startup code here

        # =================================================
        # apscheduler

        # https://stackoverflow.com/questions/11654353/how-to-setup-apscheduler-in-a-django-project/15929907
        # https://dev.to/brightside/scheduling-tasks-using-apscheduler-in-django-2dbl
        # https://stackoverflow.com/questions/6791911/execute-code-when-django-starts-once-only
        # https://apscheduler.readthedocs.io/en/stable/userguide.html

        import logging

        logging.basicConfig()
        logging.getLogger('apscheduler').setLevel(logging.DEBUG)

        scheduler = BackgroundScheduler(job_defaults={'misfire_grace_time': 1}, )
        # scheduler.shutdown(wait=False)  
        scheduler.start()

        scheduler.print_jobs()
        s1 = scheduler.add_job(myjob01, 'interval', seconds=10, id='myjob01_id', replace_existing=True )

        # =================================================





