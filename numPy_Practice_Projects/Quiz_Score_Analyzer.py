# Quiz Score Analyzer
# This program allows you to input quiz scores for a class of students and provides
#  various analyses such as average score, highest score, lowest score, and ranking 
# of students.


import numpy as np 

def Enter_scores():
    students=int(input("the number of student: "))
    store=[]
    for i in range(students):
        s_data=list(map(int,input(f"Enter scores of student {i+1}: ").split()))
        store.append(s_data)
    return np.array(store)
score=Enter_scores()
  

def view_scores(scores):
    print("Scores of students:")
    for i ,score in enumerate(scores,start=1):
        print(f"{i}: {score}")

view_scores(score)

def Statistics(scores):
    print(f"the average score is {np.average(scores)}")
    print(f"the highest score is {np.max(scores)}")
    print(f"the lowest score is {np.min(scores)}")
    return scores

Statistics(score)

def rank_students(scores):
    total_scores =np.sum(scores,axis=1)
    ranks = np.argsort(-total_scores) + 1  # Adding 1 to make ranks start from 1
    print("Student Rankings based on total scores:")
    for i ,rank in enumerate(ranks,start=1):
        print(f"Student {i}: Rank {rank}, Total Score: {total_scores[i-1]}")
rank_students(score)



