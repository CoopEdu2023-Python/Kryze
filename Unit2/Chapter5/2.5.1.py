# "Duck" 和 "Person" 类有相同的方法，但是"in the forest" 函数只关心参数是否拥有正确的方法，不管它的类型
# 尽管"john"是一个"Person", 但是他拥有和"Duck"也痒的方法，在函数中一样可以被正常处理，因此john也可以看成是一个"Duck"