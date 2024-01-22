import tensorflow as tf


def triangle_area(a, b, c):

    s = (a+b+c)/2.0

    area = tf.sqrt(s*(s-a)*(s-b)*(s-c))

    return area




