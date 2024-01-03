# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Lets initiate a newlist with none 
        new_list = None
        #Lets create pointer, which always points to head
        curr = head

        # while making sure curr pointer is not none, we can traverse the original linkked list to build the reverse linked list
        while curr:
            next_node = curr.next # keeping track of next node in current linked list and this next_node pointer is used to traverse the original linked list
            curr.next = new_list # This way we can severe the connection between current node in original linked list with the next node in the orginal linked list
            new_list = curr # pointing new_list to the curr value. This keeps the new list always pointed to the head of the new list
            curr = next_node # we are using next node to initate the curr variable this way is curr is always the head of orginal linked list 
            # and this loop is iterated until curr becomes none

        return new_list