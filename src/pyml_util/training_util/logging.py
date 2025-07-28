from pathlib import Path
from time import perf_counter
from datetime import datetime

def log_training(logfile_path: str|Path):
    
    outpath_abs = Path(logfile_path).resolve()

    def decorator(func):
        def wrapper(*args, **kwargs):
            init_time = perf_counter()

            func(*args, **kwargs)

            end_time = perf_counter()
            timestamp = datetime.strftime(datetime.now(), "%Y/%m/%d-%H:%M:%S:%f")
            args = (func.__name__, timestamp, (end_time-init_time)*1000)

            if not outpath_abs.exists():
                with open(outpath_abs, "w") as writer:
                    writer.write("func_name, execute_timestamp, execute_duration_ms\n")

            with open(outpath_abs, "a") as appender:
                appender.write(", ".join(map(str, args)) + "\n")

        return wrapper
    return decorator