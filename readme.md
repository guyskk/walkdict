## walkdict 

walkdict is a tool to deep traversal dict and list
no Recursion Depth limit

walkdict可以用来深度遍历dict和list
不受dict嵌套深度限制

## usage 用法

```python
from walkdict import walkdict
d={"key":"value","inner":{"inner-key":"inner-value","list":[1,2,3,4]}}
for k,v in walkdict(d):
	print k,v
```

## note 注意事项

can't process circulation dict or list
which will cause program frozen

无法处理循环引用的dict和list
将会导致程序假死，一直运行无法正常退出

for example 例如

```python
d={"key":"value"}
d["key"]=d
for k,v in walkdict(d):
	print k,v
```

## test 测试
	
	py.test

## license 

MIT License