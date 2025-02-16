import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

celery_app = Celery("core")

celery_app.config_from_object("django.conf:settings", namespace="CELERY")

celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    "fetch-btc-block-data-every-minute": {
        "task": "app.tasks.fetch_btc_block_data",
        "schedule": 60.0,
    },
    "fetch-eth-block-data-every-minute": {
        "task": "app.tasks.fetch_eth_block_data",
        "schedule": 60.0,
    },
}

if __name__ == "__main__":
    celery_app.start()
