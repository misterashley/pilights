import time, random

spi = open('/dev/spidev0.1','w') #unbuffered
i = 0
number_of_leds = 20
led = [1,1,1]
led_state = []
for x in range(0,number_of_leds):
    led_state.append(led)



def random_colour():
    return [random.randrange(0,256),random.randrange(0,256),random.randrange(0,256)]

def mix():
    global led_state
    led_state = []
    for i in range(0,number_of_leds):
        led_state.append(random_colour())
    push_state()
        
    
def leds_off():
    set_leds(0,0,0)

def show(r,g,b):
    print "red "+str(r)+" green "+str(g)+" blue "+str(b)

def set_leds(r,g,b):
    spi.write((chr(b)+chr(r)+chr(g))*number_of_leds)
    spi.flush()
    time.sleep(0.001)

def set_a_led(led_address,r,g,b):
    global number_of_leds
    if (led_address > number_of_leds or led_address < 0): pass
    else:
        if led_address > 0:
            spi.write(chr(b)+chr(r)+chr(g))
            spi.flush()
            leds_remaining = led_address - 1
            show(r,b,g)
        else:
            leds_remaining = number_of_leds
    return leds_remaining

def push_state():
    global led_state 
    for i in led_state:
        spi.write(chr(i[0])+chr(i[1])+chr(i[2]))
        spi.flush()


##def fade_leds(state,num_leds):
##    for i in num_leds

def fade():
    global led_state
    global number_of_leds
    print "fade loop "+str(led_state) #[[0,0,0],[0,0,0]]
    for x in range(0,255):
        for i in range(0,number_of_leds):
            print led_state[i][0]
            if led_state[i][0] > 0 : led_state[i][0] -= 1
            if led_state[i][1] > 0 : led_state[i][1] -= 1
            if led_state[i][2] > 0 : led_state[i][2] -= 1
            #print 'after loop ' +str(led_state)
            push_state()

def red2green():
    r=0
    g=200
    b=0
    some_led = number_of_leds
    while g > 0:
        g -= 10
        r += 10
        some_led = set_a_led(some_led,r,g,b)
    set_a_led(some_led,r,g,b)

def xmas():
    while True:
        spi.write((chr(0)+chr(150)+chr(0)+chr(0)+chr(0)+chr(150))*10)
        spi.flush()
        time.sleep(random.random())
        spi.write((chr(0)+chr(0)+chr(150)+chr(0)+chr(150)+chr(0))*10)
        spi.flush()
        time.sleep(random.random())
                  
def sparkle(): pass
##    choose a light
##    turn on the light full blast, and soon after diminish until low light level


def init_led():
    r=0
    b=0
    g=150
    while g:
        r += 1
        g -= 1
        set_leds(r,g,b)
    
    while r:
        b += 1
        r -= 1
        set_leds(r,g,b)

    while b:
        g += 1
        b -= 1
        set_leds(r,g,b)


init_led()
#fade(led_state,number_of_leds)
push_state()
##spi.flush()
