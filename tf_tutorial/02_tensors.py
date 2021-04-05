import tensorflow as tf
import os


os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# x = tf.constant(4, shape=(1, 1), dtype=tf.float32)
# x = tf.constant([[1, 2, 3], [4, 5, 6]])  # rank: 2
# x = tf.random.normal((3, 3), mean=3, stddev=1)  # Standar Deviation: 표준 편차 
# x = tf.random.uniform((3, 3), minval=0, maxval=1)  # uniform distribution: 균등 분포
# x = tf.range(10)
# print(x)

# # cast
# x = tf.cast(x, dtype=tf.float32)
# print(x)

# elementwise
x = tf.constant([1, 2, 3])
y = tf.constant([4, 5, 6])

z = tf.tensordot(x, y, axes=0)
print(z)