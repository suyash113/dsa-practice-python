def delete_by_value(self, value):
    if not self.head:
        return False

    current = self.head
    prev = None

    while True:
        if current.data == value:
            if current == self.head:
                # Only one node
                if self.head.next == self.head:
                    self.head = None
                else:
                    # Find the tail node
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next
                    self.head = self.head.next
                    tail.next = self.head
            else:
                prev.next = current.next
            self.length -= 1
            return True

        prev = current
        current = current.next

        if current == self.head:
            break

    return False  # value not found

def delete_by_index(self, index):
    if not self.head or index < 0 or index >= self.length:
        return False

    current = self.head
    prev = None

    if index == 0:
        if self.head == self.tail:
            self.head = None
        else:
            tail = self.head
            while tail.next != self.head:
                tail = tail.next
            self.head = self.head.next
            tail.next = self.head
        self.length -= 1
        return True

    for _ in range(index):
        prev = current
        current = current.next

    prev.next = current.next
    self.length -= 1
    return True
