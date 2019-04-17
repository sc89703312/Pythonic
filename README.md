# Pythonic
让你的python代码更优雅

------

.. _idiom:

Write Idiom Python
=====================================================================


Python支持链式比较
---------------------------------------------------------------
.. code-block:: python

   # bad
   a = 5
   if a > 1 and a < 7:
       pass
   # good
   if 1 < a < 7:
       pass


Python交换变量
---------------------------------------------------------------
.. code-block:: python

   # bad
   x = 10
   y = 5
   tmp = x
   x = y
   y = tmp

   # good
   x = 10
   y = 5
   x, y = y, x


Python中替代三目运算符?:
---------------------------------------------------------------
.. code-block:: python

   # bad
   a = 10
   b = 5
   if a > b:
       c = a
   else:
       c = b
   # good
   c = a if a > b else b


拼接字符列表时，用join方法去实现
---------------------------------------------------------------
.. code-block:: python

   # bad


格式化字符时多使用format函数
---------------------------------------------------------------
.. code-block:: python

    # bad
    name = "tony"
    age = 100
    str = "myname : " + name + " my age : " + str(age)
    str1 = "myname : %s my age : %d" % (name, age)
    # good
    str2 = "myname : {} my age {}".format(name, age)


使用列表或者字典comprehension
---------------------------------------------------------------
.. code-block:: python

    # bad
    mylist = range(20)
    odd_list = []
    for e in mylist:
        if e % 2 == 1:
            odd_list.append(e)
    # good
    odd_list = [e for e in mylist if e % 2 == 1]

    # bad
    user_list = [{'name': 'lucy', 'email': 'lucy@g.com'}, {'name': 'lily', 'email': 'lily@g.com'}]
    user_email = {}
    for user in user_list:
        if 'email' in user:
            user_email[user['name']] = user['email']
    # good
    {user['name']: user['email'] for user in user_list if 'email' in user}


条件判断时，避免直接和True, False, None进行比较(==)
---------------------------------------------------------------
.. code-block:: python

   # bad
   if l == []:
       pass
   # good
   if l:    # 实际调用l.__len__() == 0
       pass

   # bad
   if something == None:
   # good, None 是单例对象
   if something is None:


使用enumerate代替for循环中的index变量访问
---------------------------------------------------------------
.. code-block:: python

   # bad
   my_container = ['lily', 'lucy', 'tom']
   index = 0
   for element in my_container:
       print '{} {}'.format(index, element)
       index += 1

   # good
   for index, element in enumerate(my_container):
       print '%d %s' % (index, element)


避免使用可变(mutable)变量作为函数参数的默认初始化值
---------------------------------------------------------------
.. code-block:: python

   # bad
   def function(l = []):
    l.append(1)
    return l

    print function()
    print function()
    print function()

    # print
    [1]
    [1, 1]
    [1, 1, 1]

    # good 使用None作为可变对象占位符
    def function(l=None):
        if l is None:
            l = []
        l.append(1)
        return l


一切皆对象
---------------------------------------------------------------
.. code-block:: python

    # bad
    def print_addition_table():
        for x in range(1, 3):
            for y in range(1, 3):
                print(str(x + y) + '\n')

    def print_subtraction_table():
        for x in range(1, 3):
            for y in range(1, 3):
                print(str(x - y) + '\n')

    def print_multiplication_table():
            for x in range(1, 3):
                for y in range(1, 3):
                    print(str(x * y) + '\n')

    def print_division_table():
        for x in range(1, 3):
            for y in range(1, 3):
                print(str(x / y) + '\n')

    print_addition_table()
    print_subtraction_table()
    print_multiplication_table()
    print_division_table()

    # good, python一切都是对象，可以函数作为参数，类似技巧可以用来简化代码
    import operator as op

    def print_table(operator):
        for x in range(1, 3):
            for y in range(1, 3):
                print(str(operator(x, y)) + '\n')

    for operator in (op.add, op.sub, op.mul, op.div):
        print_table(operator)


防御式编程EAFP vs LBYL
---------------------------------------------------------------
* EAFP：easier to ask forgiveness than permission
* LBYL：look before you leap

EAFP可以理解成一切按正常的逻辑编码，不用管可能出现的错误，等出了错误再说；而LBYL就是尽可能每写一行代码，都要提前考虑下当前的前置条件是否成立；

.. code-block:: python

    # LBYL
    def getPersonInfo(person):
        if person == None:
            print 'person must be not null!'
        print person.info

    # EAFP
    def getPersonInfo(person):
        try:
            print person.info
        except NameError:
            print 'person must be not null!'

