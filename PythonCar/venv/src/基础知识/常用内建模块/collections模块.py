# -*- coding: UTF-8 -*
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import ChainMap
from collections import Counter
import os,argparse


'''
collections是Python内建的一个集合模块，提供了许多有用的集合类。
namedtuple
我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：
'''
p = (1,2)
'''
但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。定义一个class又小题大做了，这时，namedtuple就派上了用场：
'''
Point = namedtuple('Point',['x','y'])
p1 = Point(1,2)
print(p1.x)
print(p1.y)

'''
namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。

可以验证创建的Point对象是tuple的一种子类：
'''
print(isinstance(p1,Point))
print(isinstance(p1,tuple))
'''
类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
'''
Circle = namedtuple('Circle',['x','y','r'])

'''
deque
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。

deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
'''
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

'''
defaultdict
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
'''
dd = defaultdict(lambda :'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

'''
OrderedDict
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
如果要保持Key的顺序，可以用OrderedDict：
'''

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

'''
ChainMap
ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。

什么时候使用ChainMap最合适？举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。

下面的代码演示了如何查找user和color这两个参数：
'''

# 构造缺省参数:
defaults = {
    'color':'red',
    'user':'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u','--user')
parser.add_argument('-c','--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)
# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

'''
Counter
Counter是一个简单的计数器，例如，统计字符出现的个数：
'''
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)
c.update('hello')
print(c)