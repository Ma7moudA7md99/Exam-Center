# importing needed libraries
from flask import Flask, redirect, render_template, request, url_for
import pyodbc

# database connection
# SERVER={your server name}
# change before running
connection_string = 'DRIVER=SQL Server;SERVER=MAHMOUD_AHMED;DATABASE=exam_center;'

# initialize app name
exam_center = Flask(__name__)


# Check the current user session.
@exam_center.route('/', methods=['GET', 'POST'])
def login():
    return render_template('home.html')


@exam_center.route('/doctor', methods=["GET", "POST"])
def get_login():
    # Declare global variables
    global username, password, title
    title = ""
    # If the request method is POST
    if request.method == 'POST':
        # Get username and password from form
        username = request.form.get('username')
        password = request.form.get('password')

        # Establish connection with database
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        try:
            # Attempt to retrieve password for doctor
            cursor.execute(
                f"select passkey from doctor where username = '{username}'")
            doctor_check = cursor.fetchone()

            # Check if the doctor's password matches
            if doctor_check[0] == password:
                print('Doctor')
            else:
                print('wrong username or password')
        except:
            print("Error in fetching data")

    # Return empty string
    return render_template('login.html', title = 'Doctor Log')

@exam_center.route('/student', methods=["GET", "POST"])
def student_login():
    # Declare global variables
    global username, password
    title = ""
    # If the request method is POST
    if request.method == 'POST':
        # Get username and password from form
        username = request.form.get('username')
        password = request.form.get('password')

        # Establish connection with database
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        try:
            # Attempt to retrieve password for student
            cursor.execute(
                f"select passkey from student where username = '{username}'")
            student_check = cursor.fetchone()
            # Check if the student's password matches
            if student_check[0] == password:
                return "redirect(url_for('student'))"
            else:
                print('wrong username or password')
        except:
            print("Error in fetching data")
    # Return empty string
    return render_template('login.html', title = 'Student Log')
if __name__ == '__main__':
    exam_center.run(debug=True)
