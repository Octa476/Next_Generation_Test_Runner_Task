# Next_Generation_Test_Runner_Task

## How to run the app

1. Clone the repository on your local machine:

```bash
https://github.com/Octa476/Next_Generation_Test_Runner_Task.git
```
2. Navigate to the project directory:
```bash
cd Next_Generation_Test_Runner_Task
```

3. Run the app:

- On Linux and Mac:
```bash
python3 program_B.py program_A.py
```

- On Windows:
```bash
python program_B.py program_A.py
```

## How it works

The script **program_B.py** starts a subprocess by running the script **program_A.py**. The two programs comunicate via
**stdin** and **stdout** in this specific way:
* when the **subprocess** is created the stdin and stdout of it is connected with the main process by the <**subprocess.PIPE**>
(in this way the main process controls the flow of data to his child process);
* running a command like <**process.stdin.write(b'Hi\n')**> sends the byte string <**b'Hi\n'**> to the stdin of the subprocess;
* the loop <**for line in sys.stdin:**> takes the last written line of its stdin and excutes a command based on the
<**line**> string;
* if the executed command is a <**print**> then that string printed is saved in a buffer which is then flushed to the stdout
using <**sys.stdout.flush()**>;
* after the flush, the main process has access to that <**byte string**> which is then converted into a normal string that can be
later used in the process;
* the subprocess is ended gracefully when no input is provided to the stdin or the <**"Shutdown"**> command is provided because there
will be no <**line**> from <**sys.stdin**> to be read or the break statement will cause the loop to end itself;   





