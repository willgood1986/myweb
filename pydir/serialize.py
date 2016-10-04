# -*- coding: utf-8 -*-

class student(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

class serialize(object):
    '''
        pickle.dumps(instance)
        pickle.dump(instance, file-handle)
        pickle.load

        json.dumps(class, default=lambda obj: obj.__dict__)
        json.loads(str, object_hook=get the instance from dict)
    '''
    def serwithpickle(self):
        import pickle
        d = dict(name='jim', age=20, address='test address')
        with open('./ser-pickle.txt','wb') as f:
            pickle.dump(d, f)

    def deserwithpickle(self):
        import pickle
        with open('./ser-pickle.txt', 'rb') as f:
            r = pickle.load(f)
            print('source %s' % r)

def dict2student(d):
    return student(d['name'], d['age'], d['address'])

if __name__ == '__main__':
    s = serialize()
    s.serwithpickle()
    s.deserwithpickle()
    stu = student('jim', 12, 'GD')
    import json
    with open('./ser-j.bin', 'w') as f:
        f.write(json.dumps(stu, default=lambda obj: obj.__dict__))

    with open('./ser-j.bin', 'r') as f:
        src = f.read()
        print('read result:' + src)
        deser = json.loads(src, object_hook=dict2student)
        print('deserilize result %r' %deser)

    print(serialize.__doc__)
