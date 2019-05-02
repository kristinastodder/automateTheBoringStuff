#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

#The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento'}

#Generate 3 quiz files.
for quizNum in range(5):
    #Create the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    #Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum+1))
    quizFile.write('\n\n')
    
    #Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    
    #Loop through all 50 states, making a question for each.
    for questionNum in range(5):
        #Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 2)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

    #Write the question and answer options to the quiz file.
    quizFile.write('%s. What is the capital of %s?\n' % (questionNum +1, states[questionNum]))
    for i in range(3):
        quizFile.write('%s. %s\n' % ('ABC'[i], answerOptions[i]))
    quizFile.write('\n')
        
    #Write the answer key to a file.
    answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABC' [
        answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
