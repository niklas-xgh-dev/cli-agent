from functions.get_file_content import get_file_content

def run_tests():
    print('get_file_content("calculator", "lorem.txt"):')
    print(get_file_content("calculator", "lorem.txt"))
    print()

    print('get_file_content("calculator", "main.py"):')
    print(get_file_content("calculator", "main.py"))
    print()

    print('get_file_content("calculator", "pkg/calculator.py"):')
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()

    print('get_file_content("calculator", "/bin/cat"):')
    print(get_file_content("calculator", "/bin/cat"))
    print()

    print('get_file_content("calculator", "pkg/does_not_exist.py"):')
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print()

if __name__ == "__main__":
    run_tests()
