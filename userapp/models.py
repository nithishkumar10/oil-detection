from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(help_text="user_name", max_length=50)
    user_age = models.IntegerField(null=True)
    user_email = models.EmailField(help_text="user_email")
    user_password = models.EmailField(help_text="user_password", max_length=50)
    user_address = models.TextField(help_text="user_address", max_length=100)
    user_subject = models.TextField(
        help_text="user_subject", max_length=100, default="default_value_here"
    )
    user_contact = models.CharField(help_text="user_contact", max_length=15, null=True)
    user_image = models.ImageField(upload_to="media/", null=True)
    Date_Time = models.DateTimeField(auto_now=True, null=True)
    User_Status = models.TextField(default="pending", max_length=50, null=True)
    Otp_Num = models.IntegerField(null=True)
    Otp_Status = models.TextField(default="pending", max_length=60, null=True)
    Last_Login_Time = models.TimeField(null=True)
    Last_Login_Date = models.DateField(auto_now_add=True, null=True)
    No_Of_Times_Login = models.IntegerField(default=0, null=True)
    Message = models.TextField(max_length=250, null=True)

    class Meta:
        db_table = "UserModel"
        
        
class Contact_Us(models.Model):
    Full_Name = models.CharField(help_text="Full_name", max_length=50)
    Email_Address = models.EmailField(help_text="Email")
    Subject = models.CharField(help_text="Subject", max_length=50)
    Message = models.CharField(help_text="Message", max_length=50)

    class Meta:
        db_table = "Contact_Us_Details"     

        
        


class PredictionCount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prediction_count = models.PositiveIntegerField(default=0)

    def _str_(self):
        return f"{self.user.username} - Predictions: {self.prediction_count}"


class Predict_details(models.Model):
    predict_id = models.AutoField(primary_key=True)
    Field_1 = models.CharField(max_length=60, null=True)
    Field_2 = models.CharField(max_length=60, null=True)
    Field_3 = models.CharField(max_length=60, null=True)
    Field_4 = models.CharField(max_length=60, null=True)
    Field_5 = models.CharField(max_length=60, null=True)
    Field_6 = models.CharField(max_length=60, null=True)
    Field_7 = models.CharField(max_length=60, null=True)
    Field_8 = models.CharField(max_length=60, null=True)
    Field_9 = models.CharField(max_length=60, null=True)
    Field_10 = models.CharField(max_length=60, null=True)

    class Meta:
        db_table = "predict_detail"


class Last_login(models.Model):
    Id = models.AutoField(primary_key=True)
    Login_Time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "last_login"


class Feedback(models.Model):
    Feed_id = models.AutoField(primary_key=True)
    Rating = models.CharField(max_length=100, null=True)
    Review = models.CharField(max_length=225, null=True)
    Sentiment = models.CharField(max_length=100, null=True)
    Reviewer = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "feedback_details"

from django.db import models

from django.db import models

class PredictionResult(models.Model):
    predicted_class = models.IntegerField()
    email = models.EmailField()
    image_url = models.URLField()
    pdf_file = models.FileField(upload_to='prediction_pdfs/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction {self.id} - {self.predicted_class}"

