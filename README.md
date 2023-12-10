# ATTENDANCE_PROJECT

### 1. Requirments
- Install the following   
1.python: 3.11.0  
2.mysql: 8.0.33  
3.django: 5.0
  
### 2. Clone project from Gitlabs
- Copy the clone URL from Gitlab and paste it on the terminal of the working project directory.
```
git clone git@github.com:f-a-h-e-e-m/Employee_project.git
```
### 3. Configure project
- Create a virtual environment for the project.  
```
python3 -m venv attendance_env
```
- Install libraries from `requirements.txt` file.
```
 pip install -r requirements.txt
```

- Create `.env` file inside the root project folder(where manage.py file exist).  


### 4. Configure database

- Create corresponding database using mysql. 

- Add database credentials and details in `.env` and use below mentioned data as env file(only mentioned for testing purpose):

```
SECRET_KEY=(q%$_z2+ly$a@**v+ag8c^5norajn&-54@cv_xr_%kq((f!l*f

DATABASE_NAME='Attendance_db'
DATABASE_USER='remote_score_user'
DATABASE_PASSWORD='RRoot@123#'
DATABASE_PORT='3306'
DATABASE_HOST='13.232.41.167'

```

### 5. Configure celery

- Please install `redis`  and related configuration in your operating system.

```
celery -A attendance_app worker -l info

```
