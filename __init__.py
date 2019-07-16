from gym import make as gym_make

from env.cartpole_swingup import CartPoleSwingUpEnv
from env.cartpole_swingup_continuous import CartPoleSwingUpContinuousEnv


def make(env_name, *make_args, **make_kwargs):
    if env_name == "CartPoleSwingUp":
        return CartPoleSwingUpEnv()
    elif env_name == "CartPoleSwingUpContinuous":
        return CartPoleSwingUpContinuousEnv()
    else:
        return gym_make(env_name, *make_args, **make_kwargs)
