class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("no negative please.")
        self._capacity = capacity
        self._size = 0 

    def __str__(self):
        return f"{'🍪' * self._size}"

    def deposit(self, put_jar):
        if put_jar < 0:
            raise ValueError("really? negative?.")
        if self._size + put_jar > self._capacity:
            raise ValueError("too much cookies!")
        self._size += put_jar

    def withdraw(self, take_jar):
        if take_jar < 0:
            raise ValueError("Really? Negative??")
        if self._size - take_jar < 0:
            raise ValueError("damn, we need cookies.")
        self._size -= take_jar

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar() 
    while True:
        try:
            action_jar = input("Do you want to put or take cookies? ").strip().lower()
            if action_jar == "put":
                put_jar = int(input("How many? "))
                jar.deposit(put_jar)
            elif action_jar == "take":
                take_jar = int(input("How many? "))
                jar.withdraw(take_jar)
            else:
                print("choose 'put' or 'take'.")
                continue
            print(f"Jar now: {jar}") 
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
