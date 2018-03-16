import tqdm
import multiprocessing
import keyboard
from test_debugger import main
from debugger import debug, step


def wrap():
    pause_flag = False
    # Initialize the debug and application queues for passing messages
    debug_q = multiprocessing.Queue()
    info_q = multiprocessing.Queue()
    # Create the debug process
    debug_process = multiprocessing.Process(target=debug, args=(debug_q, info_q, main,))
    debug_process.start()
    num_lines = info_q.get()
    last_number = 0
    pbar = tqdm.tqdm(total=num_lines)
    while debug_process.is_alive():
        if not pause_flag:
            step(debug_q)
            if not info_q.empty():
                line_number = info_q.get()
                if line_number > last_number:
                    pbar.update(1)
                    last_number = line_number
        if keyboard.is_pressed('s'):
            break
        elif keyboard.is_pressed('c'):
            pause_flag = False
        elif keyboard.is_pressed('p') or pause_flag:
            pause_flag = True
    debug_process.terminate()
    debug_q.close()
    info_q.close()
    pbar.n = num_lines


wrap()

