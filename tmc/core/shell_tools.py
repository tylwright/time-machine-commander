import subprocess


def run_command(cmd):
    """
    Runs shell command
    :param cmd: Command you wish to run
    :return: Output of the command you ran
    """
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output
