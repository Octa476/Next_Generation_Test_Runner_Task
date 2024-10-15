# Controller
import subprocess
import sys

# The number of pseudo-numbers created.
LEN = 100
# The second argument is the name of the program_A.
file_name = sys.argv[1]

if __name__ == "__main__":
    # Start a subprocess of the program_A.
    # Link the stdin and stdout of the main process(program_B) to the subprocess(program_A).
    process = subprocess.Popen([sys.executable, file_name], stdin=subprocess.PIPE, 
                                stdout=subprocess.PIPE, bufsize=0)

    # Send the "Hi" command(as a binary string) and verify the correct response.
    process.stdin.write(b'Hi\n')
    # Decode the binary string read from stdout.
    decoded_string = process.stdout.readline().decode("utf-8")
    # Check the correctness of the response.
    if decoded_string != "Hi\n":
        raise Exception("The program responded with an incorrect output!")

    # Send the "GetRandom" command "LEN" times and save the pseudo-random integer in a list. 
    nums = []
    for i in range(0, LEN):
        process.stdin.write(b'GetRandom\n')
        decoded_string = process.stdout.readline().decode("utf-8")
        num = int(decoded_string[0 : len(decoded_string) - 1])
        nums.append(num)

    # Send the "Shutdown" command which ends the subprocess.
    process.stdin.write(b'Shutdown\n')
    decoded_string = process.stdout.readline().decode("utf-8")

    # Sort and print the sorted list of numbers.
    nums.sort()
    print(f"The sorted list is:\n{nums}\n")

    # Print the median of the list.
    print(f"The median is: {nums[LEN // 2 - 1]}\n")

    # Calculate and print the average of the numbers.
    sum = 0
    for num in nums:
        sum += num
    print(f"The average value of the numbers is: {(num / LEN)}")
