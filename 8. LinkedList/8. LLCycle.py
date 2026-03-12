def hasCycle(self, head) -> bool:
        temp = head
        seen = {}
        while (temp is not None):
            if(temp.next not in seen):
                seen[temp.next] = 1
                temp = temp.next
            else:
                return True
        return False