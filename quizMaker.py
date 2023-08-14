# Name: Lavanya Uppala
# Creighton University, School of Medicine
# Date: 12/29/2022
# Email: lvu06382@creighton.edu
#
# Contributors: NONE
#
# The program converts a .csv file of properly formatted quiz questions
# into a sheet of randomized quiz questions, and a matching answer sheet
# along with other specifications based on option arguments:
# -i the input file name, if nonexistent then input will come from
#       the keyboard
# -o the output file name for the quiz file,
#       if nonexistent then output will be sent to the screen
# -a the output file name for the answer-key file,
#       if nonexistent then output will be sent to the screen

import sys
import getopt
import random
import pandas as pd

class quizMaker():


    # prints usage information in case of error
    def usage(self):
        print("Usage: quizMaker.py [-i FILE] [-o FILE]")
        print("\t-i: input file (.csv delimited); STDIN if not used")
        print("\t-q: quiz file (.txt file); STDOUT if not used")
        print("\t-a: answerkey file (.txt file); STDOUT if not used")


        # input should ideally be in the form question, correct answer,
        # 3x incorrect answer, answer rationale, comma-delimited


    def main(self):

        try:

            # reads in arguments from the command line
            opts, args = getopt.getopt(sys.argv[1:], "i:q:a:")

            input_file_name = ""
            quiz_file_name = ""
            answerkey_file_name = ""

            # set preferences based on arguments
            for (opt, arg) in opts:
                if opt == "-i":
                    input_file_name = arg
                elif opt == "-o":
                    quiz_file_name = arg
                elif opt == "-a":
                    quiz_file_name = arg
        
        # exception handling for invalid options
        except getopt.GetoptError as err:

            sys.stdout = sys.stderr
            print(str(err))
            self.usage()
            sys.exit(2)

        # list which stores all the lines read in from input
        file_input = []

        # file to be read
        inFile = ""

        input_file_name = "TestQuizMaker.csv"
        # initializes input source depending on option
        if input_file_name == "":
            inFile = sys.stdin
        else:
            inFile = open(input_file_name, "r")

        # reads all lines of input
        inFile.readline()
        line_read = inFile.readlines()
        #print (line_read)

        # files to be output
        quizFile = ""
        answerFile = ""

        quiz_file_name = "quiz.txt"
        answerkey_file_name = "answers.txt"

        # initializes output documents depending on options
        if quiz_file_name == "":
            quizFile = sys.stdout
        else:
            quizFile = open(quiz_file_name, "w")

        if answerkey_file_name == "":
            answerFile = sys.stdout
        else:
            answerFile = open(answerkey_file_name, "w")

        questionNum = 0

        # iterates through input file and generates output
        for line in line_read:

            questionNum = questionNum + 1

            # read a single line
            line_items = list(map(str.strip, line.split(",")))
            question = line_items[0]
            correctanswer = line_items[1]
            answers = line_items[1:5]
            rationale = line_items[6]
            
            random.shuffle(answers)
            #print(answers)

            questionAns = ["A.", "B.", "C.", "D."]
            randomAnswers = [m+str(n) for m,n in zip(questionAns, answers)]

            quizFile.write(str(questionNum) + ".\t" + str(question) +
                            "\n" + "\n".join(randomAnswers) + "\n\n")
            answerFile.write(str(question) + "\n" + correctanswer +
                            "\n" + rationale + "\n\n")
            



objectTest = quizMaker()
objectTest.main()
