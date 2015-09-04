# coding:utf-8


def walkdict_rec(key, obj):
    """遍历dict或list
    采用递归recursion方式实现，dict嵌套不能太深，list长度也不能太大，大概不要超过100，否则会报错。
    用法：
        for k, v in walk_dict('', obj):
            print k, v
    """
    if isinstance(obj, list):
        for i, v in enumerate(obj):
            new_key = "%s[%d]." % (key, i)
            for item in walkdict_rec(new_key, v):
                yield item
    elif isinstance(obj, dict):
        for k, v in obj.items():
            if type(k) is type:
                new_key = "%s$%s." % (key, k.__name__)
            else:
                new_key = "%s%s." % (key, k)
            for item in walkdict_rec(new_key, v):
                yield item
    else:
        yield (key[:-1], obj)


def walkdict(obj):
    """遍历dict或list
    采用迭代和栈实现，不受递归深度限制，性能也更好一点。
    用法：
        for k, v in walkdict(obj):
            print k, v
    """
    stack = [("", obj)]
    while stack:
        (key, obj) = stack.pop()
        if isinstance(obj, list):
            for (k, v) in enumerate(obj):
                new_key = "%s[%d]." % (key, k)
                # 减少入栈出栈，提高性能
                if isinstance(v, (list, dict)):
                    stack.append((new_key, v))
                else:
                    yield (new_key[:-1], v)
        elif isinstance(obj, dict):
            for k in obj:
                if type(k) is type:
                    new_key = "%s$%s." % (key, k.__name__)
                else:
                    new_key = "%s%s." % (key, k)
                # 减少入栈出栈，提高性能
                if isinstance(obj[k], (list, dict)):
                    stack.append((new_key, obj[k]))
                else:
                    yield (new_key[:-1], obj[k])
        else:
            yield (key[:-1], obj)
