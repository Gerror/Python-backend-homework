from application import celery_app
from users.models import User
from application.settings import CHECK_COUNT_RESULT_PATH

@celery_app.task()
def check_count():
    with open(CHECK_COUNT_RESULT_PATH, "w") as f:
        users = User.objects.all()
        f.write(str(users.count()))

