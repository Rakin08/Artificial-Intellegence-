import random
def tableDrivenAgent(percept):
    percepts=[]
    table={
    (('A','Clean'),): 'Right',
    (('A','Dirty'),): 'Suck',
    (('B','Clean'),): 'Left',
    (('B','Dirty'),): 'Suck'
    }
   percepts.append(percept)
   
   action=table[tuple(percepts)]
   
   return action
 loc_A,loc_B='A','B'
 location=random.choice([loc_A,loc_B])
 status=random.choice(['Clean','Dirty'])
 
 percept=(location,status)
 location=tableDrivenAgent(percept)
 print('Agent has percieved : ',percept, ' and performed action: ',action)
