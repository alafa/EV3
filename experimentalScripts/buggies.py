import ev3dev.ev3 as ev3

class Buggy:
    """Little bugs that some shine and others doesnt"""
    def __init__(self, lightON):
        self.__lighting = lightON
    def seeIfShinning(self):
        return self.__lighting

# We have an array of the buffys we have
myBugies = []

# We are going to create 10little bugs
# The touch sensor of the EV3 will tell if they are shinning or not
for x in range(0, 10):
    print "We're on buggy %d" % (x)
    myBugies.append(Buggy(ev3.TouchSensor().value))

for b in myBugies:
    if myBugies[b].seeIfShinning():
        print "Buggy number %d is Shinning!! :D" % (b)
    else:
        print "Buggy number %d is not shinning... :(" % (b)

#while True:
#    print tauched.value()
#    ev3.Leds.set_color(ev3.Leds.LEFT, (ev3.Leds.GREEN, ev3.Leds.RED)[tauched.value()])
