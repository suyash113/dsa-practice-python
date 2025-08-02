def delete_by_value(self, value):
    if not self.head:
        return False

    current = self.head
    for _ in range(self.length):
        if current.data == value:
            if self.length == 1:
                self.head = self.tail = None
            elif current == self.head:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
            elif current == self.tail:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
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

    current = self.head
    for _ in range(index):
        current = current.next

    if self.length == 1:
        self.head = self.tail = None
    elif current == self.head:
        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head
    elif current == self.tail:
        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail
    else:
        current.prev.next = current.next
        current.next.prev = current.prev

    self.length -= 1
    return True
