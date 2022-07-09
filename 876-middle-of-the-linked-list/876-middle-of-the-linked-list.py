# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        node_array = []
        
        curr_node = head
        while curr_node != None:
            node_array.append(curr_node)
            curr_node = curr_node.next
            
        return node_array[len(node_array)//2]           
            
        