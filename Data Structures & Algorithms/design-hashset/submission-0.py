class MyHashSet:

    # def __init__(self):
    #     self.data = [False] * 1000001

    # def add(self, key: int) -> None:
    #     self.data[key] = True

    # def remove(self, key: int) -> None:
    #     self.data[key] = False

    # def contains(self, key: int) -> bool:
    #     return self.data[key]
    


    # def __init__(self):
    #     self.data = bytearray(125001)

    # def add(self, key: int) -> None:
    #     byte_index : int = key // 8
    #     bit_index : int = key % 8
    #     self.data[byte_index] |= (1<<bit_index)

    # def remove(self, key: int) -> None:
    #     byte_index : int = key // 8
    #     bit_index : int = key % 8
    #     self.data[byte_index] &= ~(1<<bit_index)

    # def contains(self, key: int) -> bool:
    #     byte_index : int = key // 8
    #     bit_index : int = key % 8
    #     return self.data[byte_index] & (1<<bit_index) != 0
    


    def __init__(self):
        self.data = bytearray(125001)

    def add(self, key: int) -> None:
        self.data[key>>3] |= (1<<(key & 7))

    def remove(self, key: int) -> None:
        self.data[key>>3] &= ~(1<<(key & 7))

    def contains(self, key: int) -> bool:
        return self.data[key>>3] & (1<<(key & 7)) != 0
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)