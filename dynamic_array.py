import ctypes

class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        for ele in range(self.count - 1 , i - 1, -1):
            self.array[ele+1] = self.array[ele]
        self.array[i] = itm
        self.count = self.count + 1

    def delete(self, i):
        if self.count == self.capacity // 2:
            self.resize(self.capacity // 2)
        new_array = self.make_array(self.capacity)
        
        for ele in range(self.count - 1):
            if ele < i:
                new_array[ele] = self.array[ele]
            else:
                new_array[ele] = self.array[ele + 1]
        
        self.count = self.count - 1
        self.array = new_array



da = DynArray()
for i in range(5):
    da.append(i)
    print(da[i])

da.insert(2, 101)
print("__________")
for i in range(da.__len__()):
    print(da[i])
print("__________")
da.delete(2)
for i in range(da.__len__()):
    print(da[i])
