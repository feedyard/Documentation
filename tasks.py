from invoke import task

@task
def lint(ctx):
    # currently just a light weight commandline call to deal with preferred conventions
    # could look at options to use md configuration file or other extensible solution
    # along with a method for checking for dead links
    ctx.run("mdl -r ~MD009,~MD013,~MD036,~MD029,~MD001,~MD024,~MD026,~MD025,~MD033 .", pty=True)