# Setting up Amazon RDS with PostgreSQL for Django Application

This guide will walk you through the process of setting up an Amazon RDS instance with PostgreSQL as the database engine for your Django application.

## Step 1: Create Amazon RDS Instance

1. Log in to the AWS Management Console.
2. Navigate to the Amazon RDS service.
3. Click on "Create database".
4. Choose "PostgreSQL" as the engine option.
5. Select a suitable DB instance class, storage type, and allocated storage.
6. Configure the instance settings:
   - **DB Instance Identifier**: Choose a unique identifier for your RDS instance.
   - **Master username**: Choose a username for the master user.
   - **Master password**: Choose a strong password for the master user.
7. Configure the advanced settings as needed.
8. Click on "Create database" to create the RDS instance.

## Step 2: Note Down Information

After creating the RDS instance, note down the following information:

- **Database Name**: `postgres`
- **Username**: Your chosen username
- **Password**: Your chosen password
- **Host (Endpoint)**: Your RDS instance endpoint
- **Port**: Default PostgreSQL port (5432)

## Step 3: Configure Security Group

1. Navigate to the Amazon RDS service.
2. Select the RDS instance you created.
3. In the "Connectivity & security" tab, click on the associated security group.
4. Click on "Edit inbound rules".
5. Add a new rule to allow inbound connections on port 5432 from the EC2 instance or IP address where your Django application is hosted.
6. Save the changes.

## Step 4: Update Django Configuration

In your Django application's `settings.py` file, update the database connection settings:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'your_chosen_username',
        'PASSWORD': 'your_chosen_password',
        'HOST': 'your_rds_endpoint',
        'PORT': '5432',
    }
}
```
>>[Unit]
Description=gunicorn daemon
After=network.target
   [Service]
   User=ubuntu
   Group=www-data
   WorkingDirectory=/home/ubuntu/data/s3rds_backend/core
   ExecStart=/home/ubuntu/.cache/pypoetry/virtualenvs/s3rds-backend-UDyHgMYQ-py3.12/bin/gunicorn --access-logfile - --workers 3  --bind unix:/home/ubuntu/data/s3rds_backend/core/backend.sock backend.wsgi:application>
   
   [Install]
   WantedBy=multi-user.target

###

   
# S3 
>>poetry add boto3
>>poetry add django-storages
>>INSTALLED_APPS+=  'storages',
