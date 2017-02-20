# Crawler小爬虫，总结
---
### python数据类型
- 字符串，单引号双引号-普通字符串，三引号-跨行长字符串

```python
str = 'this is string'
str = "this is also a string"
str = '''
		this is a long string
		which inclode many sustring
		and multiple lines
		'''
```

- 列表，用中括号`[]`表示，可以加入各种数据类型的数据

```python
	list = [1, 2 ,3, 4 ,5]
	multipleTypeList = ['123', 123, otherType]
```

- 元组，定义好的元组中的不能够修改，但是可以用`del`删除，`+`连接，`*`复制元组，使用`()`表示

```python
tuple = (1, 2, 3, 4, 5)
multipleTypeTuple = (1, 2, '123', otherType)
```

- 字典，无序的对象集合，相当于其它语言中的map，关联数组或哈希表，又键和对应的值组成，通过键来取值，而且键必须是独一无二的

```python
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
multipleDic = {'1' : 1, '2' : '123'}
#清空词典的所有条目
dict.clear()
#返回指定键的值，如果值不在字典中返回default值
dic.get(key, default=None)
#如果键在字典dict里返回true，否则返回false
dict.has_key(key) 
#以列表返回可遍历的(键, 值) 元组数组
dict.items() 
#以列表返回一个字典所有的键
dict.keys() 
#把字典dict2的键/值对更新到dict里
dict.update(dict2) 
#以列表返回字典中的所有值
dict.values()
```
- set集合

```python
set = set()
set.add(data)
#弹出最后一个数据并返回
set.pop()
```

- Queue，队列

```python
import Queue
myqueue = Queue.Queue(maxsize = 10)
myqueue.put(10)
#从队头删除并返回一个项目
myqueue.get()

#python queue模块的FIFO队列先进先出。
class Queue.Queue(maxsize) FIFO
#LIFO类似于堆。即先进后出。
class Queue.LifoQueue(maxsize) LIFO
#还有一种是优先级队列级别越低越先出来。
class Queue.PriorityQueue(maxsize) 优先级队列
```
  

- 去掉所有的特殊字符串，使用正则表达式 `re.sub[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）], 'replaceString', 'contentString'`

```python
#-*-coding:utf-8-*-
import re
temp = "想做/ 兼_职/学生_/ 的 、加,我Q：  1 5.  8 0. ！！？？  8 6 。0.  2。 3     有,惊,喜,哦"
temp = temp.decode("utf8")
string = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"), "".decode("utf8"),temp)
print string # 想做兼职学生的加我Q158086023有惊喜哦

```

- 对数据是否为None，字符串比较大小，相等`==`:

```python
type # 未定义的话会有NoneType的错误出现
if type is None :
	pass

string = ''
if string == '':
	pass
	
```

- 异常处理

```python
try:
	pass
except Exception,e:
	e.args
	e.message
	str(e)
```

- 编码问题
	- 对ascii和utf-8的编码装换，因为大多数都是使用utf-8字符，但是因为python默认编写时候就是用ascii来编写的，所以会出现乱码的问题
	- 写有中文字符的文件的时候，可以使用`codecs`指定编码写入
	- 在写入`csv`文件的时候需要指定csv文件为utf-8
	
```python
# Unicode编码
string = u'中国人'
#使用encode可以对Unicode进行解码
string.encode('utf-8')
#使用decode可以将编码变成Unicode的编码
string.decode('utf-8')

#需要注意的一个问题是在使用list，set，dic这种数据类型的时候，因为函数调用了__repr__()，
#所以直接用pring输出的话，即使原来就是Unicode编码，
#打印的时候，也只会出现Unicode，在终端上无法显示出对应的中文
#如果想要显示的话，需要将list，set循环遍历，dic取出键值打印才能够正确


# 普通文件写入utf-8编码
 writeFile = codecs.open(fileName, 'w', "utf-8")
 writeFile.write(content)
 writeFile.close()
 
 # 写入csv文件
 f = open(fileName, 'w')
 #设置编码为utf8
 f.write(codecs.BOM_UTF8)
 #写一行
 f.writerow(content)
 #写多行
 f.writerows(content)
 
 f.close()

``` 


