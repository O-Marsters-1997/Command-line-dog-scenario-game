from scenarios import scenario_list
from scenarios import options_list
from scenarios import outcomes_list
from scenarios import Instruction 
import time

# initial dog stats
stats_dictionary = {'sleepiness': 50, 'hunger':50, 'playfulness':50, 'comfort': 50, 'hydration': 50}

#prompt to start the game 
def ready_to_start():
  opening_q = input('Welcome to the dog game. Are you ready to begin? (Y/N')
  if opening_q.upper() == 'Y':
    print(Instruction)
    input('Press any button when you\'re ready!')
    return gain_info()
  else:
    print('Proceed when you\'re ready')
    time.sleep(2)
    return ready_to_start() 

#Gaining user information  
def gain_info():
  print('\n' *2)

  user_dog = input("what kind of dog do you have?").lower()
  if user_dog == "dachshund":
    print("Well hello Megan, Ruby needs your help")
  else:
    user_name = input('What is your name').capitalize()
    print('Hello', user_name)
    dog_name = input('What is your dog called').capitalize()
    print('Henlo '+ dog_name + ', ' + user_name + ', ' + dog_name + ' needs your help!')
  
  ready_to_play = False
  while not ready_to_play:
    first_q = input('Would you like to play? (Y/N')
    if first_q.upper() == 'Y':
      ready_to_play = True
      return play(0)
    elif first_q.upper() == 'N':
      print(gain_info())
    else:
      print('This is not a valid answer')  



#console loops back to this if lost
def end_game():
  final_result = 'You have been unssucessful on this occasion'
  print(final_result)
  final_answer = input('Would you like to play again?  (Y/N)')
  if final_answer.upper() == 'Y':
    return play(0)
  else:
    return ready_to_start()

def play(days_gone):

  while days_gone < 5:
    day = scenario_list[0]
    time.sleep(2)
    print('Get ready for day ', days_gone + 1)
    print('\n')
    time.sleep(2)
    print(day)
    print('\n')
    while True:
      input1 = input(options_list[0])
      if input1.lower() not in ('a','b','c'):
        print('No')
      else:
        break

#scenarios
    if input1.lower() == 'a':
      if days_gone == 0:
        print('\n', outcomes_list[0],'\n')
        stats_dictionary['playfulness'] -= 30
      elif days_gone == 1: 
        stats_dictionary['sleepiness'] -= 20
        stats_dictionary['playfulness'] += 20
        print('\n', outcomes_list[3], '\n')
      elif days_gone == 2: 
        stats_dictionary['hunger'] += 15
        stats_dictionary['hydration'] += 15
        print('\n', outcomes_list[6], '\n')
      elif days_gone == 3: 
        stats_dictionary['hunger'] -= 5
        stats_dictionary['hydration'] -= 5
        stats_dictionary['comfort'] -= 20 
        print('\n', outcomes_list[9], '\n') 
      elif days_gone == 4: 
        stats_dictionary['comfort'] -= 15
        stats_dictionary['sleepiness'] -= 10  
        print('\n', outcomes_list[12], '\n')
    
    elif input1.lower() == 'b':
      if days_gone == 0:
        print('\n', outcomes_list[1], '\n')
        stats_dictionary['sleepiness'] += 15
        stats_dictionary['playfulness'] += 15
      elif days_gone == 1: 
        print('\n', outcomes_list[4], '\n')
        stats_dictionary['playfulness'] -= 10
        stats_dictionary['hunger'] += 10
      elif days_gone == 2: 
        print('\n', outcomes_list[7], '\n')
        stats_dictionary['hunger'] += 5
        stats_dictionary['hydration'] += 5
      elif days_gone == 3: 
        print('\n', outcomes_list[10], '\n')
        stats_dictionary['hunger'] -= 10
        stats_dictionary['hydration'] -= 10
        stats_dictionary['comfort'] += 10
      elif days_gone == 4: 
        print('\n', outcomes_list[13], '\n')
        stats_dictionary['comfort'] += 15
        stats_dictionary['sleepiness'] -= 10

        
      
    elif input1.lower() == 'c':
      if days_gone == 0:
        print('\n', outcomes_list[2], '\n')
        stats_dictionary['playfulness'] -= 10
      elif days_gone == 1: 
        print('\n', outcomes_list[5], '\n')
        stats_dictionary['sleepiness'] += 15
      elif days_gone == 2: 
        print('\n',outcomes_list[8],'\n')
        stats_dictionary['hunger'] += 15
        stats_dictionary['hydration'] += 15
      elif days_gone == 3: 
        print('\n',outcomes_list[11],'\n')
        stats_dictionary['hunger'] += 15
        stats_dictionary['hydration'] += 15
        stats_dictionary['comfort'] += 15
      elif days_gone == 4: 
        print('\n',outcomes_list[14],'\n')
        stats_dictionary['sleepiness'] -= 20
        stats_dictionary['hunger'] -= 20
        stats_dictionary['hydration'] -= 20
        stats_dictionary['playfulness'] -= 20
        stats_dictionary['comfort'] -= 50

          
    print(stats_dictionary)
    
    critical_dictionary = dict((k,v) for k,v in 
    stats_dictionary.items() if v > 90 or v < 10)

    if len(critical_dictionary) == 0:
      scenario_list.pop(0)
      options_list.pop(0)
      return play(days_gone + 1)
    else:
      print('You have failed to make sure your dog is healthy this week. \nHowever, you should try again!')
      return end_game()

  else:
    input('Congratulations, \nClick anywhere to play again')
    return ready_to_start() 


if __name__ == '__main__':
  print(ready_to_start())