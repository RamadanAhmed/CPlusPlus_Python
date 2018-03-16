import inspect
import sys


def trace_lines(frame, event, arg):
    """Handler that executes with every line of code"""
    # We only care about *line* and *return* events
    if event != 'line' and event != 'return':
        return

    # Get a reference to the code object and source
    co = frame.f_code
    line_no = frame.f_lineno - co.co_firstlineno
    trace_lines.info_q.put(line_no)
    # Wait for a debug command
    cmd = trace_lines.debugq.get()

    if cmd == "step":
        # If stepping through code, return this handler

        return trace_lines


def trace_calls(frame, event, arg):
    """Handler that executes on every invocation of a function call"""

    # We only care about function call events
    if event != 'call':
        return

    # Get a reference for the code object and function name
    co = frame.f_code
    func_name = co.co_name

    # Only react to the functions we care about
    if func_name in ['main']:
        # Get the source code from the code object
        source = inspect.getsourcelines(co)[0]
        source_len = len(source)
        trace_lines.info_q.put(source_len)
        # Wait for a debug command (we stop here right before stepping into or out of a function)
        cmd = trace_lines.debugq.get()

        if cmd == 'step':
            # If stepping into the function, return the line callback
            return trace_lines
        elif cmd == 'over':
            # If stepping over, then return nothing
            return
    return


def step(debugq):
    """Click handler for the Step Into button"""

    # Tell the debugger we want to step in
    if debugq.empty():
        debugq.put("step")


def stop(debugq):
    """Click handler for the Stop button"""

    # Tell the debugger we're stopping execution
    debugq.put("stop")


def over(debugq):
    """Click handler for the Step Over / Step Out button"""

    # Tell the debugger to step over the next code block
    debugq.put("over")


def debug(debugque, info_q, fn):
    """Sets up and starts the debugger"""

    # Setup the debug and application queues as properties of the trace_lines functions
    trace_lines.debugq = debugque
    trace_lines.info_q = info_q

    # Enable debugging by setting the callback
    sys.settrace(trace_calls)

    # Execute the function we want to debug with its parameters
    fn()
