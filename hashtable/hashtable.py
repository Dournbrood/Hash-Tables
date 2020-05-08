import math


class HashTableEntry:
    def __init__(self, value):
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.load = 0
        self.capacity = capacity
        self.storage = [None] * math.ceil(capacity)

    def djb2(self, key):
        my_hash = 5381

        encoded_key = str(key).encode()

        for char in encoded_key:
            my_hash = my_hash * 33 + char

        return my_hash

    def hash_index(self, key):
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        index = self.hash_index(key)

        new = HashTableEntry((key, value))

        if self.storage[index] == None:
            self.storage[index] = new
            self.load += 1
            return new

        current = self.storage[index]
        previous = None

        while current is not None:
            if current.value[0] == key:
                current.value = (key, value)
                return new

            previous = current
            current = current.next

        previous.next = new
        self.load += 1
        return new

    def delete(self, key):
        index = self.hash_index(key)

        current = self.storage[index]

        if current.value[0] == key:
            old_head = self.storage[index]
            self.storage[index] = self.storage[index].next
            old_head.next = None
            self.load -= 1
            return current

        previous = None

        while current is not None:
            if current.value[0] == key:
                # Found it
                if previous is not None:
                    previous.next = current.next
                current.next = None
                self.load -= 1
                return current

            previous = current
            current = current.next

        return None

    def get(self, key):
        index = self.hash_index(key)

        current = self.storage[index]

        if current == None:
            return None

        while current is not None:
            if current.value[0] == key:
                return current.value[1]

            current = current.next

        return None

    def resize(self):
        if self.load / self.capacity < 0.2:
            new_table = HashTable(self.capacity * 0.5)

            for head in self.storage:
                current = head

                while current is not None:
                    new_table.put(current.value[0], current.value[1])

                    current = current.next

            self.storage = new_table.storage
            self.capacity = new_table.capacity

            new_table == None

        if self.load / self.capacity > 0.7:
            new_table = HashTable(self.capacity * 2)

            for head in self.storage:
                current = head

                while current is not None:
                    new_table.put(current.value[0], current.value[1])

                    current = current.next

            self.storage = new_table.storage
            self.capacity = new_table.capacity

            new_table == None


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
