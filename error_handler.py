import traceback, sys
def handle(e):
    print('--- htpyX error ---')
    traceback.print_exc(file=sys.stdout)
