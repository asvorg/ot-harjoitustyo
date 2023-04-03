from invoke import task

@task
def test(ctx):
    ctx.run("coverage report -m --omit=/usr/**,salasana-wallet/src/tests/**", pty = True)

@task(test)
def coverage_report(ctx):
    ctx.run("coverage html --omit=/usr/**,salasana-wallet/src/tests/**", pty=True)
