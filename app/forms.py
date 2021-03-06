from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired, Optional 

class LoginForm(FlaskForm):
    """
    Represents the form for logging in.
    Attributes
    ----------
    username : StringField
        Text box for user to enter username.    
    password : PasswordField
        Text box for user to enter password.
    submit : SubmitField
        Button for user to log in.
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
class OverviewForm(FlaskForm):
    """
    Represent the form for the account home page.

    Attributes
    ----------
    complete : BooleanField
        Checkbox for user to mark task as complete.
    """
    complete = BooleanField('Mark as complete')

class NewTaskForm(FlaskForm):
    """
    Represents the form for creating a new task.

    Attributes
    ----------
    title : StringField
        Where users can type in the title of a new task. Data is required for this.
    description : StringField
        Where users can type in the description of a new task. Data is not required for this.
    create : SubmitField
        Button for user to finish creating new task.
    date : StringField
        Where users can type in a date for a deadline of a task. Data is not required for this.
    priority : IntegerField
        Where users enter priority of a task. Data is not required for this.
    """
    title = StringField('*Required Title', validators = [DataRequired()])
    description = StringField('Description')
    create = SubmitField('Create')
    date = DateField('*Required: Finish by (mm/dd/yyyy)', format=('%m/%d/%Y'))
    reminder = BooleanField("Flash Reminder")

    priority = SelectField('Priority', choices=[('None','None'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),
                                                 ('6','6'),('7','7'),('8','8'),('9','9'),('10','10')])
    category = SelectField("Add Category", choices=[('None','None'),('Work','Work'),('School','School'),('Personal','Personal')])


class DeleteTaskForm(FlaskForm):
    """
    Represents the form for deleting a task.
    
    Attributes
    ----------
    title : StringField
        Where users can type in the title of a task that they will delete. Data is required for this.
    delete : SubmitField
        Button for user to finish deleting a task.
    """
    title = StringField('Title of task to delete', validators = [DataRequired()])
    delete = SubmitField('Delete')

class RegisterForm(FlaskForm):
    """
    Represents the form for creating a new user account.
    Attributes
    ----------
    username : StringField
        Text box for user to enter username.    
    password : PasswordField
        Text box for user to enter password.
    create : SubmitField
        Button for new user to make an account.
    """
    username = StringField("Username", validators= [DataRequired()])
    password = PasswordField("Password", validators= [DataRequired()])
    create = SubmitField("Register")
    
class EditTaskForm(FlaskForm):
    """
    Represents the form for editing an existing task.

    Attributes
    ----------
    title : StringField
        Textbox for user to enter a new title.
    description : StringField
        Textbox for user to enter a new title.
    save : SubmitField
        Button for user to save changes.
    date : Datefield
        Date that the task needs to be finished by.
    category : StringField
        Category that task belongs to.
    reminder : BooleanField
        Enable alerts about task due date.
    """
    title = StringField("*Required Title", validators=[DataRequired()])
    description = StringField("Description")
    save = SubmitField("Save changes")
    date = DateField('*Required: Finish by (mm/dd/yyyy)', format=('%m/%d/%Y'))
    category = SelectField("Add Category", choices=[('None','None'),('Work','Work'),('School','School'),('Personal','Personal')])
    reminder = BooleanField("Flash Reminder")

class FindTaskForm(FlaskForm):
    """
    Represents the form for finding an existing task.

    Attributes
    ----------
    title : StringField
        Title of the task.
    find : SubmitField
        Button for user to start search for task by title.
    """
    title = StringField("Title", validators=[DataRequired()])
    find = SubmitField("Find")

class ShareTaskForm(FlaskForm):
    """
    Represents the form for sharing a task with another user.

    Attributes
    ----------
    title : StringField
        Title of the task being shared.
    username : StringField
        Username of the recipient user.
    share : SubmitField
        Button for the user to share the task with another user.
    """
    title = StringField("Task", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    share = SubmitField("Share")    

    
class SetPriorityForm(FlaskForm):
    """
    Represents the form for setting priority to a task.

    Attributes
    ----------
    title : StringField
        Title of the task being shared.
    priority : IntegerField
        priority number of the task.
    set : SubmitField
        Button for the user to set priority of a task.
    """
    title = StringField("Title of Task to set priority", validators=[DataRequired()])
    #priority = IntegerField("Priority level (1-10)", validators=[DataRequired()])
    priority = SelectField(u'Priority', choices=[('None','None'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),
                                                 ('6','6'),('7','7'),('8','8'),('9','9'),('10','10')])
    set = SubmitField("Set")    
    
    
class CategorizeForm(FlaskForm):
    """
    Represents the form for adding category to a task.
    
    Attributes
    ----------
    title : StringField
        Where users can type in the title of a task that they want to add category to. Data is required.
    addcategory : SubmitField
        Button for user to finish adding category.
    """
    title = StringField('Title of task to add category', validators = [DataRequired()])
    category = SelectField("Add Category", choices=[('None','None'),('Work','Work'),('School','School'),('Personal','Personal')])
    addcategory = SubmitField('Add category')
