def delete_by_value(self, value):
    if not self.head:
        return False

    if self.head.data == value:
        self.head = self.head.next
        self.length -= 1
        return True

    prev = self.head
    current = self.head.next
    while current:
        if current.data == value:
            prev.next = current.next
            self.length -= 1
            return True
        prev = current
        current = current.next

    return False

def delete_by_index(self, index):
    if index < 0 or index >= self.length or not self.head:
        return False

    if index == 0:
        self.head = self.head.next
        self.length -= 1
        return True

    current = self.head
    for _ in range(index - 1):
        current = current.next

    current.next = current.next.next
    self.length -= 1
    return True
