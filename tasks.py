from invoke import task

@task
def coverage_report(ctx):
    ctx.run("coverage html --omit=/usr/**,salasana-wallet/src/tests/", pty=True)

#@task(coverage)
#def coverage_report(ctx):
#    ctx.run("coverage html", pty=True)

@task
def start(ctx):
    ctx.run("python3 src/main/main.py", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src")