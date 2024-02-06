def frange(start: float, stop: float, step: float):
    """生成从start到stop的step步长的浮点数序列。start要大于stop， step负数

    Args:
        start (float): _description_
        stop (float): _description_
        step (float): _description_

    Yields:
        _type_: _description_
    """
    while start > stop:
        yield float("{:.3f}".format(start))
        start += step
