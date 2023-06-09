
## 2023-1 Mobile Web Programming Class Assignment Repository

### After Git Clone

After cloning the repository for the Mobile Web Programming class assignment, you can follow these steps to execute the Django project:

1. Open a terminal or command prompt and navigate to the root directory of the cloned Django project.

2. Activate your virtual environment, if you have one set up for this project. Use the appropriate command based on your operating system and virtual environment setup. For example, if you are using `venv` on a Unix-based system, you can run:

   ```shell
   source <venv_name>/bin/activate

3. Install the project dependencies by running the following command:

   ```shell
   pip install -r requirements.txt
4. Once the dependencies are installed, you need to apply any pending database migrations. Run the following command:

   ```shell
   python manage.py migrate

5. Finally, start the Django development server by running the following command:

   ```shell
   python manage.py runserver

6. The development server will start, and you should see output similar to the following:

   ```shell
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CONTROL-C.

**you can find yolov5 code assignment at changedetection.py, detect.py**