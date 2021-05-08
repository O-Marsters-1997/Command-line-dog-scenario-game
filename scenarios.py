scenario_list = [ 
'Day 1:     You are taking your dog for a walk, it sees a much bigger dog and gestures that it wants to say hello, do  you?:', 
  
'Day 2:   You are finishing your work for the day, before heading out to walk your dog. But your work is taking longer than expected, do you?', 
  
'Day 3:   Your dog has not been eating properly so you had planned to drive into town to get their favourite treats to encourage them to. However your car is broken, do you?', 
  
'Day 4:   Your dog normally sleeps in your room but the window is broken. You are worried about them being cold, do you?',
  
'Day 5:   Your dog has a problem with its leg and needs to go to the vet. As it happens its friend from across the road needs to go too but its owner cn only take them towards the end of the day. You know your dog will be happier with their friend there, so do you?']

options_list = [
#Day 1
['a)  Let your dog off the lead to go play', 'b)  Hold your dog back', 'c)  approach cautiously with your dog on the lead'],

#Day 2
['a)  Finish your work and take your dog out for a longer walk tomorrow','b)  Take your dog for as long a walk as you were planning, despite it setting you back later','c)   Take your dog for a smaller walk now and then finish your work later this evening'],

#Day 3
['a)  Call a mechanic out and hope that you can get to the dog shop before it closes','b)   Spend extra time playing with them and hope that that makes them happy enough to eat their food', 'Walk to a more local shop and get some treats, even if they aren\'t their favourite'],

#Day 4
['a)   Try to close the window as best you can and give your dog extra blankets','b)   Start off with your dog in your room, but set an alarm for the middle of the night so you can check on them and move them if necessary', 'c)   Set up your dog\'s bed in the kitchen'],

#Day 5
['a)  Wait until the end of the day so that your dog can go to the vet with their friend','b)   Take your dog to the vet as soon as possible','c)   Wait until tomrrow so that the dogs can go together at an earlier time of the day']] 

outcomes_list = [
#Day 1
'The big dog runs at yours\', your dog is timid. Their playfulness has been adversely affected', 'Your dog whines because they haven\'t been able to play properly. They become restless and their playfulness and sleepiness has been affected', 'The big dog runs at yours, but you are ble to get in the way and stop your dog from becoming too skittish. Your dog\'s playfulness has marginally been affected.',

#Day 2
'Your dog becomes very restless. Their playfulness and sleepiness have been drastically affected', 'Your dog is very happy at first, but then you snap at them as you are very stressed, making them sad and putting them off their food. Their hunger and playfulness have been affected', 'Your dog is not as happy as possible but able to get to sleep. Their sleepiness has been affected.',

#Day 3
'The mechanic doesn\'t arrive in time and you are unable to make your dog eat at all. Their hunger and hydration has been affected.', 'Although your dog is still not eating properly, they are happy enough that they eat a little bit. Their hunger and hydration has been slightly affected', 'Your dog doesn\'t like these treats and refuses to eat. Their hunger and hydration has been affected.',

#Day 4
'Your dog is cold and uncomfortable during the night. But tthey are able to wake you up when they want to be fed. Their hunger, hydration and comfort have been affected', 'You wake to find that your dog is uncomfortable so you take them into the other room. You give them some treats so they settle down and they aren\'t as hungry in the morning. Their hunger, hydration and comfort have been affected', 'Your dog has a more comfortable night sleep but they aren\'t able to eat until you wake up. Their hunger, hydration and comfort have been affected',

#Day 5
'Your dog\'s leg will take longer to fix than you first thought. They must come back tomorrow and their comfort and playfulness have been affected', 'Your dog does not like the vet but their leg has been mended today and they are much happier. Their comfort has been affected','Your dog\'s leg continues to get worse and they are in a lot of pain. All of their statistics are affected'] 




Instruction = 'Your job is to make sure that your dog remains healthy and happyduring the week. \nYour dog starts with a rating of 50 for each of its core statistics. \nThese are as follows: \nSleepiness: 50 \nHunger: 50 \nplayfulness: 50 \nComfort: 50 \nHydration: 50 \n\nYou must think about what you should do each day and make sure that none of your dog\'s statistics reaches less than 20 nor higher than 90 \nGood luck!' 

#options for each scenaio
#1)  Let your dog off the lead to go play2) Hold your dog back until the bigger dog has gone 3)  Make your way cautiously towards it''