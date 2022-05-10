# Wolf goat cabbage game
# PEAS:
    1- performance measure : success the goal
    2- environment :boat,river,human,wolf,goat,cabbage
    3- actuator : let user to move in the environment 
    4- sensor : screen , mouse , keyboard 
  
 # ODESA:
     1- observability : fully observable 
     2-deterministic: deterministic
     3-  episode:sequential
     4- static: static
     5- agent: single agent 
     
# Type of agent:
Goal-based agent.

# Problem Formulation:

  # Initial state :
    wolf, goat , cabbage at the first bank waiting to be transferred to the other bank , farmer has to carry one thing with him 
  # Successor function : 
    - Step 1 : farmer takes the goat with him and leaves it on the other bank 
    - Step 2 :the farmer returns and take the cabbage to the other side and take the goat back 
    - Step 3: the farmer leaves the goat on the first bank and take the wolf with him to the other bank
    - Step 4 : the farmer leaves the wolf with the cabbage and return to bring the goat 
    - Step 5 :the farmer returns and bring the goat and return to the other bank 


