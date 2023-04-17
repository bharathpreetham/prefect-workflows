from prefect import task,flow

@task
def task_a():
    for i in range(1,1000):
        print(i*i)

@task
def task_b():
    pass

@flow
def my_flow():
    a = task_a()
    b = task_b(wait_for=[a])

my_flow()