from django.shortcuts import render
import json
from random import shuffle
# Create your views here.


questions = []
def dispay_quiz (request) :
    global questions 
    questions=load_questions()
    titles = [qus["question"] for qus in questions ]
    questions_ids = [qus["id"] for qus in questions ]
    questions_len = range(1,len(questions)+1)
    all_ans = [qus["wrong_answers"] + [qus["correct_answer"]] for qus in questions] 
    questions_zip   = zip(questions_len,titles ,all_ans ,questions_ids )
    contest = {
         "questions" : questions_zip , 
    }
    

    return render (request , 'quiz.html' , context=contest) 


def show_result (request) :
        
        user_answers = request.POST.copy() 
        del user_answers["csrfmiddlewaretoken"]
        # print(user_answers)

        score = 0
        for id , ans in user_answers.items() : 
            for l in  questions: 
                if str(l["id"]) ==  id : 
                    if ans == l["correct_answer"]  :
                        score+=1
             
             
        return render (request , 'result.html' ,{"score" :score}) 




def load_questions():
    with open(r"C:\Users\abdul\OneDrive\سطح المكتب\quiz Game\quizgame\quizapp\data.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

        questions = data["questions"] 
        shuffle(questions) 
        return questions[:5] 





