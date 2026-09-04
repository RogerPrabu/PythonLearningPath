def logger(func):
    def wrapper(*args, **kwargs):
        with open('logs.txt', 'a') as log:
            log.write("- Log -\n")
            log.write(f"Function Name: {func.__name__}\nFunction arguments: {args}\nFunction keyword arguments: {kwargs}\n\n")
            data = func(*args, **kwargs)
            log.write(f"Error: {data[0]}\nAPI Message: {data[1] if type(data[1]) == str else "Success!"}\n")
            log.write("-------\n\n")
        return data
    return wrapper