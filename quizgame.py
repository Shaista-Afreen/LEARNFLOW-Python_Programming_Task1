#Quiz Game

def quiz_game():
    print("Select your quiz topic:")
    print("A. General Knowledge Quiz")
    print("B. Sports/Games Quiz")
    print("C. Science Quiz")
    selection=input("Enter your choice (A/B/C): ").upper()
    if selection == 'A':
        # GENERAL KNOWLEDGE QUIZ
        print("You have selected General Knowledge Quiz")
        print("Choose a level for your quiz:")
        print("1. Easy")
        print("2. Medium")
        print("3. Difficult")
        level=input("Enter your choice (1/2/3): ").lower()
        # Easy level in General Knowledge Quiz
        if level == "1":
            print("You have chosen easy level")
            questions11=( "Who invented the telephone?",
            "What is the chemical symbol for the element gold?",
            "What is the capital city of Australia?",
            "What is the longest river in the world?",
            "What is the capital city of France?" )

            options11=(("A. Alexander Graham Bell ","B. Thomas Edison ","C. Nikola Tesla ","D. Albert Einstein "),
                ("A. Au ","B. Ag ","C. Fe ","D. Hg"),
                ("A. Sydney ","B. Melbourne ","C. Canberra ","D. Brisbane "),
                ("A. Nile River ","B. Amazon River ","C. Mississippi River","D. Yangtze River "),
                ("A. Paris ","B. London ","C. Rome ","D. Berlin "))
            answers11=("A","A","C","A","A")
            guesses11=[]
            score11=0
            question_num11=0

            for question11 in questions11:
                print("**************************")
                print(question11)
                for option11 in options11[question_num11]:
                    print(option11)

                guess11=input("Enter (A,B,C,D): ").upper()
                guesses11.append(guess11)
                if guess11 == answers11[question_num11]:
                    score11 += 1
                    print("CORRECT!")
                else:
                    print("INCORRECT!")
                    print(f"{answers11[question_num11]} is the correct answer")
                question_num11 += 1

        
            print("******************")
            print("  RESULTS   ")
            print("*******************")
            print("Answers: ", end="")
            for answer11 in answers11:
                print(answer11,end=" ")
            print()
            print("Guesses: ", end="")
            for guess11 in guesses11:
                print(guess11,end=" ")
            print()
            print(f"Your score is {score11}/5")

        #Medium Level in General Knowledge Quiz

        elif level == "2":
            print("You have chosen medium level")    
            questions12=("What is the closest planet to the sun?",
                "How many continents are there?",
                "Which planet is known as the Red Planet?",
                "What is the largest ocean on Earth?",
                "What is the largest mammal in the world?")
            options12=(("A. Mercury ","B. Earth ","C. Venus ","D. Jupiter "),
                ("A. Seven ","B. Six ","C. Five ","D. Eight "),
                ("A. Venus ","B. Earth ","C. Mars ","D. Jupiter "),
                ("A. The Pacific Ocean ","B. Atlantic","C. Indian ","D. Arctic"),
                ("A. The African Elephant ","B. The Blue Whale ","C. The Fin Whale ","D. Giraffe "))
            answers12=("A","A","C","A","B")
            guesses12=[]
            score12=0
            question_num12=0

            for question12 in questions12:
                print("**************************")
                print(question12)
                for option12 in options12[question_num12]:
                    print(option12)

                guess12=input("Enter (A,B,C,D): ").upper()
                guesses12.append(guess12)
                if guess12 == answers12[question_num12]:
                    score12 += 1
                    print("CORRECT!")
                else:
                    print("INCORRECT!")
                    print(f"{answers12[question_num12]} is the correct answer")
                question_num12 += 1


            print("******************")
            print("  RESULTS   ")
            print("*******************")
            print("Answers: ", end="")
            for answer12 in answers12:
                print(answer12,end=" ")
            print()
            print("Guesses: ", end="")
            for guess12 in guesses12:
                print(guess12,end=" ")
            print()
            print(f"Your score is {score12}/5")

        #Difficult level in General Knowledge Quiz
        elif level == "3":
            print("You have chosen difficult level")
            questions13=("Which country is the largest producer of coffee in the world?",
            "What is the capital city of Canada?",
            "Who developed the theory of general relativity?",
            "Which mountain is the highest in Africa?",
            "Who was the first person to walk on the moon?")

            options13=(("A. Brazil ","B. Colombia ","C. Vietnam ","D. Ethiopia "),
            ("A. Ottawa ","B. Toronto ","C. Vancouver ","D. Montreal "),
            ("A. Isaac Newton ","B. Albert Einstein ","C. Stephen Hawking ","D. Max Planck "),
            ("A. Kilimanjaro ","B. Mount Kenya ","C. Mount Elgon ","D. Mount Stanley "),
            ("A. Neil Armstrong ","B. Buzz Aldrin ","C. Michael Collins ","D. Yuri Gagarin "))
            answers13=("A","A","B","A","A")
            guesses13=[]
            score13=0
            question_num13=0

            for question13 in questions13:
                print("**************************")
                print(question13)
                for option13 in options13[question_num13]:
                    print(option13)

                guess13=input("Enter (A,B,C,D): ").upper()
                guesses13.append(guess13)
                if guess13 == answers13[question_num13]:
                    score13 += 1
                    print("CORRECT!")
                else:
                    print("INCORRECT!")
                    print(f"{answers13[question_num13]} is the correct answer")
                question_num13 += 1


            print("******************")
            print("  RESULTS   ")
            print("*******************")
            print("Answers: ", end="")
            for answer13 in answers13:
                print(answer13,end=" ")
            print()
            print("Guesses: ", end="")
            for guess13 in guesses13:
                print(guess13,end=" ")
            print()
            print(f"Your score is {score13}/5")

        else:
            print("No proper option selected")

    #SPORTS/GAMES QUIZ

    elif selection == 'B':
        print("You have selected Sports/Games Quiz")
        print("Choose a level for your quiz:")
        print("1. Easy")
        print("2. Medium")
        print("3. Difficult")
        level=input("Enter your choice (1/2/3): ").lower()
        # Easy Level in Sports/Games Quiz
        if level == "1":
            print("You have chosen easy level")
            questions21=( "What ball is used in table tennis?",
            "In what kind of sport are the “Golden Ball” medals won?",
            "What game is considered the national sport of Japan?",
            "In which country were the first Olympic Games held?",
            "Who was the first player to score 10,000 runs in Test cricket?" )

            options21=(("A. Football ","B. Basketball ","C. Tennis ","D. Ping-pong "),
                ("A. Hockey ","B. Football ","C. Baseball ","D. Basketball"),
                ("A.Tennis ","B. Golf ","C. Baseball ","D. Sumo "),
                ("A. Italy ","B. Greece ","C. USA ","D. France"),
                ("A. Sunil Gavaskar ","B. Don Bradman ","C. Allan Border ","D. Sachin Tendulkar "))
            answers21=("D","B","D","B","A")
            guesses21=[]
            score21=0
            question_num21=0

            for question21 in questions21:
                print("**************************")
                print(question21)
                for option21 in options21[question_num21]:
                    print(option21)

                guess21=input("Enter (A,B,C,D): ").upper()
                guesses21.append(guess21)
                if guess21 == answers21[question_num21]:
                    score21 += 1
                    print("CORRECT!")
                else:
                    print("INCORRECT!")
                    print(f"{answers21[question_num21]} is the correct answer")
                question_num21 += 1


            print("******************")
            print("  RESULTS   ")
            print("*******************")
            print("Answers: ", end="")
            for answer21 in answers21:
                print(answer21,end=" ")
            print()
            print("Guesses: ", end="")
            for guess21 in guesses21:
                print(guess21,end=" ")
            print()
            print(f"Your score is {score21}/5")

        # Medium level in Sports/Games Quiz

        elif level == "2":
            print("You have chosen medium level")
            questions22=("What sport is considered the most popular in the world? ",
                "Which country won the first ever cricket world cup in 1975? ",
                "Which country has won the most icc cricket world cup titles ? ",
                "Which country is known for introducing the game of cricket to the world? ",
                "Which is the national sport of america ?")
            options22=(("A. Football ","B. Tennis ","C. Golf ","D. Basketball "),
                ("A. Australia ","B. West Indies ","C. England ","D. India "),
                ("A. West Indies ","B. India ","C. Australia ","D. Pakistan "),
                ("A. India ","B. England ","C. Australia ","D. West Indies "),
                ("A. Baseball ","B. Ice Hockey ","C. Tennis ","D. Golf "))
            answers22=("A","B","C","B","A")
            guesses22=[]
            score22=0
            question_num22=0


            for question22 in questions22:
                print("***************************")
                print(question22)
                for option22 in options22[question_num22]:
                    print(option22)

                guess22=input("Enter (A,B,C,D): ").upper()
                guesses22.append(guess22)
                if guess22 == answers22[question_num22]:
                    score22 += 1
                    print("CORRECT!")
                else:
                    print("INCORRECT!")
                    print(f"{answers22[question_num22]} is the correct answer")
                question_num22 += 1


            print("******************")
            print("  RESULTS   ")
            print("*******************")
            print("Answers: ", end="")
            for answer22 in answers22:
                print(answer22,end=" ")
            print()
            print("Guesses: ", end="")
            for guess22 in guesses22:
                print(guess22,end=" ")
            print()
            
            print(f"Your score is {score22}/5")
            
    #Difficult level in Sports/Games Quiz 
        elif level == "3":
            print("You have chosen difficult level")
            questions23=("Thomas Cup and Uber Cup are prestigious trophies of which sport?",
                "Name the 1st woman cricketer to appear at 6 Cricket World Cups?",
                "Which of the following countries has won the Football World Cup the maximum number of times?",
                "Which sport was originally known as mintonette?",
                "Which country won the most gold medals at the Summer Olympics?")

            options23=(("A. Badminton ","B. Lawn Tennis ","C. Table Tennis ","D. Golf "),
                ("A. Mithali Raj ","B. Smriti Mandhana ","C. Harmanpreet Kaur ","D. Jhulan Goswami "),
                ("A. Germany ","B. Italy ","C. Argentina ","D. Brazil"),
                ("A. Badminton ","B. Volleyball ","C. Table Tennis ","D. Squash "),
                ("A. United States ","B. USSR ","C. China ","D. United Kingdom"))
            answers23=("A","A","D","B","A")
            guesses23=[]
            score23=0
            question_num23=0


            for question23 in questions23:
                print("**************************")
                print(question23)
                for option23 in options23[question_num23]:
                    print(option23)

                guess23=input("Enter (A,B,C,D): ").upper()
                guesses23.append(guess23)
                if guess23 == answers23[question_num23]:
                    score23 += 1
                    print("CORRECT!")
                else:
                    print("INCORRECT!")
                    print(f"{answers23[question_num23]} is the correct answer")
                question_num23 += 1


            print("******************")
            print("  RESULTS   ")
            print("*******************")
            print("Answers: ", end="")
            for answer23 in answers23:
                print(answer23,end=" ")
            print()
            print("Guesses: ", end="")
            for guess23 in guesses23:
                print(guess23,end=" ")
            print()
                
            print(f"Your score is {score23}/5")
            

        else:
            print("No proper option selected.")


    #SCIENCE QUIZ
    elif selection == 'C':
        print("You have selected SCIENCE Quiz")
        print("Choose a level for your quiz:")
        print("1. Easy")
        print("2. Medium")
        print("3. Difficult")
        level=input("Enter your choice (1/2/3): ").lower()

        #Easy level in Science Quiz
        if level == "1":
            print("You have chosen easy level")

            questions31=("What is the hardest natural substance on Earth?",
                "What is the boiling point of water?",
                "What is the pH level of pure water?",
                "Which type of electromagnetic radiation has the most energy per photon?",
                "What is the main component of the sun?")
            options31=(("A. Gold ","B. Iron ","C. Diamond ","D. Silver"),
                ("A. 50°C ","B. 75°C ","C. 100°C ","D. 125°C "),
                ("A. 5 ","B. 6 ","C. 7 ","D. 8 "),
                ("A. Radio Waves ","B. Infrared ","C. X-Rays ","D. Gamma Rays"),
                ("A. Helium ","B. Hydrogen ","C. Oxygen ","D. Carbon"))
            answers31=("C","C","C","D","B")
            guesses31=[]
            score31=0
            question_num31=0


            for question31 in questions31:
                print("***************************")
                print(question31)
                for option31 in options31[question_num31]:
                    print(option31)

                guess31=input("Enter (A,B,C,D): ").upper()
                guesses31.append(guess31)
                if guess31 == answers31[question_num31]:
                    score31 += 1
                    print("CORRECT!")
                else:
                    print("INCORRECT!")
                    print(f"{answers31[question_num31]} is the correct answer")
                question_num31 += 1


            print("******************")
            print("  RESULTS   ")
            print("*******************")
            print("Answers: ", end="")
            for answer31 in answers31:
                print(answer31,end=" ")
            print()
            print("Guesses: ", end="")
            for guess31 in guesses31:
                print(guess31,end=" ")
            print()
                
            print(f"Your score is {score31}/5")
                

        #Medium Level in Science Quiz
        elif level == "2":
            print("You have chosen medium level.")
            questions32=("What is the powerhouse of the cell?",
                "What is the largest organ in the human body?",
                "Which gas is most abundant in the Earth's atmosphere?",
                "Which planet has the most moons?",
                "What is the most common type of star in the Milky Way galaxy?")
            options32=(("A. Nucleus ","B. Ribosome ","C. Mitochondria ","D. Endoplasmic reticulum "),
                ("A. Heart ","B. Liver ","C. Lungs ","D. Skin "),
                ("A. Oxygen ","B. Carbondioxide ","C. Nitrogen ","D. Hydrogen "),
                ("A. Jupiter ","B. Mars ","C. Earth ","D. Saturn "),
                ("A. Red giant ","B. White dwarf ","C. Red dwarf ","D. Blue giant "))
            answers32=("C","D","C","A","C")
            guesses32=[]
            score32=0
            question_num32=0


            for question32 in questions32:
                print("***************************")
                print(question32)
                for option32 in options32[question_num32]:
                    print(option32)

                guess32=input("Enter (A,B,C,D): ").upper()
                guesses32.append(guess32)
                if guess32 == answers32[question_num32]:
                    score32 += 1
                    print("CORRECT!")
                else:
                    print("INCORRECT!")
                    print(f"{answers32[question_num32]} is the correct answer")
                question_num32 += 1


            print("******************")
            print("  RESULTS   ")
            print("*******************")
            print("Answers: ", end="")
            for answer32 in answers32:
                print(answer32,end=" ")
            print()
            print("Guesses: ", end="")
            for guess32 in guesses32:
                print(guess32,end=" ")
            print()
            
            print(f"Your score is {score32}/5")
            


        #Difficult Level in Science Quiz
        elif level == "3":
            print("You have chosen  difficult level.")
            questions33=("What is the second most abundant element in the Earth's crust?",
                "What is the name of the largest moon of Saturn?",
                "What type of radiation has the shortest wavelength?",
                "What is the rarest naturally occurring element on Earth?",
                "Which scientist is known for the laws of planetary motion?")
            options33=(("A. Silicon ","B. Oxygen ","C. Aluminum ","D. Iron"),
                ("A. Europa","B. Titan ","C. Ganymede ","D. Callisto"),
                ("A. Radio Waves ","B. Infrared ","C. Ultraviolet ","D. Gamma Rays "),
                ("A. Astatine","B. Francium ","C. Technetium ","D. Promethium "),
                ("A. Isaac Newton ","B. Albert Einstein ","C. Johannes Kepler ","D. Galileo Galilei"))
            answers33=("A","B","D","A","C")
            guesses33=[]
            score33=0
            question_num33=0


            for question33 in questions33:
                print("***************************")
                print(question33)
                for option33 in options33[question_num33]:
                    print(option33)

                guess33=input("Enter (A,B,C,D): ").upper()
                guesses33.append(guess33)
                if guess33 == answers33[question_num33]:
                    score33 += 1
                    print("CORRECT!")
                else:
                    print("INCORRECT!")
                    print(f"{answers33[question_num33]} is the correct answer")
                question_num33 += 1


            print("******************")
            print("  RESULTS   ")
            print("*******************")
            print("Answers: ", end="")
            for answer33 in answers33:
                print(answer33,end=" ")
            print()
            print("Guesses: ", end="")
            for guess33 in guesses33:
                print(guess33,end=" ")
            print()
                
            print(f"Your score is {score33}/5")
                

        else:
            print("No proper option selected.")

    else :
        print("No proper option selected")

while True:
    quiz_game()
    play_again = input("Do you want to play the quiz game again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        break
print("Thanks for playing!")
