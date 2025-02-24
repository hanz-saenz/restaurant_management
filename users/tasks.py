from celery import shared_task
import pandas as pd
from .models import User

@shared_task
def process_user_upload(file_content):
    df = pd.read_csv(pd.compat.StringIO(file_content))
    for _, row in df.iterrows():
        User.objects.create(
            first_name=row['first_name'],
            last_name=row['last_name'],
            email=row['email'],
            phone=row['phone'],
            typology=row['typology'],
            restaurant_id=row['restaurant_id']
        )