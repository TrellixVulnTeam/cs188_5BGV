# tutorial.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import tensorflow as tf
import numpy as np

# Placeholder, which should be replaced with an actual numpy.array when it is
# evaluated (see 'feed_dict' below).
x = tf.placeholder(tf.float32, shape=(2, 1))

# Variables, which have a state (i.e. each of them hold a numpy.array).
W = tf.Variable(np.array([[1, 0], [0, 1], [1, 0], [0, 1]]), dtype=tf.float32)
b = tf.Variable(np.array([[1], [1], [-1], [-1]]), dtype=tf.float32)

# Tensor, which can depend on placeholders and variables. Note that this
# tensor is not a numpy.array but it can be evaluated to one when the session
# is run (see 'session.run' below).
y = tf.matmul(W, x) + b

# You need a session to actually run the computations in the graph.
session = tf.Session()

# The variables need to be initialized first before they can be used.
session.run(tf.initialize_all_variables())

# You can evaluate placeholders, variables, tensors and ops (as we will see
# later) by passing them to 'session.run'. For example, you can evaluate 'W'.
W_value = session.run(W)
print('W_value:\n%r' % W_value)

# However, if you try to evaluate 'y' without passing any other arguments,
# an error is raised since you need to specify a numpy.array to be used to
# replace the placeholder 'x'.
try:
    y_value = session.run(y)
except tf.errors.InvalidArgumentError:
    print('y depends of the placeholder x but a value for x was not specified')

# You can specify the numpy.array by passing a dict mapping placeholders to
# the numpy.arrays they should replace. You should use the keyword argument
# 'feed_dict' to specify such dict.
x_datum = np.array([[3], [7]])
y_value = session.run(y, feed_dict={x: x_datum})
print('x_datum:\n%r\ny_value:\n%r' % (x_datum, y_value))

# You can also specify ops to be performed when running the session. For
# instance, 'W2_op' is an op that updates 'W' to be twice it's value.
W2_op = tf.assign(W, W*2)
# You can pass a list to 'session.run' to do multiple evaluations at a time.
# For instance, you can pass in '[y, W2_op]', in which case 'y' is evaluated
# and 'W' is updated to be twice as much. The return value of 'session.run'
# are the evaluated numpy.arrays of the corresponding elements in the list
# that was passed in.
y_value, W2_value = session.run([y, W2_op], feed_dict={x: x_datum})
print('y_value:\n%r\nW2_value:\n%r' % (y_value, W2_value))
# If you evaluate 'y', you can see that it's using the new value of 'W'.
y2_value = session.run(y, feed_dict={x: x_datum})
print('y2_value:\n%r' % y2_value)
