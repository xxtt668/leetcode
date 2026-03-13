from typing import List
from typing import Optional



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1=[2,4,3]
list2=[5,6,4]
list3=[]
def create_link_listnode(lst):
    dummmy=ListNode(0)
    current=dummmy
    for val in lst:
        current.next=ListNode(val)
        current=current.next
    return dummmy.next

l1=create_link_listnode(list1)
l2=create_link_listnode(list2)

current=l1
print(current.next.val)


def traverse_listnode(list_node):
    current=list_node
    values=[]
    while current:
        values.append(str(current.val))
        current=current.next
    print("脸标志","->".join(values))
traverse_listnode(l1)




class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=ListNode(0)
        current3=l3

        current1=l1
        current2=l2
        while current1 and current2:
            current3.next.val=current1.val+current2.val
            if current3.next.val>9:
                current3.next.val=current3.next.val %10
                current3.next.next.val+=1
                current3=current3.next


