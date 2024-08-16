def task_1() ->str:
    a = int(1)
    b = float(1.01)
    c = str("Hellow")
    d = [2, 3, 2]
    e = bool(5 > 4)
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))




def task_2() ->str:
    a = [1, 2, 3, 5, 8, 13, 21] #последовательность Фибоначи
    print(a[:3])



def task_3(a:int) ->int:
    return a**2

task_1()
task_2()
print(task_3(3))
