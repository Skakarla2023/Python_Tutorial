# 🧠 Exceptions in Python

- When you run a code, in the end of your output you will find something like **exit code 0**, which means your program executed successfully with **0 errors**.
- Any value other than 0 means trash, i.e., we have got some errors.
- In Python we perform exception handling using the three keywords : **try, catch** and **finally**.


- Observe the following code:

```python
try:
    age = int(input('Age:'))
    print(age)
except ValueError:
    print("Invalid value")
finally:
    print("Code executed successfully")
```

Output:
```
Age:sad
Invalid value
Code executed successfully
```


