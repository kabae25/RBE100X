filename = '/Programs/test.py'

try:
   with open(filename, mode='r') as exfile:
       code = exfile.read()
   execCode = compile(code, filename, 'exec')
   exec(execCode)
except Exception as e:
   import sys
   sys.print_exception(e)
finally:
   import XRPLib.resetbotPLib.resetbot