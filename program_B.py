import subprocess
import sys

file_name = sys.argv[1]

process = subprocess.Popen([sys.executable, file_name], stdin=subprocess.PIPE, 
                            stdout=subprocess.PIPE, bufsize=0)

process.stdin.write(b'Hi\n')
decoded_string = process.stdout.readline().decode("utf-8")
if decoded_string != "Hi\n":
     raise Exception("The program responded with an incorrect output1")

nums = []
for i in range(0, 100):
    process.stdin.write(b'GetRandom\n')
    decoded_string = process.stdout.readline().decode("utf-8")
    num = int(decoded_string[0 : len(decoded_string) - 1])
    nums.append(num)

process.stdin.write(b'Shutdown\n')
decoded_string = process.stdout.readline().decode("utf-8")
nums.sort()
print(nums)
print(nums[49])
sum = 0
for num in nums:
    sum += num
print(num / 100)
