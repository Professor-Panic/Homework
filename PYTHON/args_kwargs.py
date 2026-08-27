def args_kwargs(*args,**kwargs):
    print(f"type of args {type(args)}")
    for x in args:
        print(x)
    for k,v in kwargs.items():
        print(k,v)
args_kwargs(10,20,30,length=20)