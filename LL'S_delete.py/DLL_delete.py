def delete_by_value(self, value):
    current = self.head
    while current:
        if current.data == value:
            if current == self.head:
                self.head = current.next
                if self.head:
                    self.head.prev = None
            elif current == self.tail:
                self.tail = current.prev
                self.tail.next = None
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
            self.length -= 1
            return True
        current = current.next
    return False

def delete_by_index(self, index):
    if index < 0 or index >= self.length or not self.head:
        return False

    if index == 0:
        self.tail = self.head
        if self.head:
            self.head.prev = None
        self.length -= 1
        return True

    if index == self.length - 1:
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1
        return True

    current = self.head
    for _ in range(index):
        current = current.next

    current.prev.next = current.next
    current.next.prev = current.prev
    self.length -= 1
    return True
