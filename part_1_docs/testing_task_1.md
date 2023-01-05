### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:  # Needs to be double equals to assess equality in an if statement
      return True
    else  # Colon after 'else' missing
      return False
   

  dif highest_card(self, card1 card2):  # Needs to be 'def' at start and a comma between 'card1' and 'card2'
  # The following four lines should all be indented by 1 to sit within the highest_card function
  if card1.value > card2.value:
    return card  # 'card' is not a valid variable, needs to be 'card1'
  else:
    return card2
  


def cards_total(self, cards):  # Needs to be indented to be included in the class 
  total  # No starting value assigned to 'total' variable
  for card in cards:
    total += card.value
    return "You have a total of" + total  # This line should not be indented within for loop as will currently only return total after first card, also needs to either be an f string or the total variable will need to be converted to a string value for concatenation.
  
```
