def kwargs_decorator_generator(s):
    args, kwargs = [], []
    for elem in s.split(","):
        if "=" in elem:
            var, func = elem.split("=")
            kwargs.append((var.strip(), func.strip()))
        else:
            args.append(elem.strip())

    def decorator(func):
        def wrapper(*args_values, **kwargs_values):
            recieved_values = {}
            for arg, value in zip(args, args_values):
                recieved_values[arg] = value

            for (kwarg, f), value in zip(kwargs, args_values[len(args):]):
                recieved_values[kwarg] = value

            calculated_values = {}
            for (kwarg, f) in kwargs[len(args_values) - len(args):]:
                calculated_values[kwarg] = recieved_values[kwarg] =\
                    kwargs_values.get(kwarg, eval(f, recieved_values))

            return func(*args_values, **calculated_values)

        return wrapper

    return decorator
