import sys
import os

def create_log_file(file_path):
    logs = """2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 09:15:10 INFO Data export completed.
2024-01-22 10:30:55 WARNING Disk usage above 80%.
2024-01-22 11:05:00 DEBUG Starting data backup process.
2024-01-22 11:30:15 ERROR Backup process failed.
2024-01-22 12:00:00 INFO User logged out.
2024-01-22 12:45:05 DEBUG Checking system health.
2024-01-22 13:30:30 INFO Scheduled maintenance."""
    with open(file_path, "w") as file:
        file.write(logs)

def parse_log_line(line):
    parts = line.split(" ", 3)
    if len(parts) < 4:
        return None
    return {"date": parts[0], "time": parts[1], "level": parts[2], "message": parts[3]}

def load_logs(file_path):
    logs = []
    with open(file_path, "r") as file:
        for line in file:
            log_entry = parse_log_line(line.strip())
            if log_entry:
                logs.append(log_entry)
    return logs

def count_logs_by_level(logs):
    counts = {}
    for log in logs:
        counts[log["level"]] = counts.get(log["level"], 0) + 1
    return counts

def display_log_counts(counts):
    print("Рівень логування | Кількість")
    print("-" * 25)
    for level, count in counts.items():
        print(f"{level:<15} | {count}")

def filter_logs_by_level(logs, level):
    return [log for log in logs if log["level"].lower() == level.lower()]

def main():
    log_file = "logs.txt"
    create_log_file(log_file)
    logs = load_logs(log_file)
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)
    
    if len(sys.argv) > 1:
        level = sys.argv[1]
        filtered_logs = filter_logs_by_level(logs, level)
        if filtered_logs:
            print(f"\nДeтaлi логів для рівня '{level.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"\nЗаписів рівня '{level.upper()}' не знайдено.")

if __name__ == "__main__":
    main()

