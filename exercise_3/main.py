import sys
from pathlib import Path
from collections import namedtuple, defaultdict

LogLine = namedtuple('LogLine', ['date', 'time', 'level', 'description'])
log_levels = ('INFO', 'DEBUG', 'ERROR', 'WARNING')


def parse_log_line(line: str) -> LogLine:
    date, time, level, *rest = line.split(' ')
    return LogLine(date, time, level, ' '.join(rest))


def load_logs(file_path: str) -> list:
    path = Path(file_path)

    if path.exists() and path.is_file():
        with open(path.resolve(), 'r', encoding='utf-8') as file:
            return [parse_log_line(line.strip()) for line in file if line.strip()]

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
    try:
        logs = load_logs(sys.argv[1])
        log_level_filter = sys.argv[2] if len(sys.argv) > 2 else ''

        if len(logs) > 0:
            display_log_counts(count_logs_by_level(logs))

            if log_level_filter:
                log_level_upper = log_level_filter.upper()

                if log_level_upper in log_levels:
                    print(f"\nДеталі логів для рівня '{log_level_upper}':")
                    for log in filter_logs_by_level(logs, log_level_upper):
                        print(f'{log.date} {log.time} - {log.description}')
        else:
            print('Logs are empty or file path is incorrect.')
    except IndexError:
        print('Enter logs file path.')


if __name__ == "__main__":
    main()
