#using toritoise and hare algirthm here 
"""
one pointer rune 1 node at once. and the second one rune 2 nodes at once 


"""

class Solution(object):
    def middleNode(self, head):

        #using tortoise and hare algorithm 
        count = 0 
        temp = head
        one = head #tortoise
        two = head #hare

        while temp:
            temp = temp.next
            count+=1
        
        while two:
          
            two = two.next
            if two:
                two = two.next  ##remeber here that we need to verify the two pointer first adn then the one pointer. 
            else:
                break
            one = one.next
        
        # if count % 2 == 0:
        #     one = one.next
        
        return one
        
