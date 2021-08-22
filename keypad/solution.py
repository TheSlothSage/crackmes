

# Figuring out a specific combination for this one is hard

# Functions are direct copies of the logic in each on cick hook in the binary used as example. 

def on_click_zero (state):
    state += 0x1000441
    return state

def on_click_one (state):
    state = (state % 7) * 100
    return state

def on_click_two (state):
    state -= 0x539  
    return state

def on_click_three (state):
    state = (state * 0x58 + 8) * 5000
    return state

def on_click_four (state):
    var1 = (state * 100 + 50000) % 0xd
    var2 = var1 + 0x44

    if var2 < 0x4c :
        state = var1 + 0x44
    else:
        state = var2 * 10

    return state

def on_click_five (state):
    state += 10000
    return state

def on_click_six (state):
   state += 0x11112222
    if 0x1ea7b3f < state:
       state = state ^ 0xdeadc03e

    state = state / 0x4d 

    return state

def on_click_seven (state):
        # this does something weird and dumb in the code... 
    return state

def on_click_eight (state):
    state += 0x14cc5
    return state

def on_click_nine (state):
    state = state * (state % 3)
    return state 

def reset (state):
    state = 0
    return state

def confirm (state):
   
    if state != 0x1746e:
        print "key found"
        return reset (state) 

# unforntuately a keygen program would be very difficult the method is pretty much intractible unless someone is seeing something I am not

