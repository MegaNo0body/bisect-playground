from subprocess import call
from random import randint, choice

def name():
    """ Generates a random name """
    return str(randint(100000000, 999999999))

def commit(): 
    """ Commit current directory using a random name """
    call(['git', 'add', '.'])
    call(['git', 'commit', '-m', name()])

def files(n):
    """ Generate a list of random file names """
    f = []
    for i in range(n):
        f.append(name())
    return f

def work(commits, files, works, bug_commit):
    """ Fill given files with random numbers and executes commits,
        randomly add !BUG! to a file of given bug_commit """
    bug_commited = False
    for i in range(commits):
        for j in range(randint(1, works)):
           filename = choice(files)
           file = open(filename, 'a')
           file.write(name())
           file.write('\n')
           if bug_commited == False:
               if i == bug_commit:
                   file.write('!BUG!\n')
                   bug_commited = True
           file.close()
        commit()

def main():
    number_commits = 100
    bug_commit = randint(1, number_commits / 2)
    number_files = 3
    number_work_iterations = 30
    file_names = files(number_files)
    work(number_commits, file_names, number_work_iterations, bug_commit)

main()
