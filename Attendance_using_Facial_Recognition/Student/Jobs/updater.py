from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import modify_db


def start():
	scheduler = BackgroundScheduler(timezone='Asia/Kolkata')
	scheduler.add_job(modify_db, 'cron', day="12", hour="00", minute="05")
	scheduler.start()   