其实用EAFP风格的代码最大的好处是代码逻辑清晰，而LBYL会导致本来两句话说清楚的事，往往因为穿插了很多条件检查的语句使代码逻辑变得混乱。Python社区更提倡EAFP形式的。另外还有一个原因，在高并发场景下， if条件如果是个表达式，会造成一致性问题，这个时候必须用EAFP形式。这个可以参考Glow团队的技术博客[Glow cache structure](http://tech.glowing.com/cn/glow-cache-structure).


用dict对象完成switch...case...的功能
---------------------------------------------------------------

.. code-block:: python

    # bad
    def apply_operation(left_operand, right_operand, operator):
        if operator == '+':
            return left_operand + right_operand
        elif operator == '-':
            return left_operand - right_operand
        elif operator == '*':
            return left_operand * right_operand
        elif operator == '/':
            return left_operand / right_operand
    # good
    def apply_operation(left_operand, right_operand, operator):
        import operator as op
        operator_mapper = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}
        return operator_mapper[operator](left_operand, right_operand)



访问tuple的数据项时，可以用namedtuple代替index的方式访问
---------------------------------------------------------------

.. code-block:: python

    # bad
    rows = [('lily', 20, 2000), ('lucy', 19, 2500)]
    for row in rows:
        print '{}`age is {}, salary is {} '.format(row[0], row[1], row[2])

    # good
    from collections import  namedtuple
    Employee = namedtuple('Employee', 'name, age, salary')
    for row in rows:
        employee = Employee._make(row)
        print '{}`age is {}, salary is {} '.format(employee.name, employee.age, employee.salary)



用isinstance来判断对象的类型
---------------------------------------------------------------
因为在python中定义变量时，不用像其它静态语言，如java， 要指定其变量数据类型，如int = 4. 但是这并不意味在python中没有数据类型，只是一个变量的数据类型是在运行的时候根据具体的赋值才最终确定。比如下面的代码是计算一个对象的长度值，如果是序列类型（str,list,set,dict）的, 直接调用len方法，如果是True, False, None则返回1，如果是数值的，则返回其int值.

.. code-block:: python

    # bad
    def get_size(some_object):
        try:
            return len(some_object)
        except TypeError:
            if some_object in (True, False, None):
            return 1
        else:
            return int(some_object)

    print(get_size('hello'))
    print(get_size([1, 2, 3, 4, 5]))
    print(get_size(10.0))

    # good
    def get_size(some_object):
        if isinstance(some_object, (list, dict, str, tuple)):
            return len(some_object)
        elif isinstance(some_object, (bool, type(None))):
            return 1
        elif isinstance(some_object, (int, float)):
            return int(some_object)


用with管理操作资源的上下文环境
---------------------------------------------------------------
在一个比较典型的场景里，如数据库操作，我们操作connection时一般要正常关闭连接，而不管是正常退出还是异常退出。如下：

.. code-block:: python

    # bad
    class Connection(object):
    def execute(self, sql):
        raise Exception('ohoh, exception!')

    def close(self):
        print 'closed the Connection'

    try:
        conn = Connection()
        conn.execute('select * from t_users')
    finally:
        conn.close()

    # good
    class Connection(object):
    def execute(self, sql):
        raise Exception('ohoh, exception!')

    def close(self):
        print 'closed the Connection'

    def __enter__(self):
        return self

    def __exit__(self, errorType, errorValue, error):
        self.close()

    with Connection() as conn:
        conn.execute('select * from t_users')


使用generator返回耗费内存的对象
---------------------------------------------------------------

.. code-block:: python

   # bad
   def f():
       # ...
       return biglist

   # good
   def f():
       # ...
       for i in biglist:
           yield i


更多资源：
---------------------------------------------------------------

* `《分享书籍[writing idiomatic python ebook]》 <http://www.cnblogs.com/jcli/p/3624904.html>`_
* `《Python 3 Patterns, Recipes and Idioms》 <https://media.readthedocs.org/pdf/python-3-patterns-idioms-test/latest/python-3-patterns-idioms-test.pdf>`_
* `《30个有关Python的小技巧》 <http://blog.jobbole.com/63320/>`_
* `《Hidden features of Python》 <http://stackoverflow.com/questions/101268/hidden-features-of-python>`_
* `《Python程序员的10个常见错误》 <http://blog.jobbole.com/68256/>`_
* `《Python高级编程slide》 <http://www.dongwm.com/archives/fen-xiang-%5B%3F%5D-ge-zhun-bei-gei-gong-si-jiang-pythongao-ji-bian-cheng-de-slide/>`_
* `《Effective Python》 <https://book.douban.com/subject/26312313/>`_
* `《编写高质量代码：改善Python程序的91个建议》 <https://book.douban.com/subject/25910544/>`_
* `《Code Like a Pythonista: Idiomatic Python》 <http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html>`_
* `《The Little Book of Python Anti-Patterns》 <http://docs.quantifiedcode.com/python-code-patterns/>`_
