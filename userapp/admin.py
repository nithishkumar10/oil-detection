from django.contrib import admin

# Register your models here.
from . models import UserModel,Contact_Us,PredictionCount,Predict_details,Last_login,Feedback,PredictionResult

admin.site.register(UserModel)
admin.site.register(Contact_Us)
admin.site.register(PredictionCount),
admin.site.register(Predict_details)
admin.site.register(Last_login)
admin.site.register(Feedback)
admin.site.register(PredictionResult)
