def gym_render():
    import gym
    from ml_logger import logger

    env = gym.make("Reacher-v2")
    logger.print("gym Reacher-v2 is working!", color="green")
    img = env.render('rgb_array')
    logger.print(f"Reacher-v2 renders <{img.shape}>", color="green")


def gym_dmc_render():
    import gym
    from ml_logger import logger

    env = gym.make("dmc:Cartpole-balance-v1")
    logger.print(f"dmc Cartpole starts!", color="green")
    img = env.render('rgb_array')
    logger.print(f"dmc:Cartpole renders <{img.shape}>", color="green")


def mpi_import():
    print('now import MPI')
    from mpi4py import MPI
    from ml_logger import logger

    logger.print(MPI, "success!", color="green")



def both():
    from ml_logger import logger

    logger.print("this is running", color="yellow")

    gym_render()
    gym_dmc_render()

    logger.print("success", color="green")


if __name__ == "__main__":
    import jaynes

    jaynes.config(runner=dict(entry_script="mpirun python -u -m jaynes.entry"))
    jaynes.run(mpi_import)
    # jaynes.run(gym_render)
    # jaynes.run(gym_dmc_render)
    # jaynes.run(both)
    jaynes.listen()
