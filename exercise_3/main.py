import sys
from pathlib import Path
from collections import namedtuple, defaultdict

Log_line = namedtuple('Log_line', ['date', 'time', 'level', 'description'])
Log_level = namedtuple('Log_level', ['info', 'debug', 'error', 'warning'])

log_level = Log_level('INFO', 'DEBUG', 'ERROR', 'WARNING')

log_levels = defaultdict(str)
log_levels['-i'] = log_level.info
log_levels['--info'] = log_level.info
log_levels['-d'] = log_level.debug
log_levels['--debug'] = log_level.debug
log_levels['-e'] = log_level.error
log_levels['--error'] = log_level.error
log_levels['-w'] = log_level.warning
log_levels['--warning'] = log_level.warning

def parse_log_line(line: str) -> dict:
    date, time, level, *rest = line.split(' ')
    log_line = Log_line(date, time, level, ' '.join(rest))

    return log_line



def load_logs(file_path: str) -> list:
    path = Path(file_path)

    if path.exists():
        file = path.read_text('utf-8')
        return [parse_log_line(line.strip()) for line in file.split('\n') if line.strip()]
    
    return []



def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log.level == level]



def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)

    for line in logs:
        counts[line.level] += 1
    
    return counts



def display_log_counts(counts: dict):
    print('Рівень логування | Кількість')
    print('-----------------|----------')
    for k, v in counts.items():
        print(f'{k:<17}| {v}')


def main():
    _, *params = sys.argv
    file_path_param, *level_param = params
    level_param = level_param[0] if len(level_param) > 0 else ''
    level_from_map = log_levels[level_param]

    if level_param and not level_from_map:
        print(f'Second parameter "{level_param}" is specified incorrectly.')
        print(f'Available values are: "{', '.join(list(log_levels.keys())[:-1])}"')
        return


    if file_path_param:
        logs = load_logs(file_path_param)
        if len(logs):
            display_log_counts(count_logs_by_level(logs))

            if level_from_map:
                print(f"\nДеталі логів для рівня '{level_from_map}':")
                for log in filter_logs_by_level(logs, level_from_map):
                    print(f'{log.date} {log.time} - {log.description}')
        else:
            print('Logs are empty or bad file path.')
    else:
        print('Logs file name is not specified.')

if __name__ == "__main__":
    main()
