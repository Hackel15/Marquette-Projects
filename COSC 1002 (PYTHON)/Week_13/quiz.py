def validate(card):
      card = list(str(card))
      odd = [ int(card[o]) for o in range(1,len(card),2) ]
      even = [ int(card[e]) for e in range(0,len(card),2) ]

      if ((sum(odd)%10==0) and ((sum(even)*2)%10==0)):
            return True
      return False
