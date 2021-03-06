## 生成器(generator)

> 注意:   
> Python语言中能够用for循环的都是属迭代器的方式  

### 定义
```
生成器是一次生成一个值的特殊类型函数。可以将其视为可恢复函数。调用该函数将返回一个可用于生成连续 x 值的生成器.
```

### 特点
```python
__iter__() 	# 返回iterators对象本身
next() # 每当next方法被调用时，返回下一个值直到StopIteration异常被抛出结束.

简单的说就是在函数的执行过程中，yield语句会把你需要的值返回给调用生成器的地方，
然后退出函数，下一次调用生成器函数的时候又从上次中断的地方开始执行，
而生成器内的所有变量参数都会被保存下来供下一次使用。
```

### 自带的生成器 
```python
>>> gen = xrange(3)
>>> dir(gen)			# 具有__iter__方法.
['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__getitem__', '__hash__', '__init__', '__iter__', '__len__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> generator = gen.__iter__()
>>> dir(generator)		# 具有next方法.
['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__length_hint__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'next']
>>> generator.next()
0
>>> generator.next()
1
>>> generator.next()
2
>>> generator.next()		# 抛出StopIteration异常表示结束.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
### 创建生成器   

> 示例1  
> 用class的方式实现xrange的功能.

```python
#coding:utf-8

class yrange(object):
    def __init__(self, num):
        self.num = num
        self.initial_val= 0

    def __iter__(self):
        return self

    def next(self):
        while self.initial_val < self.num:
            self.initial_val += 1
            return self.initial_val
        raise StopIteration

yx = yrange(10)
print yx

```   

> 示例2  
> 用yield实现xrange的功能.

```python
#coding:utf-8

def create_generator(N):
    i = 0
    while i < N:
        yield i
        i += 1

cg = create_generator(10) 
print cg

```  

> 示例3  
> 用class和yield的方式实现xrange的功能.

```python
#coding:utf-8

class yrange(object):
    def __init__(self, num):
        self.num = num
        self.initial_val= 0 
        
    def __iter__(self):
        return self.next()

    def next(self):
        while self.initial_val < self.num:
            self.initial_val += 1
            yield self.initial_val

gen = yrange(10)
for n in gen:
    print n
```  

> 生成器的一个应用场景

```python
# coding:utf-8

def read_file(fpath):
    block_size = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(block_size)
            if not block:
		return
            yield block
```

### 为什么会出现生成器? 
```
避免一次性或者无限制的占用较大的内存.
生成器更能节省内存开销，它的值是按需生成.
```

### 对比 ###
```
generator 生成器
iterators 迭代器
iterables 可迭代的

可以直接作用于for循环的对象统称为可迭代对象(Iterable)
可以被next()函数调用并不断返回下一个值的对象称为迭代器(Iterator)
所有的Iterable均可以通过内置函数iter()来转变为Iterator
```