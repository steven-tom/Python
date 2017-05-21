class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    """

    def __init__(self, value=0, previous=0):
        self.value = value
        self.previous=previous

    def next(self):
        "*** YOUR CODE HERE ***"

        if self.value==self.previous==0:
            self.value=1
            return Fib(self.value, self.previous)

        elif self.previous==0:
            self.previous=self.value
            return Fib(self.value)

        else:
            self.previous, self.value= self.value, self.value+self.previous
            return Fib(self.value)



    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, item, price , quantity=0, balance=0):
        self.item=item
        self.price=price
        self.quantity=quantity
        self.balance=0

    def vend(self):
        difference=self.balance-self.price
        if self.quantity<1:
            return('Machine is out of stock.')
        elif difference<0:
            return('You must deposit $'+str( abs(difference))+' more.')
        else:
            self.balance=0
            self.quantity-=1
            if difference==0:
                return('Here is your '+str(self.item)+'.')
            return('Here is your '+str(self.item)+' and $'+str(difference)+' change.')


    def deposit(self, balance):
        self.balance+=balance
        if self.quantity==0:
            return('Machine is out of stock. Here is your $'+str(self.balance)+'.')

        return('Current balance: $'+str(self.balance))


    def restock(self, quantity):
        self.quantity+=quantity
        return ('Current '+str(self.item)+' stock: '+str(self.quantity))


class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> double_fussy = MissManners(m) # Composed MissManners objects
    >>> double_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> double_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> double_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> double_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    def __init__(self, obj):
        self.obj = obj

    def ask(self, message, *args):
        magic_word = 'please '
        if not message.startswith(magic_word):
            return 'You must learn to say please first.'
        else:
            #check_message=message.replace("please ","")
            check_message=message[7:]

            if hasattr(self.obj, check_message):
                func=getattr(self.obj,check_message)
                return func(*args)
            else:
                return('Thanks for asking, but I know not how to '+check_message+".")
            

            #check if function is in vending class
            #self.obj.message(*args)

