class Solution(object):
    def middleNode(self, head):

        count = 0
        temp = head

        while temp:
            count += 1
            temp = temp.next

        temp = head

        for _ in range(count // 2):
            temp = temp.next

        return temp