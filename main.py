import random
import time

finished = False
already = []
tries = 1

def generate(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return random.randint(range_start, range_end)

def main():
    global tries
    num = input("Enter the number you want to try out: ")
    start_time = time.time()  # Get the start time before the loop starts
    while not finished:
        n = generate(len(num))
        tries += 1
        if n in already:
            continue
        if int(n) == int(num):
            end_time = time.time()  # Get the end time when the loop ends
            duration = end_time - start_time  # Calculate the duration of the loop
            print(f"Finished! Number generated!\nStats:\n- Number of tries: {tries}\n- Duration: {duration:.2f} seconds\n")
            break
        else:
            already.append(n)
            print(f"Invalid Number: {n}")
            continue

if __name__ == '__main__':
    main()
