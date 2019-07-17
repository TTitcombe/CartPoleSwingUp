# CartPoleSwingUp

*CartPoleSwingUp* is a custom gym environment, adapted from [hardmaru's version](https://github.com/hardmaru/estool/blob/master/custom_envs/cartpole_swingup.py).

*Swing-up* is a more complex version of the popular *CartPole* gym environment. In swing-up, the cart must first swing
the pole to an upright position before balancing it as in normal CartPole.

This adapted version includes a non-continuous version of the environment for use with models such as DQN.

**Note:** this env currently does not work with the latest versions of *gym*. I am working to correct this.

### How to use
Either copy the file containing the environment to your own codebase, or install the repo with `pip install git+https://github.com/TTitcombe/CartPoleSwingUp.git`.
You can then import the code with `import CartPoleSwingUp`.
Once you've imported the environment class, you can simply call `env = CartPoleSwingUpEnv()`.
However, if you do not want to hard-code an environment, I have created a helper function which defaults to gym behaviour if using any other env:
```python
from CartPoleSwingUp import make

swing_up_env = make("CartPoleSwingUp")
cartpole_env = make("CartPole-v1")
```
