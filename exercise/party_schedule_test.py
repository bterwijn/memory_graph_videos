import party_schedule
import party_schedule_solution
import io
import contextlib
import difflib
import colorama
from colorama import Fore, Style

exercise_functions = [
    party_schedule.exercise1,
    party_schedule.exercise2,
    party_schedule.exercise3,
    party_schedule.exercise4,
    party_schedule.exercise5,
    party_schedule.exercise6,
    party_schedule.exercise7,
    party_schedule.exercise8
]

solution_functions = [
    party_schedule_solution.exercise1,
    party_schedule_solution.exercise2,
    party_schedule_solution.exercise3,
    party_schedule_solution.exercise4,
    party_schedule_solution.exercise5,
    party_schedule_solution.exercise6,
    party_schedule_solution.exercise7,
    party_schedule_solution.exercise8
]

def main():
    colorama.init()
    schedule1 = party_schedule.schedule
    schedule2 = party_schedule_solution.schedule
    all_correct = True
    for i in range(0,len(exercise_functions)):
        print(f'=== exercise{i+1}', end='')
        exercise_functions[i](schedule1)
        solution_functions[i](schedule2)
        str1 = schedule_to_string(schedule1)
        str2 = schedule_to_string(schedule2)
        if str1 != str2:
            print()
            print_error_message(str1,str2)
            all_correct = False
            break
        else:
            print(' OK')
    if all_correct:
        print('=== All exercises OK, Great Work!!!')

def schedule_to_string(schedule):
    strbuf = io.StringIO()
    with contextlib.redirect_stdout(strbuf):
        party_schedule.print_schedule(schedule)
    return strbuf.getvalue()

def print_error_message(str1, str2):
    matcher = difflib.SequenceMatcher(None, str1, str2)
    result1, result2 = [], []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal': # Unchanged text
            result1.append(str1[i1:i2])
            result2.append(str2[j1:j2])
        elif tag == 'replace': # Highlight replaced parts
            result1.append(f"{Style.BRIGHT}{Fore.RED}{str1[i1:i2]}{Style.RESET_ALL}")
            result2.append(f"{Style.BRIGHT}{Fore.GREEN}{str2[j1:j2]}{Style.RESET_ALL}")
        elif tag == 'delete': # Highlight deletions in red
            result1.append(f"{Style.BRIGHT}{Fore.RED}{str1[i1:i2]}{Style.RESET_ALL}")
        elif tag == 'insert': # Highlight insertions in green
            result2.append(f"{Style.BRIGHT}{Fore.GREEN}{str2[j1:j2]}{Style.RESET_ALL}")
    print("=================== ERROR, Your schedule:")
    print("".join(result1),end='')
    print("=================== is not equal to correct schedule:")
    print("".join(result2),end='')

if __name__ == "__main__":
    main()
