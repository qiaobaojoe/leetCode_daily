class MyHashMap:

    def __init__(self):
        self.val = [-1] * (10 ** 10)

    def put(self, key: int, value: int) -> None:
        self.val[key] = value

    def get(self, key: int) -> int:
        return self.val[key]

    def remove(self, key: int) -> None:
        self.val[key] = -1

    
if __name__ == "__main__" :
    my_map = MyHashMap()
    my_map.put(1,1)
    print(my_map.get(2))
    print(my_map.get(3))
