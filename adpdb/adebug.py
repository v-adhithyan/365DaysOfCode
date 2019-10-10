import sys

def sample(a, b):
    x = a + b
    y = x * 2
    print("Sample: " + str(y))

def trace_calls(frame, event, arg):
    if frame.f_code.co_name == "sample":
        print(frame.f_code)

sys.settrace(trace_calls)
