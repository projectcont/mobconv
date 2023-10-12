#========================================
# Scheduler Jobs
# модуль настраивает периодичсекое выполнение задачи, автор-
# https://github.com/devchandansh/django-apscheduler/blob/master/example_project/example_project/urls.py
#========================================

from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
scheduler = BackgroundScheduler()
scheduler.configure(timezone=utc)


import cron.scheduler_jobs
#scheduler.add_job(cron.scheduler_jobs.getapi, 'interval', seconds=10)

# расписание выполнение функции cron.scheduler_jobs.getapi - раз в сутки
scheduler.add_job(cron.scheduler_jobs.getapi, 'interval', seconds=86400)
scheduler.start()

#========================================