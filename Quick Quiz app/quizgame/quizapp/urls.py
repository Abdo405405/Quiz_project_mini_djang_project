from django.urls import path ,include


from . import views

app_name = "quizapp"
urlpatterns = [
    path("" , view=views.dispay_quiz, name="quiz" ) , 

    path ("result" , view=views.show_result , name="result")

]