class Counter:
    count = 0  # class variable (sab objects ke liye same hota hai)

    def __init__(self):
        Counter.count += 1  # jab object banta hai, count +1 hota hai

    @classmethod
    def show_count(cls):
        print("Total objects created:", cls.count)

# Ab object banate hain
c1 = Counter()
c2 = Counter()
c3 = Counter()

# Total count check karte hain
Counter.show_count()
