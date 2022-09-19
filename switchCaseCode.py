def monday():
    return "monday"
def tuesday():
    return "tuesday"
def wednesday():
    return "wednesday"
def thursday():
    return "thursday"
def friday():
    return "friday"
def saturday():
    return "saturday"
def sunday():
    return "sunday"
def default():
    return "Invalid day"
switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
}
def switch(dayOfWeek):
    return switcher.get(dayOfWeek, default)()
print(switch(1))
print(switch(0))


def vowel(num):
    switch={
      1:'a',
      2:'e',
      3:'i',
      4:'o',
      5:'u'
      }
    return switch.get(num,"Invalid input")
vowel(3)
vowel(0)


def add():
    return n+m

def subs():
    return n-m

def prod():
    return n*m

def div():
    return m/n

def rem():
    return m%n

def operations(op):
    switch={
       '+': add(),
       '-': subs(),
       '*': prod(),
       '/': div(),
       '%': rem(),
       }
    return switch.get(op,'Choose one of the following operator:+,-,*,/,%')

operations('*')

operations('^')