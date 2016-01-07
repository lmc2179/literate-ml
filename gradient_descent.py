class AbstractGradientDescent(object):
    def minimize_function(self, initial_x, f_grad, iterations):
        x = initial_x
        for i in range(iterations):
            learning_rate = self._get_learning_rate(i)
            x = self._gradient_descent(f_grad, x, learning_rate)
        return x

    def _gradient_descent_step(self, f_grad, x, learning_rate):
        return x - learning_rate * f_grad(x)

    def _get_learning_rate(self, i):
        raise NotImplementedError