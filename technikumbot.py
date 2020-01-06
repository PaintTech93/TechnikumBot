from talk import talk
import wikipedia
import random
import operator
import datetime
from speak import myCommand

def technikumbot(command):

    errors=[
        "I don't know what you mean",
        "I could not understand you",
        "Can you repeat it please?",
    ]

    if 'hello' in command:
        talk("Hello I am Tech, FH Technikum's personal assistant" "How may I help you")

    elif 'time' in command:
        currenttime = datetime.datetime.now()
        print(currenttime.strftime("%H:%M:%S"))
        talk("It's " + str(currenttime.strftime("%H:%M:%S")))

    elif 'date' in command:
        today = datetime.date.today()
        print("Today's current date is -", today)
        talk("Today's current date is -" + str(today))

    elif 'tell your story' in command:
        talk("Well, first of my creators wanted to program me based on JASPER which did not work out. Later on, the decision for the Text to Speech engine was made. First, Google gTTS has been discussed, but later on, after some initial struggle they decided on another one")


    elif 'calculate' in command:
        talk("What do you want to calculate?")
        calc=myCommand()

        def get_operator_fn(oper):
            return {
                '+': operator.add, #Befehl ist zum Beispiel "1 plus 1"
                '-': operator.sub, #Befehl ist zum Beispiel "7 minus 4"
                '*': operator.mul, #Befehl ist zum Beispiel "6 multiplied by 5"
                '/': operator.__truediv__, #Befehl ist zum Beispiel "6 divided by 5"
                'Mod': operator.mod,
                'mod': operator.mod,
                '^': operator.pow, #Befehl ist zum Beispiel "7 to the power of 6"
            }[oper]

        def eval_binary_expr(op1, oper, op2):
            op1, op2 = int(op1), int(op2)
            return get_operator_fn(oper)(op1, op2)

        talk("The Result is "+ str((eval_binary_expr(*(calc.split())))))

    elif 'information' in command:
        talk("What would you like to know more about?")
        Input = myCommand()

        talk('Searching...')
        try:
            try:
                res = client.Input(Input)
                outputs = next(res.outputs).text
                talk('Alpha says')
                talk('Gotcha')
                talk(outputs)
            except:
                outputs = wikipedia.summary(Input, sentences=3)
                talk('Gotcha')
                talk('Wikipedia says')
                talk(outputs)
        except:
            talk("No results on wikipedia.")

    elif 'cancel the program' in command:
        talk("Technikum Bot goes offline.")


    else:
        error = random.choice(errors)
        talk(error)

