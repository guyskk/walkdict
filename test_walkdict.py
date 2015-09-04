from datetime import datetime
from walkdict import walkdict, walkdict_rec


def test_1():
    d = {
        "dict": "value",
        "key": {
            "inner": "inner-value"
        },
        "list": [1, 2, 3, 4]
    }
    ls = sorted(list(walkdict(d)))
    exp = [("dict", "value"),
           ("key.inner", "inner-value"),
           ("list.[0]", 1),
           ("list.[1]", 2),
           ("list.[2]", 3),
           ("list.[3]", 4), ]
    assert ls == sorted(exp)


def test_2():
    d = {
        datetime: "value",
        "required": True,
        "validate": datetime,
    }
    ls = sorted(list(walkdict(d)))
    exp = [("$datetime", "value"),
           ("required", True),
           ("validate", datetime), ]
    assert ls == sorted(exp)


def test_3():
    d = {
        "dict": "value",
        "list-dict": [
            {
                "desc": "desc-str",
            },
            {
                "desc": "desc-str",
            },
        ],
    }

    ls = sorted(list(walkdict(d)))
    exp = [("dict", "value"),
           ("list-dict.[0].desc", "desc-str"),
           ("list-dict.[1].desc", "desc-str"), ]
    assert ls == sorted(exp)


dd = {
    "dict": {
        "inner-dict": {
            "desc": "desc-str",
            "required": True,
            "validate": "string",
        },
        "inner-list": [{
            "desc": "desc-str",
            "required": True,
            "validate": "string",
        }, {
            datetime: "desc-str",
            "required": True,
            "validate": "string",
        }],
        "inner-obj": "obj"
    },
    "list": [{
        "desc": "desc-str",
        "required": True,
        "validate": "string",
    }, {
        "desc": "desc-str",
        "required": True,
        "validate": "string",
    }],
    "str": {
        "desc": "desc-str",
        "required": True,
        "validate": "string",
    },
    "obj": "obj"
}

ddd = d = {}
for i in range(200):
    d["deep"] = {"deep": "deep"}
    d = d["deep"]
d["deep"] = [i for i in range(200)]


def test_walkdict_eq_walkdict_rec():
    assert sorted(list(walkdict(dd))) == sorted(list(walkdict_rec("", dd)))


def test_deep_dict_list():
    # assert no error
    list(walkdict(ddd))


def do_profile():
    import cProfile as profile
    from timeit import timeit

    for (k, v) in walkdict(dd):
        print "'%s' -> '%s'" % (k, v)

    print "walkdict_rec",\
        timeit("list(walkdict_rec('',dd))",
               "from __main__ import walkdict_rec,dd", number=100)
    print "walkdict    ",\
        timeit("list(walkdict(dd))",
               "from __main__ import walkdict,dd", number=100)
    print "walkdict_rec"
    profile.run("for i in range(300):list(walkdict_rec('',ddd))")
    print "walkdict    "
    profile.run("for i in range(300):list(walkdict(ddd))")

if __name__ == '__main__':
    do_profile()
